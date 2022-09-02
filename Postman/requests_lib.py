import requests

req = requests.get('http://www.tutorialspoint.com/')

# Page encoding
e = req.encoding
print("Encoding: ",e)

# Response code
s = req.status_code
print("Response code: ",s)

# Response Time
t = req.elapsed
print("Response Time: ",t)


t = req.headers['Content-Type']
print("Header: ",t)

z = req.text
print("Content =", z[0:50])


in_values = {'username':'Jack','password':'Hello'}
res = requests.post('https://httpbin.org/post',data = in_values)
print(res.text)