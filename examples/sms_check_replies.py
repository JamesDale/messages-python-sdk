# Configuration parameters and credentials
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import sys
import json

auth_user_name = 'YOUR_API_KEY' # The username to use with basic authentication
auth_password = 'YOUR_API_SECRET' # The password to use with basic authentication

client = MessageMediaMessagesClient(auth_user_name, auth_password)

replies_client = client.replies

result = replies_client.get_check_replies()
