#   lambda/delete_inventory_item/lambda_function.py
import json
import boto3

TABLE_NAME = "Inventory"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id'] # Get item ID from path

        # Delete the item from the DynamoDB table
        table.delete_item(Key={'Item id': item_id})

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item deleted successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }