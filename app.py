from flask import Flask
from slackeventsapi import SlackEventAdapter

from config import JOB_POSTING_CHANNEL
from config import SLACK_BOT_USER_OAUTH_TOKEN
from config import SLACK_SIGNIN_SECRET
from slack_bot import SlackJobPoster


app = Flask(__name__)


print(SLACK_BOT_USER_OAUTH_TOKEN)
print(SLACK_SIGNIN_SECRET)


slack_ev_adapter = SlackEventAdapter(SLACK_SIGNIN_SECRET, "/slack/events", app)


# @slack_ev_adapter.on('message')
# def message(payload):
#     event = payload.get('event', {})
#     text = event.get('text')

#     if 'say_hello' in text.lower():
#         msg = 'hello world!'
#         MESSAGE_SCHEMA['text']['text'] = msg
#         x = {'channel': JOB_POSTING_CHANNEL, 'blocks': [MESSAGE_SCHEMA]}
#         return slack_wclient.chat_postMessage(**x)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)


msg = ">> hello world!"
SlackJobPoster().post_message(
    channels=JOB_POSTING_CHANNEL,
    message="check out this cool bot!",
    attachments=[
        {
            "fallback": "How is it going?",
            "color": "#36a64f",
            "title": "Luan is testing this bot",
            "footer": "This is a test message",
            "text": "This is just a test message\nMute this channel if you want!",
        }
    ],
)
