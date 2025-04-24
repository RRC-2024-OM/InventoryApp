#   lambda/get_all_inventory_items/lambda_function.py
import json
import boto3

TABLE_NAME = "Inventory"  # Replace with your actual table name
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        response = table.scan() # Scan the entire table
        items = response.get('Items', []) # Extract items from response

        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }