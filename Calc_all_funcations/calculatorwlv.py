import math
import json

def lambda_handler(event, context):
    # Get values of a, b, and c from the input
    a = float(event['a'])
    b = float(event['b'])
    c = float(event['c'])
    # Calculate the average of a, b, and c
    average = (a + b + c) / 3

    # Calculate the middle value of a, b, and c
    middle = sorted([a, b, c])[1]

    # Calculate the value of a to the power of b
    power = a ** b

    # Calculate the square root of a squared plus b squared
    square_root = math.sqrt(a ** 2 + b ** 2)

    # Return the results in JSON format
    return {
        'statusCode': 200,
        'body': json.dumps({
            'average': average,
            'middle': middle,
            'power': power,
            'square_root': square_root
        })
    }
