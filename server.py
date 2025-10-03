#!/usr/bin/env python3
"""
Simple HTTP server for Dragon Jump development
Usage: python server.py [port]
"""

import http.server
import socketserver
import sys
import webbrowser
from pathlib import Path

def serve(port=8000):
    """Start local development server"""
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=Path(__file__).parent, **kwargs)
            
        def end_headers(self):
            # Enable CORS for Pyodide
            self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
            self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
            super().end_headers()
    
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"🐉 Dragon Jump server running at http://localhost:{port}")
        print("Press Ctrl+C to stop")
        
        # Auto-open browser
        webbrowser.open(f'http://localhost:{port}')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    serve(port)