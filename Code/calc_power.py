import json

def lambda_handler(event, context):
    a = float(event['a'])
    b = float(event['b'])
    power = a ** b

    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': power
        })
    }
