import math
import json

def lambda_handler(event, context):
    a = float(event['a'])
    b = float(event['b'])
    square_root = math.sqrt(a ** 2 + b ** 2)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': square_root
        })
    }
