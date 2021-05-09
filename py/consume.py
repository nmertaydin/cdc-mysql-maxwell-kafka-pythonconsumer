from kafka import KafkaConsumer

try:
    print('Hello. I am about to consume maxwell messages...')
    consumer = KafkaConsumer('maxwell', bootstrap_servers='kafka:9092')
    for message in consumer:
        print(message)
except Exception as e:
    print(e)
    pass