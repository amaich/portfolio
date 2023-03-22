import urllib.request
import urllib.parse
import json
import shutil
import os
import datetime
from config import *

today_dir = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M')

#получение списка подов
def get_pod_list(cluster, project, token):
    pod_list_req = urllib.request.Request(f'https://api.{cluster}.ocp.ca.sbrf.ru:6443/api/v1/namespaces/{project}/pods')
    pod_list_req.add_header('Authorization', token)
    pod_list_req.add_header('Accept', 'application/json')
    content = urllib.request.urlopen(pod_list_req)

    data = json.load(content)['items']
    pods_list = []
    for i in data:
        pods_list.append(i['metadata']['name'])

    return pods_list

#получение лога контейнера
def get_pod_log(cluster, project, pod, container, token):
    url_values = urllib.parse.urlencode({'container': container})
    url = f'https://api.{cluster}.ocp.ca.sbrf.ru:6443/api/v1/namespaces/{project}/pods/{pod}/log'
    full_url = '?'.join([url, url_values])

    print(full_url)

    pod_log_req = urllib.request.Request(full_url)
    pod_log_req.add_header('Authorization', token)
    pod_log_req.add_header('Accept', 'application/json')
    with urllib.request.urlopen(pod_log_req) as f:
        with open(today_dir + '/' + project + pod + '_log.txt', 'w') as file_log:
            file_log.write(f.read().decode('utf-8'))

#создание архива и добавление в него логов
def zip_del(dir):
    shutil.make_archive(dir, 'zip', dir)
    shutil.rmtree(dir)

#Создаем папку, в которую будут собираться логи
os.mkdir(today_dir)

#проходим циклом по всем подам, доступным в первом проекте и собираем логи только с тех, что указаны в словаре в config.py
for i in get_pod_list(os_cluster_1, os_project_1, os_token_1):
    for j in os_pod_container.keys():
        if i.startswith(j):
            get_pod_log(os_cluster_1, os_project_1, i, os_pod_container[j], os_token_1)

#проходим циклом по всем подам, доступным во втором проекте и собираем логи только с тех, что указаны в словаре в config.py
for i in get_pod_list(os_cluster_2, os_project_2, os_token_2):
    for j in os_pod_container.keys():
        if i.startswith(j):
            get_pod_log(os_cluster_2, os_project_2, i, os_pod_container[j], os_token_2)

#архивируем собранные логи
zip_del(today_dir)