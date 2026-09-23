import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/plants': {
        target: 'http://localhost:5555',
        changeOrigin: true,
      },
    },
},

})
