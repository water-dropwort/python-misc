import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=35.0030&longitude=135.4616&timezone=Asia%2FTokyo&current_weather=true"
res = requests.get(url)

def print_vl():
    print("----------------------------------------------------------------")

print(res.status_code)
print_vl()
print(res.headers)
print_vl()
print(res.text)
print_vl()
print(res.content)
