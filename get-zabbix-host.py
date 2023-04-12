import requests
import json

# Remplacez les informations de connexion ci-dessous par vos propres informations d'identification Zabbix
url = 'http://<IP_address>/zabbix/api_jsonrpc.php'
username = 'admin'
password = 'password'

# Créez une session Zabbix en utilisant l'API
def zabbix_login(url, username, password):
    payload = {
        'jsonrpc': '2.0',
        'method': 'user.login',
        'params': {
            'user': username,
            'password': password
        },
        'id': 1,
        'auth': None
    }

    response = requests.post(url, json=payload)
    return json.loads(response.content)['result']

# Récupérez tous les hosts Zabbix en utilisant l'API
def get_hosts(url, auth_token):
    payload = {
        'jsonrpc': '2.0',
        'method': 'host.get',
        'params': {
            'output': [
                'hostid',
                'name',
                'status'
            ]
        },
        'auth': auth_token,
        'id': 1
    }

    response = requests.post(url, json=payload)
    return json.loads(response.content)['result']

# Connectez-vous à Zabbix et récupérez tous les hosts
auth_token = zabbix_login(url, username, password)
hosts = get_hosts(url, auth_token)

# Affichez tous les hosts
for host in hosts:
    print(host)
