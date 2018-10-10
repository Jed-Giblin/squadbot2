import random


def andrews_loop(client, message):
    if message.content.find('transmog'):
        drawn = random.randint(1, 25)
        if drawn == random.randint(1, 25):
            yield from client.send_message(message.channel, 'SHUT UP ANDREW!!!!!!!!!!!!!!!!!', tts=True)
    else:
        drawn = random.randint(1, 100)
        if drawn == random.randint(1, 100):
            yield from client.send_message(message.channel, 'SHUT UP ANDREW!!!!!!!!!!!!!!!!!', tts=True)