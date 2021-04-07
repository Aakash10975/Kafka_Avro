from confluent_kafka.avro import SchemaRegistryClient, Schema


schema_str = """
    {
        "type": "record",
        "name": "user",
        "fields": [
            {"name": "firstName", "type": "string"},
            {"name": "age",  "type": "int"}
        ]
    }
"""

avro_schema = Schema(schema_str, 'AVRO')
sr = SchemaRegistryClient("http://schema-registry-host:8081")    
_schema_id = client.register_schema("yourSubjectName", avro_schema)