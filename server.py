import os
import sys
import urllib.parse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PENDULUM_FILE = os.path.join(BASE_DIR, "이중진자_시뮬레이션.html")
GRAVITY_FILE = os.path.join(BASE_DIR, "중력_시뮬레이션.html")
STAR_FILE = os.path.join(BASE_DIR, "별자리_지도.html")
AIR_FILE = os.path.join(BASE_DIR, "air.html")

class MultiSimHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        raw_path = parsed.path
        clean_path = raw_path.rstrip("/").lower()

        if clean_path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        # 🌫️ 대기 시뮬레이터 라우트: /air
        if clean_path in ("/air", "/air.html", "/대기", "/atmosphere", "/atmosphere.html"):
            target_file = AIR_FILE
        # ✨ 별자리 지도 라우트: /constellation, /sky, /star, /stars, /별자리
        elif clean_path in ("/constellation", "/constellation.html", "/sky", "/sky.html", "/star", "/star.html", "/stars", "/별자리", "/지도", "/starmap"):
            target_file = STAR_FILE
        # 🪐 중력 시뮬레이터 라우트: /gravity
        elif clean_path in ("/gravity", "/gravity.html", "/중력", "/gravity_sim"):
            target_file = GRAVITY_FILE
        # 📊 발표 프레젠테이션 라우트: /presentation, /ppt
        elif clean_path in ("/presentation", "/presentation.html", "/ppt", "/ppt.html"):
            target_file = os.path.join(BASE_DIR, "presentation.html")
        # 🌀 진자 시뮬레이터 라우트: / (기본 메인)
        elif clean_path in ("", "/", "/index", "/index.html", "/pendulum", "/pendulum.html", "/진자"):
            target_file = PENDULUM_FILE
        else:
            # 기타 정적 파일 확인
            decoded_path = urllib.parse.unquote(raw_path).lstrip("/\\")
            candidate = os.path.join(BASE_DIR, decoded_path)
            if os.path.isfile(candidate):
                target_file = candidate
            else:
                # 기본 메인(진자 시뮬레이터)으로 폴백
                target_file = PENDULUM_FILE

        try:
            with open(target_file, "rb") as f:
                content = f.read()

            content_type = "text/html; charset=utf-8"
            if target_file.endswith(".js"):
                content_type = "application/javascript; charset=utf-8"
            elif target_file.endswith(".css"):
                content_type = "text/css; charset=utf-8"
            elif target_file.endswith(".json"):
                content_type = "application/json; charset=utf-8"
            elif target_file.endswith(".png"):
                content_type = "image/png"
            elif target_file.endswith(".svg"):
                content_type = "image/svg+xml"

            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.end_headers()
            self.wfile.write(content)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            pass
        except Exception as e:
            try:
                self.send_error(500, str(e))
            except Exception:
                pass

    def do_HEAD(self):
        try:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
        except Exception:
            pass

    def log_message(self, format, *args):
        pass

class ResilientServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def handle_error(self, request, client_address):
        pass

if __name__ == "__main__":
    import time
    port = 5000
    while True:
        try:
            server = ResilientServer(("0.0.0.0", port), MultiSimHandler)
            server.serve_forever()
        except Exception:
            time.sleep(1)

