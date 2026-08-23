#!/usr/bin/env python3
"""
Gilgamis LLM Wiki — Local Dashboard Server
Rebuilds dashboard data and launches local HTTP server.
"""

import http.server
import socketserver
import webbrowser
import socket
import os
import sys
import subprocess

def get_base_dir():
    cur = os.path.dirname(os.path.abspath(__file__))
    base = os.path.abspath(os.path.join(cur, '..', '..', '..', '..'))
    if os.path.exists(os.path.join(base, 'dashboard.html')):
        return base
    if os.path.exists('dashboard.html'):
        return os.path.abspath('.')
    return base

# Ensure dashboard is built
cur_dir = os.path.dirname(os.path.abspath(__file__))
build_script = os.path.join(cur_dir, 'build_dashboard.py')
if os.path.exists(build_script):
    print("Rebuilding Gilgamis LLM Wiki dashboard data...", flush=True)
    subprocess.run([sys.executable, build_script], check=True)

BASE_DIR = get_base_dir()

def find_available_port(start_port=8080):
    for port in range(start_port, start_port + 50):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            continue
    return start_port

PORT = find_available_port(8080)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        if self.path in ('/', ''):
            self.path = '/dashboard.html'
        return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def serve():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), CustomHandler) as httpd:
        url = f"http://127.0.0.1:{PORT}/dashboard.html"
        print("=" * 60, flush=True)
        print(" Gilgamis LLM Wiki — Interactive Dashboard", flush=True)
        print(f" Serving at: {url}", flush=True)
        print(" Press Ctrl+C to stop the server.", flush=True)
        print("=" * 60, flush=True)
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nDashboard server stopped.", flush=True)

if __name__ == '__main__':
    serve()
