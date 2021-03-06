# MessageMedia Messages Python SDK
[![Travis Build Status](https://api.travis-ci.org/messagemedia/messages-python-sdk.svg?branch=master)](https://travis-ci.org/messagemedia/messages-python-sdk)
[![PyPI](https://img.shields.io/pypi/v/messagemedia-messages-sdk.svg)](https://pypi.python.org/pypi/messagemedia-messages-sdk)

The MessageMedia Messages API provides a number of endpoints for building powerful two-way messaging applications.

## ⭐️ Install via PIP
Run the following command to install the SDK via pip:
`pip install messagemedia-messages-sdk`

## 🎬 Get Started
It's easy to get started. Simply enter the API Key and secret you obtained from the [MessageMedia Developers Portal](https://developers.messagemedia.com) into the code snippet below and a mobile number you wish to send to.

### 🚀 Send an SMS
* Destination numbers (`destination_number`) should be in the [E.164](http://en.wikipedia.org/wiki/E.164) format. For example, `+61491570156`.
```python
# Configuration parameters and credentials
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import json

auth_user_name = 'YOUR_API_KEY' # The username to use with basic authentication
auth_password = 'YOUR_API_SECRET' # The password to use with basic authentication

client = MessageMediaMessagesClient(auth_user_name, auth_password)

messages_client = client.messages

body_value = '''{
    "messages":[
        {
            "content":"My first message",
            "destination_number":"YOUR_MOBILE_NUMBER"
        }
    ]
}'''

body = json.loads(body_value)

result = messages_client.create_send_messages(body)
```

### 🖼 Send an MMS
* Destination numbers (`destination_number`) should be in the [E.164](http://en.wikipedia.org/wiki/E.164) format. For example, `+61491570156`.
```python
# Configuration parameters and credentials
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import json

auth_user_name = 'YOUR_API_KEY' # The username to use with basic authentication
auth_password = 'YOUR_API_SECRET' # The password to use with basic authentication

client = MessageMediaMessagesClient(auth_user_name, auth_password)

messages_client = client.messages

body_value = '''{
    "messages":[
        {
            "content":"My first message",
            "destination_number":"YOUR_MOBILE_NUMBER",
            "format":"MMS",
            "media":["https://upload.wikimedia.org/wikipedia/commons/6/6a/L80385-flash-superhero-logo-1544.png"]
        }
    ]
}'''

body = json.loads(body_value)

result = messages_client.create_send_messages(body)
```

### 🕓 Get Status of a Message
You can get a messsage ID from a sent message by looking at the `message_id` from the response of the above example.
```python
# Configuration parameters and credentials
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import json

auth_user_name = 'YOUR_API_KEY' # The username to use with basic authentication
auth_password = 'YOUR_API_SECRET' # The password to use with basic authentication

client = MessageMediaMessagesClient(auth_user_name, auth_password)

messages_client = client.messages

message_id = 'YOUR_MESSAGE_ID'

result = messages_client.get_message_status(message_id)
print result
```

### 💬 Get replies to a message
You can check for replies that are sent to your messages
```python
# Configuration parameters and credentials
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import sys
import json

auth_user_name = 'YOUR_API_KEY' # The username to use with basic authentication
auth_password = 'YOUR_API_SECRET' # The password to use with basic authentication

client = MessageMediaMessagesClient(auth_user_name, auth_password)

replies_client = client.replies

result = replies_client.get_check_replies()
```

### ✅ Check Delivery Reports
This endpoint allows you to check for delivery reports to inbound and outbound messages.
```python
# Configuration parameters and credentials
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import sys
import json

auth_user_name = 'YOUR_API_KEY' # The username to use with basic authentication
auth_password = 'YOUR_API_SECRET' # The password to use with basic authentication

client = MessageMediaMessagesClient(auth_user_name, auth_password)

delivery_reports_client = client.delivery_reports

result = delivery_reports_client.get_check_delivery_reports()
```

## 📕 Documentation
The Python SDK Documentation can be viewed [here](DOCUMENTATION.md)

## 😕 Got Stuck?
Please contact developer support at developers@messagemedia.com or check out the developer portal at [developers.messagemedia.com](https://developers.messagemedia.com/)
