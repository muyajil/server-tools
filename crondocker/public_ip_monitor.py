import requests
import os
import json
from retry import retry


def send_message_to_slack(message, markdown=True):
    data = {"text": message, "markdown": True}
    url = "https://hooks.slack.com/services/" + os.environ.get('SLACK_SERVICE_PATH')
    print(url)
    _ = requests.post(
        url,
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )


def check_and_update_content(content, path):
    if not os.path.exists(path):
        open(path, 'w').write(content)
        return True
    else:
        last_recorded_content = open(path).read().strip()
        if content != last_recorded_content:
            os.remove(path)
            open(path, 'w').write(content)
            return True
        else:
            return False


@retry(RuntimeError, delay=20)
def get_current_ip():
    current_ip = requests.get('https://api.ipify.org').text
    if len(current_ip) > 20:
        print('Error from API')
        raise RuntimeError('Error from API')
    else:
        return current_ip


current_ip = get_current_ip()
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'current_ip.txt')
changed = check_and_update_content(current_ip, file_path)
if changed:
    send_message_to_slack("Server has received a new IP Address: ```" + current_ip + "```")
