# import requests

# # Define your access token
# access_token = 'EABkSrogTtswBO3aSulmxV4CBu1ZClBIWdZBCD1d0ZBh6S8APJZCdxyrdefgr5G9sF0NKK3rsLPJ9QWQApljZCtQ2qW989L8HMO450ZB4TVoiZA5na95UMZAIBZAyImWXkwH74YZC1bdaAPsTZBsrXJ4qzsRfG3par0D2wEJSZAqHjdTGXkvTXOJQ4HPFAiSpRSIfEBuWTaSBarrSvvUsNS0XGQ6r0ZB5en7HMNItHpymuvJgZCC4isIZBxPdqvWZB2whZBRhTYbaqrYomP9AF6L0ZD'

# # Define the recipient's ID and the message text
# recipient_id = '61556698799810'
# message_text = 'Hello, this is a test message from the Send API!'

# # Construct the message payload
# message = {
#     'recipient': {'id': recipient_id},
#     'message': {'text': message_text}
# }

# # Send the message using the Send API
# url = 'https://graph.facebook.com/v13.0/me/messages?access_token=' + access_token
# response = requests.post(url, json=message)

# # Check if the message was sent successfully
# if response.status_code == 200:
#     print('Message sent successfully!')
# else:
#     print('Failed to send message. Status code:', response.status_code)
#     print('Response:', response.json())
import requests

# Define your access token
access_token = 'EABkSrogTtswBO3aSulmxV4CBu1ZClBIWdZBCD1d0ZBh6S8APJZCdxyrdefgr5G9sF0NKK3rsLPJ9QWQApljZCtQ2qW989L8HMO450ZB4TVoiZA5na95UMZAIBZAyImWXkwH74YZC1bdaAPsTZBsrXJ4qzsRfG3par0D2wEJSZAqHjdTGXkvTXOJQ4HPFAiSpRSIfEBuWTaSBarrSvvUsNS0XGQ6r0ZB5en7HMNItHpymuvJgZCC4isIZBxPdqvWZB2whZBRhTYbaqrYomP9AF6L0ZD'

# Define the recipient's ID and the message text
recipient_id = '61556698799810'
message_text = 'Hello, this is a test message from the Send API!'

# Construct the message payload
message = {
    'recipient': {'id': recipient_id},
    'message': {'text': message_text}
}

# Send the message using the Send API
url = f'https://graph.facebook.com/v19.0/me/messages?access_token={access_token}'
# print(url)
# curl -i -X GET \
 # "https://graph.facebook.com/v19.0/me?fields=id%2Cname&access_token=EABkSrogTtswBO3aSulmxV4CBu1ZClBIWdZBCD1d0ZBh6S8APJZCdxyrdefgr5G9sF0NKK3rsLPJ9QWQApljZCtQ2qW989L8HMO450ZB4TVoiZA5na95UMZAIBZAyImWXkwH74YZC1bdaAPsTZBsrXJ4qzsRfG3par0D2wEJSZAqHjdTGXkvTXOJQ4HPFAiSpRSIfEBuWTaSBarrSvvUsNS0XGQ6r0ZB5en7HMNItHpymuvJgZCC4isIZBxPdqvWZB2whZBRhTYbaqrYomP9AF6L0ZD"
response = requests.post(url, json=message)

# Check if the message was sent successfully
if response.status_code == 200:
    print('Message sent successfully!')
else:
    print('Failed to send message. Status code:', response.status_code)
    print('Response:', response.json())
