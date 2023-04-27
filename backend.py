import requests
API_KEY="04aa9b3763650739c4b1d3f9f32832da"
def get_data(place, days=None, type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_values=8*days
    filtered_data=filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo",days=3,type="Sky"))