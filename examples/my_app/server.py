import json
import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer

# Настройки подключения к нашей будущей БД
DB_PARAMS = {
    "dbname": "app_db",
    "user": "app_user",
    "password": "ehf,jhjc",
    "host": "127.0.0.1",
    "port": "5432"
}

class TodoHandler(BaseHTTPRequestHandler):
    # Настройка заголовков, чтобы Фронтенд мог общаться с Бэкендом (CORS)
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    # GET-запрос: Бэкенд забирает задачи из БД и отдает Фронтенду
    def do_GET(self):
        if self.path == "/tasks":
            self._set_headers()
            try:
                conn = psycopg2.connect(**DB_PARAMS)
                cur = conn.cursor()
                cur.execute("SELECT title FROM tasks;")
                tasks = [row[0] for row in cur.fetchall()]
                cur.close()
                conn.close()
                self.wfile.write(json.dumps(tasks).encode())
            except Exception as e:
                self.wfile.write(json.dumps([f"Ошибка БД: {e}"]).encode())

    # POST-запрос: Бэкенд принимает новую задачу от Фронтенда и пишет в БД
    def do_POST(self):
        if self.path == "/tasks":
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length).decode())
            
            self._set_headers()
            try:
                conn = psycopg2.connect(**DB_PARAMS)
                cur = conn.cursor()
                cur.execute("INSERT INTO tasks (title) VALUES (%s);", (post_data['title'],))
                conn.commit()
                cur.close()
                conn.close()
                self.wfile.write(json.dumps({"status": "success"}).encode())
            except Exception as e:
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode())

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), TodoHandler)
    print("Бэкенд запущен на http://127.0.0.1:8000")
    server.serve_forever()

