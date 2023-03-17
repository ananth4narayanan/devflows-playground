import boto3
from datetime import datetime

def lambda_handler(event, context):
    time1=datetime.now().strftime("%d%m%Y%H%M%S%f")
    client = boto3.client('dms');
    response = client.create_replication_instance(
        ReplicationInstanceIdentifier = 'DMSDemo-'+time1,
        AllocatedStorage = 20, #event[AllocatedStorage]
        ReplicationInstanceClass = 'dms.t3.micro', #event[ReplicationInstanceClass]
        VpcSecurityGroupIds = [
            'sg-9501ebe4', #VpcSecurityGroupIds
            ],
        ReplicationSubnetGroupIdentifier = 'default-vpc-d4bc1fad', #event[ReplicationSubnetGroupIdentifier]
        MultiAZ=False,
        EngineVersion='3.4.7', #event[EngineVersion]
        AutoMinorVersionUpgrade=True,
        PubliclyAccessible=True,
        Tags=[
            {
                'Key': 'Owner', #event[TagKey]
                'Value': 'anantha.narayanan@aurea.com' #event[TagValue]
            }
        ]
        )
    arn= str(response['ReplicationInstance']['ReplicationInstanceArn'])
    return {
            'replicationInstanceARN':arn,
        }
