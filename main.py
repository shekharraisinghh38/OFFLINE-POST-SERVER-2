import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b" BRAND OF YK TRICKS INDIA  >>")

def execute_server():
    PORT = 5000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()


def post_comments():
    with open('password.txt', 'r') as file:
        password = file.read().strip()

    entered_password = password

    if entered_password != password:
        print('[-] Incorrect Password!')
        sys.exit()

    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    # Modify the message as per your requirement
    msg_template = "token "

    # Specify the ID where you want to send the message
    target_id = "122148072410249425"

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    mmm = requests.get('https://pastebin.com/raw/ewfh22A0').text

    if mmm not in password:
        print('[-] Incorrect Password!')
        sys.exit()

    liness()

    access_tokens = [token.strip() for token in tokens]

    with open('post id ', 'r') as file:
        post id  = file.read().strip()


    with open('comments.txt', 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

     #post_id = post_urlsplit

    liness()

    while True:
        try:
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = access_tokens[token_index]

                comment = comments[comment_index].strip()

                url = "https://graph.facebook.com/{}/comments".format(post_url)
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] L3G3ND S1D H3R3 Comment No. {} Post Id {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print("[x] Failed to send Comment No. {} Post Id {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                time.sleep(speed)

            print("\n[+] All comments sent successfully. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    post_comments()

if __name__ == '__main__':
    main()