import slackweb


def slack_notify(message):
    """
    Send notification to slack channel.
    - `pip install slackweb`
    - URL should be set by incoming webhook.

    Args:
        message (str): message.

    """
    # Don't forget to disable token
    url = "<Incoming Webhook>"

    slack = slackweb.Slack(url=url)
    slack.notify(text=message)
