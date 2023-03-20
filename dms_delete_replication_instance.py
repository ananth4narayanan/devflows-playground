import json
import boto3
import time

def lambda_handler(event, context):
    time.sleep(120)
    client = boto3.client('dms')
    response = client.delete_replication_instance(ReplicationInstanceArn = event['ReplicationInstanceArn'])
    return {"Status":response['ReplicationInstance']['ReplicationInstanceStatus']}
