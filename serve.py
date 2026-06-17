"""本地服务器 — 启动后浏览器打开 http://localhost:8000/app.html"""
import http.server
import os
import socketserver

os.chdir(os.path.dirname(__file__))
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map[".json"] = "application/json"

print(f"服务器已启动")
print(f"在浏览器打开: http://localhost:{PORT}/app.html")
print("然后菜单 →「添加到桌面」")
print("按 Ctrl+C 停止")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
