from channels import Group
from channels.auth import channel_session, channel_and_http_session_user_from_http
import json


@channel_and_http_session_user_from_http
def ws_connect(message):
    Group('chat').send({"accept": True})
    message.channel_session["username"] = message.user.username
    Group('chat').add(message.reply_channel)


@channel_session
def ws_message(message):
    Group('chat').send({
        'text': json.dumps({'message': message.content['text'],
                            'username': message.channel_session["username"]})
    })


@channel_session
def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)
