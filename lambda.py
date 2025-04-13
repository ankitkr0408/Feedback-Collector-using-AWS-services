import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Feedback')  # Make sure name matches exactly

def lambda_handler(event, context):
    print("Received event:", event)

    try:
        body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']

        item = {
            'id': str(uuid.uuid4()),
            'name': body['name'],
            'email': body['email'],
            'message': body['message'],
            'timestamp': datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({'message': 'Feedback submitted successfully!'})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({'message': 'Internal Server Error'})
        }
