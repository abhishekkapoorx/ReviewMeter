/** @type {import('tailwindcss').Config} */

const withMT = require("@material-tailwind/html/utils/withMT");

module.exports = withMT({
  content: ["./**/templates/**/*.{html,js}", "./**/static/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
});