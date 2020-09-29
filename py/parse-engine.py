from kafka import KafkaConsumer
import json

try:
    print('Welcome to parse engine')
    consumer = KafkaConsumer('maxwell', bootstrap_servers='kafka:9092')
    for message in consumer:
        print(message)
except Exception as e:
    print(e)
    # Logs the error appropriately. 
    pass