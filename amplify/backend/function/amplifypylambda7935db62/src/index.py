import json
from nltk.tokenize import NLTKWordTokenizer

def handler(event, context):
  print('received event:')
  print(event)

  
  tknz = NLTKWordTokenizer()
  sent_lc_tok = tknz.tokenize('laksdjf lasdjfk alsdkf ')
  
  return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps('Hello from your new Amplify Python lambda!')
  }