FROM python:3.6-slim-stretch

COPY . /root/gm-service
RUN cd /root/gm-service && \
    pip3 install -r requirements.txt

CMD cd /root/gm-service && \
    python3 mysql_generate_kafka_data.py
