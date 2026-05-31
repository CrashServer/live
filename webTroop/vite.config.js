import { readFileSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const CELLS_JSON = resolve(__dirname, '../grid/cells.json');

export default {
  server: {
    port: 3000,
    host: '0.0.0.0',
    proxy: {
      // Proxy /api → grid/serve.py on port 1235.
      // When the grid server is not running the proxy emits an error;
      // we catch that and serve cells.json directly from disk so
      // cellDial works even without grid/serve.py running.
      '/api': {
        target: 'http://localhost:1235',
        changeOrigin: true,
        configure: (proxy) => {
          proxy.on('error', (_err, req, res) => {
            if (req.url === '/api/cells') {
              try {
                const data = readFileSync(CELLS_JSON, 'utf-8');
                res.writeHead(200, {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                });
                res.end(data);
              } catch {
                res.writeHead(503, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'grid server unreachable and cells.json missing' }));
              }
            } else {
              if (!res.headersSent) {
                res.writeHead(503);
                res.end('grid server unreachable');
              }
            }
          });
        },
      },
    },
  },
};
