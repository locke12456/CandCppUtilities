import requests
def get_google_home():
    data = requests.get("https://www.google.com.tw")
    print data.text
    return 0
rule = { "r":get_google_home }
def load():
    rule["r"]()
    print("module1 was loaded")
