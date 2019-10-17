import json
import time
import random
import os
from kafka import KafkaProducer

KAFKA_HOST = os.environ['KAFKA_HOST']
KAFKA_PORT = os.environ['KAFKA_PORT']
KAFKA_TOPIC_OUTPUT = os.environ['KAFKA_TOPIC_OUTPUT']

producer = KafkaProducer(bootstrap_servers=['{}:{}'.format(KAFKA_HOST, KAFKA_PORT)],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    mock_data = {
        'time': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),
        'Gender':random.choice(['Male','Female']),
        'Race':random.choice(['Asian','White']),
        'position_top':random.randint(0,500),
        'position_left':random.randint(0,500),
        'position_right':random.randint(0,500)+random.randint(0,500),
        'position_bottom':random.randint(0,500)+random.randint(0,500),
    }
    print(mock_data)
    producer.send('KAFKA_TOPIC_OUTPUT', mock_data)
    time.sleep(random.uniform(0,30))
