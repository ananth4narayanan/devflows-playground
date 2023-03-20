import json
import boto3

def lambda_handler(event, context):
    replicationInstanceARN = event["replicationInstanceARN"];
    createStatus = '';
    client = boto3.client('dms');
    response = client.describe_replication_instances(
        Filters=[
            {
                'Name': 'replication-instance-arn',
                'Values': [
                    replicationInstanceARN,
                ]
            },
        ],
        MaxRecords=99,
        Marker='string'
    )
    status= str(response['ReplicationInstances'][0]['ReplicationInstanceStatus'])
    while (status.lower() in ['deleted','deleting','failed', 'creating','modifying','upgrading','rebooting','available']):
        response = client.describe_replication_instances(
        Filters=[
            {
                'Name': 'replication-instance-arn',
                'Values': [
                    replicationInstanceARN,
                ]
            },
        ],
        MaxRecords=99,
        Marker='string'
        )
        status= str(response['ReplicationInstances'][0]['ReplicationInstanceStatus'])
        #return status;
        if(status.lower() == 'available'):
            createStatus='SUCCESS'
            arn = replicationInstanceARN;
            break
        if(status.lower() in ["deleted","deleting","failed"]):
            createStatus='FAILED'
            arn = 'Failed to create Replication Instance';
            break;
            
    return {"replicationInstanceARN":arn};
    
