import requests


ip = '127.0.0.1'
port = 6800
def schedule(project,spider):
    url = f'http://{ip}:{port}/schedule.json'
    params = {
        "project":project,
        "spider":spider
    }
    r = requests.post(url,data = params)


schedule('taobao','dingdian')