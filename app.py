from flask import Flask
from slackeventsapi import SlackEventAdapter

from config import SLACK_BOT_USER_OAUTH_TOKEN
from config import SLACK_SIGNIN_SECRET
from config import SLACK_TEST_CHANNEL
from job_boards_scrapers import LinkedIn
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

li = LinkedIn()
job_info = li.get_job_info("https://www.linkedin.com/jobs/view/3092250691/")

SlackJobPoster().post_job(
    channels=[SLACK_TEST_CHANNEL],
    job_info=job_info,
    job_board="LinkedIn",
)
