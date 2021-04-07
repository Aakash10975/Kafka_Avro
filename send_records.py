import json, uuid, ast

from confluent_kafka.avro import AvroProducer
from confluent_kafka import avro
from argparse import ArgumentParser

# from util.load_avro_schema_from_file import load_avro_schema_from_file
# from util.parse_command_line_args import parse_cmd_line_args

def load_avro_schema_from_file(schema_file):
    key_schema_string = """
    {"type": "string"}
    """
    
    key_schema = avro.loads(key_schema_string)
    value_schema = avro.load("./avro/" + schema_file)
    
    return key_schema, value_schema
    
def parse_cmd_line_args():
    arg_parser = ArgumentParser()
    
    arg_parser.add_argument("--topic", required=True, help="Topic Name")
    arg_parser.add_argument("--bootstrap-servers", required=False, default="localhost:9092", help="Bootstrap server address")
    arg_parser.add_argument("--schema-registry", required=False, default="http://localhost:8081", help="Schema Registry URL")
    arg_parser.add_argument("--schema-file", required=False, help="File name of Avro schema to use")
    arg_parser.add_argument("--record-key", required=False, type=str, help="Record key. If not provided, will be a random UUID")
    arg_parser.add_argument("--record-value", required=False, help="Record value")

    return arg_parser.parse_args()
    
       
def send_records(args):
    if args.record_value is None:
        raise AttributeError("--record-value is not provided.")
    
    if args.schema_file is None:
        raise AttributeError("--schema-file is not provided.")
        
    key_schema, value_schema = load_avro_schema_from_file(args.schema_file)
    
    producer_config = { "bootstrap.servers": args.bootstrap_servers,
                        "schema.registry.url": args.schema_registry}
    
#     producer = AvroProducer(producer_config, default_key_schema=key_schema, default_value_schema=value_schema)
    producer = AvroProducer(producer_config)
    
    key = args.record_key if args.record_key else str(uuid.uuid4())
#     value = json.loads(args.record_value)
    value = ast.literal_eval(args.record_value)
    

    try:
        producer.produce(topic=args.topic, key=key, value=value)
    except Exception as e:
        print("Exception while producing record key = {} value = {} to topic = {}: {}"\
            .format(key, value, args.topic, e))
    else:
        print("Successfully producing record value - {} to topic - {}"\
             .format(value, args.topic))
    
    producer.flush()

if __name__ == "__main__":
    send_records(parse_cmd_line_args())