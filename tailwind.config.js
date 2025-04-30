module.exports = {
  content: ['./app/templates/**/*.html'], // en vez de 'purge'
  darkMode: 'class', // DaisyUI lo necesita para aplicar temas
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: ['dark', 'light'],
  },
};