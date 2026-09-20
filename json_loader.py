import json

data={
"employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]
}




with open('data.json', 'w',newline="") as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data)
    