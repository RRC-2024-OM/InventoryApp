#   lambda/add_inventory_item/lambda_function.py
import json
import boto3
from ulid import ULID # For generating Item ID

TABLE_NAME = "Inventory"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        body = json.loads(event['body']) # Parse the request body

        # Generate a ULID for the Item ID
        item_id = str(ULID())

        # Extract data from the request
        item_name = body['Item name']
        item_description = body['Item description']
        item_qty_on_hand = body['Item qty on hand']
        item_price = body['Item price']
        item_location_id = body['Item location_id']

        # Put the item into the DynamoDB table
        table.put_item(Item={
            'Item id': item_id,
            'Item name': item_name,
            'Item description': item_description,
            'Item qty on hand': item_qty_on_hand,
            'Item price': item_price,
            'Item location_id': item_location_id
        })

        return {
            'statusCode': 201, # Created
            'body': json.dumps({'message': 'Item created successfully', 'Item id': item_id})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }