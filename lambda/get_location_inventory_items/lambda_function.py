#   lambda/get_location_inventory_items/lambda_function.py
import json
import boto3

TABLE_NAME = "Inventory"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)
INDEX_NAME = "Item location_id-Item id-index" # GSI name

def lambda_handler(event, context):
    try:
        location_id = int(event['pathParameters']['id']) # Get location ID from path

        # Query the GSI to get items for the given location
        response = table.query(
            IndexName=INDEX_NAME,
            KeyConditionExpression='Item location_id = :loc_id',
            ExpressionAttributeValues={':loc_id': location_id}
        )
        items = response.get('Items', [])

        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }