import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
#print(response)
req = response.status_code
user_name = response.json()
if req == 200:
    print("udało się dostać do strony")
    print(f"dane użytkownika to {user_name}")
else:
    print(f"coś poszło nie tak kod błedu to {req}")