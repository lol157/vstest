import os
import time
from github import Auth
from github import Github
from config import AUTH_TOKEN
import requests
import socket
import json


class GitUpdater:
    def __init__(self, repo_name, branch_name='master'):
        self.g = Github(auth=Auth.Token(AUTH_TOKEN))
        self.cur_repo = self.g.get_user().get_repo(repo_name)
        self.branch_name = branch_name
        self.last_commit = self.get_latest_commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.g.close()

    def download_file(self, download_path: str):
        file_url = self.cur_repo.get_contents(download_path, self.branch_name).download_url

        while True:
            try:
                res = requests.get(file_url, timeout=60)
                res.raise_for_status()

                with open('test.exe', 'wb') as wb:
                    wb.write(res.content)
                break
            except Exception as ex:
                print(ex)
                time.sleep(300)

    @staticmethod
    def shutdown_main_program():
        msg = json.dumps({'msg': 'shutdown'}).encode()

        with socket.create_connection(("127.0.0.1", 734)) as s:
            s.sendall(msg)

    def get_latest_commit(self):
        return gu.cur_repo.get_branch(self.branch_name).commit

    def start_check_update_loop(self):
        main_file_path = './vs_build/test1.exe'
        while True:
            if self.get_latest_commit() != self.last_commit:
                self.shutdown_main_program()
                os.remove(main_file_path)
                self.download_file(main_file_path)
                os.startfile(main_file_path)
            time.sleep(300)


if __name__ == '__main__':
    with GitUpdater('vstest') as gu:
        # main_file_path = './vs_build/test1.exe'
        # gu.shutdown_main_program()
        # os.remove(main_file_path)
        # gu.download_file(main_file_path)
        # os.startfile(main_file_path)
        print()

