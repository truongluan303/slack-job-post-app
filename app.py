import base64
import logging
import math
from functools import lru_cache
from urllib import parse as urlparse

from flask import Flask
from slackeventsapi import SlackEventAdapter

from config import SLACK_SIGNIN_SECRET


app = Flask(__name__)


_LOGGER = logging.getLogger(__name__)


slack_ev_adapter = SlackEventAdapter(SLACK_SIGNIN_SECRET, "/slack/events", app)


@lru_cache(maxsize=60)
def isPrime(i):
    if i in [2, 3]:  # shortcut low primes
        return True
    else:
        if i % 2 == 0 or i % 3 == 0:  # special since we go 3-> sqrt
            return False
        sqrt = int(math.sqrt(i) // 1)
        for s in range(
            3, sqrt + 1, 2
        ):  # check odd vals, or all prior primes + new primes
            if i % s == 0:
                return False
        return True


commands = {"isprime": isPrime, "prime": isPrime}  # map of command aliases


def lambda_handler(event, context):
    # data comes b64 and also urlencoded name=value& pairs
    msg_map = dict(
        urlparse.parse_qsl(base64.b64decode(str(event["body"])).decode("ascii"))
    )
    command = msg_map.get("command", "err")  # will be /command name
    params = msg_map.get("text", "err").split(" ")  # params ['isPrime','50']
    subcommand = params[0].lower()

    if len(params) < 2:
        response = f"available subcommands: {list(commands.keys())} + 1 parameter"
    elif subcommand in commands.keys():
        response = (
            f"{subcommand} needs an numeric param"
            if len(params) < 2
            else f"{subcommand} = {commands[subcommand](int(float(params[1])))}"
        )
    else:
        response = f"illegal sub command >{subcommand}<, commands available {list(commands.keys())}"

    # logging
    print(
        str(command)
        + " "
        + str(params)
        + " -> "
        + response
        + ",original: "
        + str(msg_map)
    )

    return {
        "response_type": "in_channel",
        "text": command + " " + " ".join(params),
        "attachments": [{"text": response}],
    }
