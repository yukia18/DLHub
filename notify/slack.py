import slackweb


def slack_notify(name, validation, score, description=''):
    """
    Send notification to slack channel.
    - `pip install slackweb`
    - URL should be set by incoming webhook.
        
    e.g. Validation method list,
    (1) holdout: train_test_split(test_size=0.2, random_state=42, shuffle=True)
    
    Args:
        name (str): your name.
        score (float): best score.
        validation (str): validation method (such as 'holdout' or 'kfold').
        descriptions (str): free form descriptions. Default to ''.

    """
    URL = "<Incoming Webhook>"
    slack = slackweb.Slack(url=URL)

    message = '[Sent by {}]\n'.format(name)
    message += 'Score: {} - {:.5f}\n'.format(validation, score)
    message += 'Descriptions: {}'.format(descriptions)

    slack.notify(text=message)

