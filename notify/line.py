import requests


def line_notify(message):
    """
    Send notification to LINE.
    - `pip install requests`
    - URL should be set by LINE API.
    
    Args:
        message (str): message.

    """
    # Don't forget to disable token
    line_token = "<LINE NOTIFY>"

    endpoint = 'https://notify-api.line.me/api/notify'
    payload = {'message': '\n{}'.format(message)}
    headers = {'Authorization': 'Bearer {}'.format(line_token)}

    requests.post(endpoint, data=payload, headers=headers)
