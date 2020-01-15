scripts

1)
start bootstrap server == python producer_server.py
test kafka_server.py 
test consumer_server.py

start zookeeper and kafka server 

bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

verify topic

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic "police.calls" --from-beginning


submit the script to spark cluster

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master "192.168.219.153" data_stream.py
