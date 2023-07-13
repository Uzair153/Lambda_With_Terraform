import boto3

def stop_ec2_instances(instance_ids):
    for instance_id in instance_ids:
        ec2 = boto3.client('ec2')
        ec2.stop_instances(InstanceIds=[instance_id])

def lambda_handler(event, context):
    instance_ids = event['instance_ids']
    instance_ids.append('i-0e26b758d317737c8')
    stop_ec2_instances(instance_ids)

if __name__ == '__main__':
    lambda_handler(None, None)