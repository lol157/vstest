import os
import requests


def get_branch_name():
    ip = requests.get('https://api.ipify.org?format=json').json()['ip']
    user = os.getlogin()

    return f'{ip}_{user}'


if __name__ == '__main__':
    print(get_branch_name())