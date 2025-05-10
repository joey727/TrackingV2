import requests
import webbrowser

# using open notify api to fetch ISS location


def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        position = data["iss_position"]
        latitude = position["latitude"]
        longitude = position["longitude"]
        return latitude, longitude
    else:
        raise Exception("failed to fetch data from Open Notify API")
