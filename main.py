import requests

def get_activity():
    response = requests.get("https://www.boredapi.com/api/activity")
    if response.status_code == 200:
        print("Activité : ", response.json()["activity"])
    else:
        print("Erreur API")

if __name__ == "__main__":
    get_activity()
