// import { marked } from 'marked';

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


document.addEventListener("DOMContentLoaded", async (event) => {
    console.log("loaded")
    let aiInsightContainer = document.getElementById("ai-insight-onload");
    aiInsightContainer.innerHTML = `
    <div class="flex flex-col justify-center align-middle">
    <p class="text-center mb-3">AI writing insights...</p>
    <span class="mx-auto material-symbols-outlined text-black text-2xl animate-spin">
        progress_activity
    </span>
    </div>
    `

    const csrftoken = getCookie('csrftoken');
    const coursepathname = document.location.pathname;

    let response = await fetch(coursepathname, {
        method: 'POST',
        headers: {
            "X-CSRFToken": csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'courseid': coursepathname.split('/')[2] }),
        credentials: "same-origin"
    });
    let data = await response.json();
    if (response.status == 200) {
        aiInsightContainer.innerHTML = marked.parse(data.result)
        // aiInsightContainer.innerHTML = `<pre class="w-full">${data.result}</pre>`
    } else {
        aiInsightContainer.innerHTML = `<div class="text-red-500 text-xl font-sans">Error Occured while retriving data</div>`
    }
});