from django.shortcuts import render
from channels import Group
from django.contrib.auth.decorators import login_required


def ws_connect(message):
    Group('chat').add(message.reply_channel)


@login_required
def chat(request):
    return render(request, 'send_message.html')