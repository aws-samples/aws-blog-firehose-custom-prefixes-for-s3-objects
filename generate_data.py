import json
from datetime import datetime
import base64
import time
import random
import boto3
done = False
 
client = boto3.client('firehose')
while (not done):
 
    event = {}
    ticker = ['WMT', 'AWD', 'QXZ', 'WER', 'TOI', 'YYT', 'UFG']
    event['ticker_symbol'] = random.choice(ticker)
    ticker_sector = {'WMT': 'RETAIL', 'AWD': 'MANUFACTURING', 'QXZ': 'HEALTHCARE', 'WER': 'FINSERV', 'TOI': 'HOSPITALITY', 'YYT': 'REAL ESTATE', 'UFG': 'TRANSPORTATION'}
    event['sector'] = ticker_sector[event['ticker_symbol']]
    event['price'] = round(random.uniform(1.0, 200.0), 2)
    event['change'] = round(random.uniform(1.0, 25.0), 2)
    now = time.time()
    event[u'EventTime'] = datetime.utcfromtimestamp(now).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    event_str = json.dumps(event)
 
    client.put_record(DeliveryStreamName='KDFS3customPrefixesExample',
            Record={
                'Data': event_str
    }
    )
 