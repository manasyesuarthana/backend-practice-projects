import requests
import sys

"""
Types of activities in github request API:
- PushEvent
- WatchEvent
- CreateEvent
- etc...
"""
USERS_API = "https://api.github.com/users/"
ENDPOINT = "/events"

if len(sys.argv) < 2:
    print("Usage: python3 github-activity.py <github_username> -- Check a user's github activity")
    exit(0)

username = sys.argv[1]

response = requests.get(USERS_API + username + ENDPOINT)
if response.status_code != 200:
    print("Failed to fetch github user data.")
    exit(1)
elif response.status_code == 404:
    print("Github user not found.")
    exit(0)

user_activity = response.json()

for activity in user_activity:
    event_type = activity["type"][:-5]
    repo = activity["repo"]["name"]

    if event_type == "Watch":
        event_type = "Watch or Star"

    if event_type == "Push":
        commit_amount = len(activity["payload"].get("commits", []))
        print(f"{username} pushed {commit_amount} commits to {repo}.")
    else:
        print(f"{username} did {event_type} on {repo}.")
    
exit(0)
