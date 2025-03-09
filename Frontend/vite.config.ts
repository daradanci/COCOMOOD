import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  base: '/COCOMOOD/',
  plugins: [vue()],
  build: {
    minify: 'esbuild',  // Быстрая сборка
    sourcemap: false,   // Отключает source maps (ускоряет)
    target: 'esnext',   // Оптимизация для современных браузеров
    outDir: 'dist',
  },
});
