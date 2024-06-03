from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Decode the received data
        post_data = post_data.decode('utf-8')

        # Extract form fields
        form_fields = {}
        for field in post_data.split('&'):
            key, value = field.split('=')
            form_fields[key] = value

        # Extract uploaded files
        files = {}
        content_type = self.headers['Content-Type']
        if 'multipart/form-data' in content_type:
            boundary = content_type.split("=")[1].encode('utf-8')
            parts = post_data.split(boundary)

            for part in parts:
                if part.startswith(b'Content-Disposition: form-data'):
                    file_info, file_data = part.split(b'\r\n\r\n', 1)
                    filename = file_info.split(b'name="')[1].split(b'"')[0].decode('utf-8')
                    file_content = file_data[:-2]  # Remove trailing \r\n
                    files[filename] = file_content

        # Save files to server
        for filename, file_content in files.items():
            with open(os.path.join("path/to/save/", filename), 'wb') as f:
                f.write(file_content)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'User registered successfully!')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

