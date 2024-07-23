import requests
import json
 
url = "https://community.cloud.automationanywhere.digital/v3/automations/deploy"
 
payload = json.dumps({
  "fileId": 13252303,
  "automationName": "Prueba_API",
  "runAsUserIds": [
    639618
  ]
})
headers = {
  'X-Authorization': 'eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiI2Mzk2MTgiLCJjbGllbnRUeXBlIjoiV0VCIiwidGVuYW50VXVpZCI6IjRiNzQxZjQ5LTJkMmItNGE3Yy05ZmM0LThlNjMwZWIyMTYxMyIsIm11bHRpcGxlTG9naW4iOmZhbHNlLCJpYXQiOjE3MjE2OTg3NjMsImV4cCI6MTcyMTY5OTk2MywiaXNzIjoiQXV0b21hdGlvbkFueXdoZXJlIiwibmFub1RpbWUiOjE1NTAyOTE5NTgwMTc1MTh9.R2Tl7YK1kXE7RjTO0E8rMCn_N10xg01orUCqYJMfbuOnbe3rpt6Yi3XLIZFedH3oU9BBoOuoIkezq26cMXf0szb8yJ5RYCzA9_4Kfu_Z1xWhzZQS0Nx4zup_u0NbTWRhd4nKdiqLggU26HfGiiFXIG9-DTnOyovdSxSJHeXX95nq2WiT3XHBI3sdliCqs0IBaTQndvUTNSkda67QerAOFHxRnDFb4niO5_oQQX4zuSYhzU_HPCsAoPLbsDjpqPnsxW7JAH_X4gFlA8MX_wpjJp-iC2MTrUS0RgdZrMNuwpkyq8OFbQ1lMNYEeGWnaIOs54PoAzpMsW1ySok24Uk79A',
  'Content-Type': 'application/json'
}
 
response = requests.request("POST", url, headers=headers, data=payload)
 
print(response.text)
