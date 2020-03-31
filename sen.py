from flask import Flask
from flask import abort
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    # WAF 200, phpinfo.php
    relative_url = '{}?{}'.format(path, request.query_string)
    if attack_request(relative_url):
        rsp_msg = 'This is WAF page. You attacked.'
        return 'Response Message: {}, Path: {}'.format(rsp_msg, path)
    return '<a href="/index.html">Index Page1</a>\n<a href="http://localhost:5000">Index Page1</a>\n<a href="/phpinfo.php">phpinfo Page</a>\n<a href="/webadmin/">Admin Page</a>'
    # return '<a href="/webadmin/">Admin Page</a>'

@app.errorhandler(404)
def not_found(error):
    return 'Site Not Found', 200

@app.route('/<path:path>')
def path(path):
    print(path)
    # WAF 200, phpinfo.php
    relative_url = '{}?{}'.format(path, request.query_string)
    if attack_request(relative_url):
        rsp_msg = 'This is WAF page. You attacked.'
        return 'Response Message: {}, Path: {}'.format(rsp_msg, path)
    # special file 200, app.xxxx, xxxx.config
    special_file, special_msg = special_prefix_suffix(path)
    if special_file:
        return 'Response Message: {}, Path: {}'.format(special_msg, path)
    # 403 for /webadmin/, 200 for /webadmin/web.7z
    if path == 'webadmin/':
        msg_403 = 'You have been forbiddened, this is forbidden page'
        return 'Response Message: {}, Path: {}'.format(msg_403, path), 403
    elif path == 'webadmin/web.7z':
        admin_page_msg = 'This is admin page, U found it, congratulation'
        return 'Response Message: {}, Path: {}'.format(admin_page_msg, path)
    # 200, redifine 404 page
    return abort(404)

def attack_request(msg):
    if '/etc/passwd' in msg or 'alert' in msg or 'phpinfo.php' in msg:
        return True
    return False

def special_prefix_suffix(msg):
    if msg.startswith('app.'):
        return True, 'This site is response for app.[anything'
    elif msg.endswith('.config'):
        return True, 'This site is response for [anything].config'
    return False, ''