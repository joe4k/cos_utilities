
import os, pprint, json
import boto3
from dotenv import load_dotenv

# load environment variable from .env file
load_dotenv()

service_endpoint=os.environ["cos_service_endpoint"]
cos_access_key_id=os.environ["cos_access_key"]
cos_secret_access_key=os.environ["cos_secret_key"]

cos_client = boto3.client('s3',
                          endpoint_url = service_endpoint,
                          aws_access_key_id=cos_access_key_id,
                          aws_secret_access_key=cos_secret_access_key)

print("service endpoint: ", service_endpoint)
print("cos access key: ", cos_access_key_id)

# Return all buckets in your COS instance
def get_all_buckets(cos_client):
    response = cos_client.list_buckets()
    return response['Buckets']
    allbuckets = []
    for bucket in response['Buckets']:
        allbuckets.append(bucket['Name'])
    return allbuckets

def get_buckets():
    # List all buckets in your COS instance
    buckets = get_all_buckets(cos_client)
    return buckets

buckets=get_all_buckets(cos_client)
print("Buckets")
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(buckets)
