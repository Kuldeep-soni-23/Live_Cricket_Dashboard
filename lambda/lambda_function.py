import json
import urllib.request

API_KEY = "a3f6b503-8980-45c9-bf61-c6a3202046c9"

def lambda_handler(event, context):

    url = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS"
        },
        "body": json.dumps(data)
    }