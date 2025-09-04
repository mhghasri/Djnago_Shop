from elasticsearch import Elasticsearch

es_client = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "Admin@123"),
    verify_certs=False      # if i have ssl
)