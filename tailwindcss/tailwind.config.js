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
        'twitter-blue': '#1DA1F2',
        'twitter-green': '#19c981',
        'twitter-red': '#fd187d',
      },
      opacity: {
        '15': '.15',
      },
      transitionDuration: {
        '50': '50ms',
        '250': '250ms',
      }
    },
  },
  plugins: [],
}
