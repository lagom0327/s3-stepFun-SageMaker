import json
import urllib.parse
import boto3
import os

print('Loading function')

s3 = boto3.client('s3')
client = boto3.client('stepfunctions')
state_machine_name = os.environ.get('state_machine_name')
runtime_region = os.environ['AWS_REGION']

def lambda_handler(event, context):
    aws_account_id = context.invoked_function_arn.split(":")[4]
    print(aws_account_id)
    #print("Received event: " + json.dumps(event, indent=2))
    my_state_machine_arn = f"arn:aws:states:{runtime_region}:{aws_account_id}:stateMachine:{state_machine_name}"
    print(my_state_machine_arn)
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    record = event['Records'][0]
    print(record)
    for record in event['Records']:
        response = client.start_execution(
            stateMachineArn=my_state_machine_arn,
            input=json.dumps(record['s3'])
        )
    
