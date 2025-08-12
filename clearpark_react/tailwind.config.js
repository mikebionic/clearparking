module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      backgroundColor: {
        glass: 'rgba(255,255,255,0.1)',
      },
      blur: {
        'glass': '20px'
      },
      height: {
        '100vh': '100vh'
      }
    },
  },
  variants: {
    extend: { 
    },
  },
  plugins: [],
}
