import requests

url = "https://youtube-video-grabber.p.rapidapi.com/ytGrab_v1"

payload = "url_=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQWV_fsmSF0w"
headers = {
    'x-rapidapi-host': "youtube-video-grabber.p.rapidapi.com",
    'x-rapidapi-key': "3e5d3e2bcdmshc50d0589f4ce715p1d0727jsn35e592fbb0b6",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)