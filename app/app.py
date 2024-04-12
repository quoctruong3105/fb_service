from flask import Flask, request
import requests
import json
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = '63da23qw-b54c-2g6a-90ae-2f54d5jf6c82'


def callSendAPI(senderPsid, response):
    PAGE_ACCESS_TOKEN = config.PAGE_ACCESS_TOKEN
    payload = {
        'recipient': {'id': senderPsid},
        'message': response,
        'messaging_type': 'RESPONSE'
    }
    headers = {'content-type': 'application/json'}
    url = 'https://graph.facebook.com/v10.0/me/messages?access_token={}'.format(PAGE_ACCESS_TOKEN)
    r = requests.post(url, json=payload, headers=headers)
    print(r.text)
    

def handleMessage(senderPsid, receiveMessage):
    if 'text' in receiveMessage:
        response = {"text": 'You just sent me: {}'.format(receiveMessage['text'])}
        callSendAPI(senderPsid, response)
    else:
        response = {"text": 'This chatbot only accepts text messages'}
        callSendAPI(senderPsid, response )


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'HOME'


@app.route('/webhook', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        VERIFY_TOKEN = '2PK5sbFAaoxK7FqI91FuT2gZ8vn_2Q2dLJAxkbksQrU8URr3X'

        if 'hub.mode' in request.args:
            mode = request.args.get('hub.mode')
            print(mode)
        if 'hub.verify_token' in request.args:
            token = request.args.get('hub.verify_token')
            print(token)
        if 'hub.challenge' in request.args:
            challenge = request.args.get('hub.challenge')
            print(challenge)
            
        if 'hub.mode' in request.args and 'hub.verify_token' in request.args:
            mode = request.args.get('hub.mode')
            token = request.args.get('hub.verify_token')
            
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print('WEBHOOK_VERIFIED')
                challenge = request.args.get('hub.challenge')
                return challenge, 200
            else:
                return 'ERROR', 403
        
        return 'SOMETHING', 200

    if request.method == 'POST':
        VERIFY_TOKEN = '2PK5sbFAaoxK7FqI91FuT2gZ8vn_2Q2dLJAxkbksQrU8URr3X'

        if 'hub.mode' in request.args:
            mode = request.args.get('hub.mode')
            print(mode)
        if 'hub.verify_token' in request.args:
            token = request.args.get('hub.verify_token')
            print(token)
        if 'hub.challenge' in request.args:
            challenge = request.args.get('hub.challenge')
            print(challenge)
            
        if 'hub.mode' in request.args and 'hub.verify_token' in request.args:
            mode = request.args.get('hub.mode')
            token = request.args.get('hub.verify_token')
            
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print('WEBHOOK_VERIFIED')
                challenge = request.args.get('hub.challenge')
                return challenge, 200
            else:
                return 'ERROR', 403


        data = request.data
        body = json.loads(data.decode('utf-8'))
        
        if 'object' in body and body['object'] == 'page':
            entries = body['entry']
            for entry in entries:
                webhookEvent = entry['messaging'][0]
                print(webhookEvent)
                senderPsid = webhookEvent['sender']['id']
                print('Sender PSID: {}'.format(senderPsid))
                
                if 'message' in webhookEvent: 
                    handleMessage(senderPsid, webhookEvent['message'])
                    
                return 'EVENT_RECEIVED', 200
        else:
            return 'ERROR', 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3105', debug=True)
