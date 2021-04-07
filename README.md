# Kafka_Avro
This repository have the sample python code to read and write to and from Kafka.

For a tutorial on how this repository was built and how it works, go to this [article](https://medium.com/@billydharmawan/avro-producer-with-python-and-confluent-kafka-library-4a1a2ed91a24?source=friends_link&sk=b845dae5da1761d3a8c8f53d610eac33) (for Avro Producer part) and [this](https://medium.com/@billydharmawan/consume-messages-from-kafka-topic-using-python-and-avro-consumer-eda5aad64230?source=friends_link&sk=9d64b23845664a41710856270d81f36a) (for Avro Consumer part).

Sample Command:
pip install < requirements.txt
python send_records.py --topic sample-topic --schema-file create-user-request.avsc --record-value '{"email": "email@email.com", "firstname": "Bob", "lastname": "Jones"}
	Successfully producing record value - {'email': 'email@email.com', 'firstName': 'Bob', 'lastName': 'Jones'} to topic - create-user-request


python consume_records.py --topic sample-topic
	Successfully poll a record from Kafka topic: sample-topic, partition: 0,                    offset: 0
	message key: 73f41876-c4c3-4c8d-921e-49aa6955144a || message value: {u'lastname': u'Jones', u'email': u'email@email.com', u'firstname': u'Bob'}