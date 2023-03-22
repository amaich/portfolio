#первая квота
os_cluster_1 = 'prom-terra000083-i39m'
os_project_1 = 'ci02473893-pprb4-samo-synapse-megacod'
os_token_1 = 'Bearer sha256~ua5fphyQ9b3wrUadOVmyKwHRlXN4E78KJfFhlZa-Rmc'

#вторая квота
os_cluster_2 = 'prom-terra000082-i39s'
os_project_2 = 'ci02473893-pprb4-samo-synapse-skol'
os_token_2 = 'Bearer sha256~H-r-Mo7udJwuRlxiUMgshZ_9Ukcl91ukataMEHCQeoo'

#словарь в котором хранятся имена подов и контейнеров, с которых нужно собирать логи в формате:
#ИМЯ_ПОДА: ИМЯ_КОНТЕЙНЕРА
os_pod_container = {
    'istio-egressgateway': 'istio-proxy',
    'istio-ingressgateway': 'istio-proxy',
    'samo-synapse-tasks': 'samo-synapse-tasks',
    'samo-synapse-facade': 'samo-synapse-facade',

}