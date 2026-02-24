import { resolve } from 'path';

export default {
    server: {
      port: 3000,
      host: '0.0.0.0'  // Pour accès réseau local
    },
    build: {
      rollupOptions: {
        input: {
          main: resolve(__dirname, 'index.html'),
          video: resolve(__dirname, 'video.html'),
        },
      },
    },
  }
