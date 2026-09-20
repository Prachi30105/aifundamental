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