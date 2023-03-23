#первая квота
os_cluster_1 = '***'
os_project_1 = '***'
os_token_1 = '***'

#вторая квота
os_cluster_2 = '***'
os_project_2 = '***'
os_token_2 = '***'

#словарь в котором хранятся имена подов и контейнеров, с которых нужно собирать логи в формате:
#ИМЯ_ПОДА: ИМЯ_КОНТЕЙНЕРА
os_pod_container = {
    'istio-egressgateway': '***',
    'istio-ingressgateway': '***',
    'samo-synapse-tasks': '***',
    'samo-synapse-facade': '***',

}
