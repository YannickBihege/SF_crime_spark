import asyncio

from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient, NewTopic


BROKER_URL = "PLAINTEXT://192.168.219.153:9092"
TOPIC_NAME = "police.calls"



async def consume(topic_name):
    """Consumes data from the Kafka Topic"""

    c = Consumer(
        {"bootstrap.servers": BROKER_URL, "group.id": "1"}
    )

   
    c.subscribe([topic_name])

    while True:
        
        message = c.poll(1.0)

      
        if message is None:
            print("no message received by consumer")
        elif message.error() is not None:
            print(f"error from consumer {message.error()}")
        else:
            print(f"consumed message {message.key()}: {message.value()}")
        await asyncio.sleep(1)



def main():
    """Runs the exercise"""

    try:
        asyncio.run(consume(TOPIC_NAME))
    except KeyboardInterrupt as e:
        print("shutting down")
   


if __name__ == "__main__":
    main()
