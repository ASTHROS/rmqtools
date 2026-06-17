from datetime import datetime
import json

from rmqtools import RmqConnection

rmq = RmqConnection(host='rabbit')
rmq.set_status_exchange('status')

response_count = {'ok': 0, 'down': 0}
response_count_2 = {'ok': 0, 'down': 0}
msg_times = [datetime.now()]
msg_times_2 = [datetime.now()]

@rmq.subscribe_status('device_logs', ['spec.*.status'])
def handle_response(channel, method, properties, body):
    print(body)

rmq.run()
