from confluent_kafka import avro

def load_avro_schema_from_file(schema_file):
    key_schema_string = """
    {"type": "string"}
    """
    
    key_schema = avro.loads(key_schema_string)
    value_schema = avro.load("/Users/aakash10975/kafka_avro/Kafka_Avro/avro/" + schema_file)
    
    return key_schema, value_schema
    