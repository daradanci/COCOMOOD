import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

export default defineConfig({
  base: '/COCOMOOD/',
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),  // Добавляем alias для @/
    },
  },
  build: {
    minify: 'esbuild',  // Быстрая сборка
    sourcemap: false,   // Отключает source maps (ускоряет)
    target: 'esnext',   // Оптимизация для современных браузеров
    outDir: 'dist',
  },
});
