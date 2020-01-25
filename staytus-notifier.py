import json
import requests
import os

url = '{}/api/v1/services/set_status'.format(os.environ['NOTIFY_PARAMETER_1'])
token = os.environ['NOTIFY_PARAMETER_2']
secret = os.environ['NOTIFY_PARAMETER_3']

service = os.environ['NOTIFY_HOSTALIAS']
status = os.environ['NOTIFY_HOSTSTATE']

headers = {'X-Auth-Token': token, 'X-Auth-Secret': secret,
           'Content-Type': 'application/json'}
data = json.dumps({'status': status, 'service': service})

r = requests.post(url, data=data, headers=headers)
# print(r.text)
