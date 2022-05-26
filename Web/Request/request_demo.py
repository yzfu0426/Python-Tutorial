#https://www.youtube.com/watch?v=tb8gHvYlCFs&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=101&ab_channel=CoreySchafer
import requests

url = "https://xkcd.com/353/"

r = requests.get(url)

#print(r)
#print(type(r))
#print(dir(r)) #attributes and methods
#print(help(r))
#print(r.text) #text of the response in unicode


image_url = "https://imgs.xkcd.com/comics/python.png"
img_r = requests.get(image_url)
#print(img_r.content)

with open('comic.png', 'wb') as f: #wb: write bytes
    f.write(img_r.content) 

print(img_r.status_code)
print(img_r.ok)
#print(img_r.headers)

print("---------------------------------------------------")

#https://httpbin.org/

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)

#Produce the correct url 
print(r.url)
print("---------------------------------------------------")

payload = {"username": "Yuzhu", "age": 22, "isProgrammer": True, "password": "123"}
r = requests.post('https://httpbin.org/post', data=payload)
#print(r.text)
r_dict = r.json()
print(r_dict['form'])

print("---------------------------------------------------")
# authtication

r = requests.get("https://httpbin.org/basic-auth/Yuzhu/123"
                , auth=('Yuzhu', '123'))


print(r.text)
print(r)

print("---------------------------------------------------")
r = requests.get("https://httpbin.org/delay/1", timeout = 3)

print(r)