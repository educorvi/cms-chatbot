import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue({
      template: {
        compilerOptions: {
          isCustomElement: (tag) => tag.includes('cms-chatbot-webchat')
        }
      },
      customElement: true
    })],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  define: { 'process.env.NODE_ENV': '"production"' },
  build: {
    outDir: 'webcomponent_dist',
    lib: {
      entry: './src/webcomponent.ce.ts',
      name: 'cms-chatbot-webchat',
      // the proper extensions will be added
      fileName: 'cms-chatbot-webchat',
      formats: ["es", "umd", "cjs"]
    },

  },
})
