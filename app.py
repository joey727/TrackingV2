import webbrowser
import requests
from time import sleep

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
        raise Exception("failed to fetch data from API")


# display location in browser via google maps
def display_location_in_browser(latitude: float, longitude: float):
    google_map_url = f"https://www.google.com/maps?q={latitude},{longitude}"
    webbrowser.open(google_map_url, new=0)


if __name__ == "__main__":
    while True:
        try:
            lat, long = get_iss_location()
            print(f"current ISS location: latitude {lat}, longitude {long}")
            display_location_in_browser(lat, long)
            sleep(130)  # 3 min refresh
        except Exception as e:
            print(f"An error occurred: {e}")
