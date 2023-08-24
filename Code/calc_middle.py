import json

def lambda_handler(event, context):
    a = float(event['a'])
    b = float(event['b'])
    c = float(event['c'])
    middle = sorted([a, b, c])[1]

    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': middle
        })
    }
