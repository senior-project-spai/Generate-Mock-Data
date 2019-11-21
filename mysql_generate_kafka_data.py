import json
import time
import random
import os
from kafka import KafkaProducer
import string

KAFKA_HOST = os.environ['KAFKA_HOST']
KAFKA_PORT = os.environ['KAFKA_PORT']
KAFKA_TOPIC_OUTPUT = os.environ['KAFKA_TOPIC_OUTPUT']


def resultsGenerator(n):
    results = []
    for _ in range(n):
        results.append(
            {
                'gender': {
                    'gender': random.choice(['Male', 'Female']),
                    'confident': random.random(),
                },
                'race': {
                    'race': random.choice(['Asian', 'White', 'Black']),
                    'confident': random.random(),
                },
                'top': random.randint(0, 500),
                'right': random.randint(0, 500),
                'bottom': random.randint(0, 500)+random.randint(0, 500),
                'left': random.randint(0, 500)+random.randint(0, 500),
            }
        )
    return results


def main():
    producer = KafkaProducer(bootstrap_servers=['{}:{}'.format(
        KAFKA_HOST, KAFKA_PORT)], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    while True:
        mock_data = {
            'time': int(time.time()),
            'Gender': random.choice(['Male', 'Female']),
            'Race': random.choice(['Asian', 'White', 'Black']),
            'position_top': random.randint(0, 500),
            'position_left': random.randint(0, 500),
            'position_right': random.randint(0, 500)+random.randint(0, 500),
            'position_bottom': random.randint(0, 500)+random.randint(0, 500),
        }

        mock_data = {
            'results': resultsGenerator(random.randint(1, 5)),
            'filepath': 's3://face-image/' + ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + "." + random.choice(['png', 'jpg']) + ".mock",
            'time': int(time.time()),
            'branch_id': random.choice([1, 2, 3, 4, 5]),
            'camera_id': random.choice([1, 2, 3, 4, 5]),
        }

        print(mock_data)
        producer.send(KAFKA_TOPIC_OUTPUT, mock_data)
        sleep_time = random.uniform(0, 10)
        time.sleep(sleep_time)
        print("Sleep: " + str(sleep_time))


if __name__ == '__main__':
    main()
