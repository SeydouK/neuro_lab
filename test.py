response = [
    {
        "id": 1,
        "Message": "text"
    },
    {
        "id": 13,
        "Message": "text"
    },
    {
        "id": 41,
        "Message": "text"
    }
]

for i in response:
    print(i['id'], i['Message'])