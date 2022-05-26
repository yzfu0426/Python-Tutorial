'''JavaScript Object Notation'''
import json

# Load an JSON String to a python object
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["j1@gmail.com", "johnsmith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)
#print(data)
print(type(data))
print(type(data['people']))

#Conversion Table: https://docs.python.org/3/library/json.html#encoders-and-decoders


for person in data['people']:
    print(person['name'])