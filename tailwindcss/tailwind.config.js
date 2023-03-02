/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["../views/*.html"],
  theme: {
    fontSize: {
      '13': '13px',
      '14': '14px',
      '15': '15px',
      '17': '17px',
      '20': '20px',
    },

    extend: {
      colors: {
        'twitter-search-bg': '#202327',
        'twitter-light-grey': '#e7e9ea',
        'twitter-grey': '#71767B',
        'twitter-dark-hover': '#181818', 
        'twitter-right-box-bg': '#16181C',
        'twitter-line': '#2F3336',
        'twitter-blue': {
          original: '#1DA1F2',
          hover: '#1A8CD8',
        },
        'twitter-icons': {
          green: '#19cf86',
          'green-bg-hover': '#071A14',
          red: '#fb197d',
          'red-bg-hover': '#200914',
          'blue-bg-hover': '#0A171F'
        }
      },
    },
  },
  plugins: [],
}
