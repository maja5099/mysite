/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["../views/*.html"],
  theme: {
    extend: {
      colors: {
        'twitter-dark-grey': '#16181C',
        'twitter-grey': '#2f3335',
        'twitter-light-grey': '#626264', 
        // search: #767676
        // light text: #E7E9EA
        // dark text: #71767B
        // right box: #16181C
        'twitter-blue': {
          original: '#1DA1F2',
          hover: '#1A8CD8',
        },
        'twitter-icons': {
          green: '#19cf86',
          red: '#fb197d',
        }
      },
      gridColumn: {
        'span-1.5': 'span 1.5 / span 1.5',
      }
    },
  },
  plugins: [],
}
