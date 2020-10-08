import json
import logging
from botocore.vendored import requests

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
def lambda_handler(event, context):
    logger.debug(event)
    timezone = event['currentIntent']['slots']['Timezone']
    weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Butwal, Nepal&APPID=6f5035581541af152fef5536c87468a2')
    weather_dict = json.loads(weather.text)
    data = weather_dict['weather'][0]['description']
    # text = 'The weather is - ' + data + '.'
    return {
        'sessionAttributes': event['sessionAttributes'],
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {
                'contentType': 'PlainText',
                'content': 'The weather is - ' + data + '.\nThank you'
            }
        }
    }