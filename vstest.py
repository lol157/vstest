import os
import time
from github import Auth
from github import Github
from config import AUTH_TOKEN
import sys
import socket
import json
import threading


# class GitImporter:
#     def __init__(self, repo_name):
#         self.g = Github(auth=Auth.Token(AUTH_TOKEN))
#         self.cur_repo = self.g.get_user().get_repo('vstest')
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.g.close()
#
#     def get_module_text(self, module_name):
#         return self.cur_repo.get_contents(f'modules/{module_name}').decoded_content.decode('utf-8')

# создаём ветку
# запускаем апдейтер
# переходим к коду

shutdown_flag = False


def listener():
    global shutdown_flag

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 734))
    srv.listen(1)

    while not shutdown_flag:
        srv.settimeout(1)
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue

        data = json.loads(conn.recv(1024).decode())

        if data.get('msg') == 'shutdown':
            conn.sendall(json.dumps({'msg': os.getpid()}).encode())
            shutdown_flag = True


def test_job():
    while True:
        time.sleep(3)
        if shutdown_flag:
            break
        print('doing job1')


if __name__ == '__main__':
    threading.Thread(target=listener, daemon=True).start()

    test_job()
