from channels import Group
import json


def ws_message(message):
    Group('chat').send({
        "text": message.content['text'],
    })

# def ws_message(message):
#     Group('chat').send({'text': json.dumps({'message': message.content['text']})})

#
# def ws_disconnect(message):
#     Group('chat').discard(message.reply_channel)
