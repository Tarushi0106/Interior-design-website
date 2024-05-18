import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('db-proj')  # Replace 'YourTableName' with your DynamoDB table name

def lambda_handler(event, context):
    try:
        # Extract values from the event
        fullname = event.get('fullname', '')
        email = event.get('email', '')
        password = event.get('password', '')

        # Generate unique UID
        uid = str(uuid.uuid4())

        # Insert record into DynamoDB
        table.put_item(
            Item={
                'uid': uid,
                'fullname': fullname,
                'email': email,
                'password': password
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data saved successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Error saving data to DynamoDB: {str(e)}'})
        }
        