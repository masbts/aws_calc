import json

def lambda_handler(event, context):
    a = float(event['a'])
    b = float(event['b'])
    c = float(event['c'])
    average = (a + b + c) / 3

    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': average
        })
    }
