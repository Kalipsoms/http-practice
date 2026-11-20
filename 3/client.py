
import requests

url = "https://jsonplaceholder.typicode.com/users/1"


with requests.get(url, timeout=10) as response:
    print("HTTP-статус:", response.status_code)
    data = response.json()

print("ID:", data["id"])
print("Имя:", data["name"])
print("Логин:", data["username"])
print("Email:", data["email"])
print("Город:", data["address"]["city"])
print("Телефон:", data["phone"])
print("Сайт:", data["website"])
