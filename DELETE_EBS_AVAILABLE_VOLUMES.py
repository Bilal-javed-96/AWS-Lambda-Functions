DELETE_EBS_AVAILABLE_VOLUMES_THROUGH_LAMBDA_FUNCTION
#python 3.7

import boto3
import json

def lambda_handler(event,context):
                                                              
    regions=['us-east-1','us-east-2','us-west-1','us-west-2'] #regions = in regions where your instances are deployed
    
    for j in regions:                                         #loop,so that code will be executed in regions defined in regions list
       
        ec2 = boto3.client('ec2', region_name=j)
        filterList = [{'Name': 'status', 'Values': ['available']}]
        response = ec2.describe_volumes(Filters=filterList, MaxResults=500)
        
        for v in response['Volumes']:
            ec2.delete_volume(VolumeId=v['VolumeId'])
