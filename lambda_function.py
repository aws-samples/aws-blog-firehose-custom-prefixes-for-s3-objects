from __future__ import print_function
 
import base64
from datetime import datetime
import time
import json
 
def lambda_handler(event, context):
    print('Loading function')
    recordNum = 1
    okRecords = 0
    processingFailedRecords = 0
 
    output = []
 
    for record in event['records']:
    
        payload = json.loads(base64.b64decode(record['data']))
        approxArrTimestampUTCFH_str = datetime.strftime(datetime.fromtimestamp(record['approximateArrivalTimestamp']/1000),'%Y-%m-%dT%H:%M:%S.%fZ')
        payload[u'ApproxArrTimestampUTCFH'] = approxArrTimestampUTCFH_str
    
    
        try:
            approxArrTimestampUTC_str = record['kinesisRecordMetadata']['approximateArrivalTimestamp']
            payload[u'ApproxArrTimestampUTCKDS'] = approxArrTimestampUTC_str
        except KeyError:
            pass
    
        if recordNum % 10 == 0:
            result = "ProcessingFailed"
            processingFailedRecords += 1
        else:
            result = "Ok"
            okRecords += 1
            
        recordNum += 1
    
        output_record = {
            'recordId': record['recordId'],
            'result': result,
            'data': base64.b64encode(json.dumps(payload) + "\n")
        }
        output.append(output_record)
 
    print('Successfully processed {} record(s).'.format(okRecords))
    print('Failed to process {} record(s).'.format(processingFailedRecords))
    print('Records Received {} record(s).'.format(len(event['records'])))
    return {'records': output}
 