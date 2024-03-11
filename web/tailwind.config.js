/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./main/templates/main/.html",
    "./templates/.html",
    "./templates/includes/.html",
    "./templates/registration/*.html",
  ],
  theme: {
    extend: {
      colors: {
        midnight: '#0D2951',
        light_blue: '#52C5F2',
        gray: '#2b2d42',
        red: '#F25041',
        ghost_white: '#F8F8FF',
      },
    },
  },
  // ... autres configurations Tailwind
}