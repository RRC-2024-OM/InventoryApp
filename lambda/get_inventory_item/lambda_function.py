#   lambda/get_inventory_item/lambda_function.py
import json
import boto3

TABLE_NAME = "Inventory"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id'] # Get item ID from path

        response = table.get_item(Key={'Item id': item_id}) # Get item from table
        item = response.get('Item')

        if item:
            return {
                'statusCode': 200,
                'body': json.dumps(item)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Item not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }