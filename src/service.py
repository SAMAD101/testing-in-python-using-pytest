import requests

database = {
    "team7": {
        "name": "Team 7",
        "members": ["Kakashi", "Naruto", "Sasuke", "Sakura", ],
    },
}


def get_team_details(team_name):
    return ("""
    Team Name: {name}
    Members: {members}
    """.format(**database[team_name]))


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError("Something went wrong")

