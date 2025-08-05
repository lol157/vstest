import time
import requests


print(requests.get('https://api.ipify.org?format=json').json()['ip'])
time.sleep(10)

#  pyinstaller test.py -n "test1" -F --distpath "./vs_build" --workpath "./vs_build/build" --specpath "./vs_build/spec" --clean
# pyinstaller update.py -n "update" -F --distpath "./vs_build" --workpath "./vs_build/build" --specpath "./vs_build/spec" --clean
# pyinstaller vstest.py -n "vstest" -F --distpath "./vs_build" --workpath "./vs_build/build" --specpath "./vs_build/spec" --clean