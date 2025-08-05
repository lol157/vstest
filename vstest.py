from github import Auth
from github import Github
from config import AUTH_TOKEN
import sys


class GitImporter:
    def __init__(self, repo_name):
        self.g = Github(auth=Auth.Token(AUTH_TOKEN))
        self.cur_repo = self.g.get_user().get_repo('vstest')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.g.close()

    def get_module_text(self, module_name):
        return self.cur_repo.get_contents(f'modules/{module_name}').decoded_content.decode('utf-8')

