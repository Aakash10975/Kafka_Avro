from confluent_kafka.avro import AvroConsumer
from argparse import ArgumentParser


def parse_cmd_line_args():
    arg_parser = ArgumentParser()
    
    arg_parser.add_argument("--topic", required=True, help="Topic Name")
    arg_parser.add_argument("--bootstrap-servers", required=False, default="localhost:9092", help="Bootstrap server address")
    arg_parser.add_argument("--schema-registry", required=False, default="http://localhost:8081", help="Schema Registry URL")
    arg_parser.add_argument("--schema-file", required=False, help="File name of Avro schema to use")
    arg_parser.add_argument("--record-key", required=False, type=str, help="Record key. If not provided, will be a random UUID")
    arg_parser.add_argument("--record-value", required=False, help="Record value")

    return arg_parser.parse_args()
    
def consume_record(args):
    default_group_name = "default-consumer-group"

    consumer_config = {"bootstrap.servers": args.bootstrap_servers,
                       "schema.registry.url": args.schema_registry,
                       "group.id": default_group_name,
                       "auto.offset.reset": "earliest"}

    consumer = AvroConsumer(consumer_config)

    consumer.subscribe([args.topic])

    try:
        message = consumer.poll(5)
    except Exception as e:
        print("Exception while trying to poll messages - {}".format(e))
    else:
        if message:
            print("Successfully poll a record from Kafka topic: {}, partition: {}, \
                   offset: {}\nmessage key: {} || message value: {}"\
                      .format(message.topic(), message.partition(), message.offset(),
                      message.key(), message.value()))
            consumer.commit()
        else:
            print("No new messages at this point. Try again later.")

    consumer.close()


if __name__ == "__main__":
    consume_record(parse_cmd_line_args())