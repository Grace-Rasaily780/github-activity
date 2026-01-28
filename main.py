from datetime import datetime
import argparse
import requests

def fetch_data(username):
    response = requests.get(f"https://api.github.com/users/{username}/events", timeout=10)
    response.raise_for_status()
    return response.json()

def parse_data(data):
    for activity in data:
        time = datetime.strptime(activity['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        if activity['type'] == 'CreateEvent': 
            print(f"{time} | Repo {activity['repo']['name']}")
        elif activity['type'] == 'PushEvent':
            print(f"{time} | Code pushed in {activity['repo']['name']}")
        elif activity['type'] == 'WatchEvent':
            print(f"{time} | Started to watch {activity['repo']['name']}")
        elif activity['type'] == 'PullRequestEvent':
            print(f"{time} | PR created in {activity['repo']['name']}")

def main():
    parser = argparse.ArgumentParser(description="List the activities from GitHub")
    parser.add_argument("username", help="GitHub Username")
    args = parser.parse_args()

    data = fetch_data(args.username)
    parse_data(data)
    
if __name__ == "__main__":
    main()
