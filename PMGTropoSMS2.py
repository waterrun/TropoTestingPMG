import requests

url = "https://api.tropo.eu/1.0/sessions"

querystring = {"action":"create","token":"547a797266697277416756594c446a466a427a48484e6c434f74434f7a596e50566f44584879757a75616461"}

payload = "myString=FromGitHub%20Adding%20lots%20of%20text%20in%20test%207%20ProntoPro&myNumber=%2B447900550902"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'postman-token': "c22ed1f2-0b27-e2a0-a0f7-9e50b96a8809"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
