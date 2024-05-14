
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


const getcourse = async (id) => {
    let coursenameinput = document.getElementById(id);
    let coursename = coursenameinput.value;

    let comparebtn = document.getElementById("compare-btn");
    comparebtn.disabled = true;

    let coursecontainer = document.getElementById(`${id}-container`);
    coursecontainer.classList.remove("hidden");
    if (coursename === "") {
        coursecontainer.innerHTML = "";
        return;
    }

    if (document.getElementById("course1").value !== "" & document.getElementById("course2").value !== "") {
        comparebtn.disabled = false;
    } 

    // let coursedata = new FormData();
    // coursedata.append('coursename', coursename);

    const csrftoken = getCookie('csrftoken');
    let response = await fetch('/compare/getcourse/', {
        method: 'POST',
        headers: {
            "X-CSRFToken": csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'coursename': coursename }),
        credentials: "same-origin"
    });
    let data = await response.json();
    if (response.status == 200) {
        coursecontainer.innerHTML = "";
        data.courses.forEach(element => {
            coursecontainer.innerHTML += `
            <div class="inline-flex items-center">
                        <label class="relative flex items-center p-3 -mt-5 rounded-full cursor-pointer" for="id-${element.id}">
                            <input name="${id}-radio" type="radio"
                                class="before:content[''] peer relative h-5 w-5 cursor-pointer appearance-none rounded-full border border-blue-gray-200 text-gray-900 transition-all before:absolute before:top-2/4 before:left-2/4 before:block before:h-12 before:w-12 before:-translate-y-2/4 before:-translate-x-2/4 before:rounded-full before:bg-blue-gray-500 before:opacity-0 before:transition-opacity checked:border-gray-900 checked:before:bg-gray-900 hover:before:opacity-10"
                                id="id-${element.id}" required value="${element.id}" />
                            <span
                                class="absolute text-gray-900 transition-opacity opacity-0 pointer-events-none top-2/4 left-2/4 -translate-y-2/4 -translate-x-2/4 peer-checked:opacity-100">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 16 16" fill="currentColor">
                                    <circle data-name="ellipse" cx="8" cy="8" r="8"></circle>
                                </svg>
                            </span>
                        </label>
                        <label class="mt-px font-light text-gray-700 cursor-pointer select-none flex flex-wrap justify-between" for="id-${element.id}">
                            <img src="${element.course_image}" class="rounded h-32 w-60 object-cover">
                            <div class="w-80 p-5">
                                <p class="block font-sans text-base antialiased font-medium leading-relaxed text-blue-gray-900">
                                    ${element.course_name}
                                </p>
                                <p class="block font-sans text-sm antialiased font-normal leading-normal text-gray-700">
                                    ${element.author}
                                </p>
                            </div>
                        </label>
                    </div>
            `
        });
        
    } else {
        console.log(response.status);
    }
};