mport urllib2
import requests
import json
gh_url = 'https://rets.io/api/v1/vendors?access_token=9d03053cd517e6c33c0656b0174fffd9&limit=1'
r = requests.get(gh_url)
req = urllib2.Request(gh_url)
print json.loads(r.text)

#POST
#r = requests.post('http://httpbin.org/post', json={"key": "value"})
#r.status_code , r.json()
#url = "http://localhost:8080"
#data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
#headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
#r = requests.post(url, data=json.dumps(data), headers=headers)


