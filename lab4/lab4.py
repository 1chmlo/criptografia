import sys
import base64
from Crypto.Cipher import AES, DES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

TAMANO_CLAVE_DES = 8
TAMANO_IV_DES = 8
TAMANO_CLAVE_3DES = 24
TAMANO_IV_3DES = 8
TAMANO_CLAVE_AES256 = 32
TAMANO_IV_AES = 16

# Solicitar datos de entrada
texto_plano_str = input("Ingrese el texto a cifrar (se usará para todos): ")
clave_unica_str = input("Ingrese la Clave (se ajustará para cada algoritmo): ")
iv_unico_str = input("Ingrese el IV (se ajustará para cada algoritmo): ")

texto_plano_bytes = texto_plano_str.encode('utf-8')

# DES
print("\nDES")
clave_en_bytes_des = clave_unica_str.encode('utf-8')
iv_en_bytes_des = iv_unico_str.encode('utf-8')

# Ajustar DES Key
tamano_requerido_clave = TAMANO_CLAVE_DES
if len(clave_en_bytes_des) > tamano_requerido_clave:
    print(f"Clave DES truncada. Original: {len(clave_en_bytes_des)} bytes, Requerido: {tamano_requerido_clave} bytes.")
    clave_des_bytes_ajustada = clave_en_bytes_des[:tamano_requerido_clave]
elif len(clave_en_bytes_des) < tamano_requerido_clave:
    bytes_faltantes = tamano_requerido_clave - len(clave_en_bytes_des)
    print(f"Clave DES rellenada. Original: {len(clave_en_bytes_des)} bytes, Requerido: {tamano_requerido_clave} bytes. (Añadidos {bytes_faltantes} bytes aleatorios)")
    clave_des_bytes_ajustada = clave_en_bytes_des + get_random_bytes(bytes_faltantes)
else:
    print(f"Clave DES tiene el tamaño correcto: {tamano_requerido_clave} bytes.")
    clave_des_bytes_ajustada = clave_en_bytes_des

# Ajustar DES IV
tamano_requerido_iv = TAMANO_IV_DES
if len(iv_en_bytes_des) > tamano_requerido_iv:
    print(f"IV DES truncado. Original: {len(iv_en_bytes_des)} bytes, Requerido: {tamano_requerido_iv} bytes.")
    iv_des_bytes_ajustado = iv_en_bytes_des[:tamano_requerido_iv]
elif len(iv_en_bytes_des) < tamano_requerido_iv:
    bytes_faltantes_iv = tamano_requerido_iv - len(iv_en_bytes_des)
    print(f"IV DES rellenado. Original: {len(iv_en_bytes_des)} bytes, Requerido: {tamano_requerido_iv} bytes. (Añadidos {bytes_faltantes_iv} bytes aleatorios)")
    iv_des_bytes_ajustado = iv_en_bytes_des + get_random_bytes(bytes_faltantes_iv)
else:
    print(f"IV DES tiene el tamaño correcto: {tamano_requerido_iv} bytes.")
    iv_des_bytes_ajustado = iv_en_bytes_des
    
print(f"Clave final DES (hex): {clave_des_bytes_ajustada.hex()}")

#Cifrado DES
cifrador_des = DES.new(clave_des_bytes_ajustada, DES.MODE_CBC, iv_des_bytes_ajustado)
texto_des_con_relleno = pad(texto_plano_bytes, TAMANO_IV_DES)
texto_cifrado_des_bytes = cifrador_des.encrypt(texto_des_con_relleno)
texto_cifrado_des_base64 = base64.b64encode(texto_cifrado_des_bytes).decode('utf-8')
print(f"DES Texto Cifrado (Base64): {texto_cifrado_des_base64}")

#Descifrado DES
texto_cifrado_des_para_descifrar = base64.b64decode(texto_cifrado_des_base64)
descifrador_des = DES.new(clave_des_bytes_ajustada, DES.MODE_CBC, iv_des_bytes_ajustado)
texto_descifrado_des_con_relleno = descifrador_des.decrypt(texto_cifrado_des_para_descifrar)
texto_descifrado_des_str = unpad(texto_descifrado_des_con_relleno, TAMANO_IV_DES).decode('utf-8')
print(f"DES Texto Descifrado: {texto_descifrado_des_str}")


#3DES
print("\n3DES")
clave_en_bytes_3des = clave_unica_str.encode('utf-8')
iv_en_bytes_3des = iv_unico_str.encode('utf-8')

#Ajustar 3DES Key
tamano_requerido_clave = TAMANO_CLAVE_3DES
if len(clave_en_bytes_3des) > tamano_requerido_clave:
    print(f"Clave 3DES truncada. Original: {len(clave_en_bytes_3des)} bytes, Requerido: {tamano_requerido_clave} bytes.")
    clave_3des_bytes_ajustada = clave_en_bytes_3des[:tamano_requerido_clave]
elif len(clave_en_bytes_3des) < tamano_requerido_clave:
    bytes_faltantes = tamano_requerido_clave - len(clave_en_bytes_3des)
    print(f"Clave 3DES rellenada. Original: {len(clave_en_bytes_3des)} bytes, Requerido: {tamano_requerido_clave} bytes. (Añadidos {bytes_faltantes} bytes aleatorios)")
    clave_3des_bytes_ajustada = clave_en_bytes_3des + get_random_bytes(bytes_faltantes)
else:
    print(f" Clave 3DES tiene el tamaño correcto: {tamano_requerido_clave} bytes.")
    clave_3des_bytes_ajustada = clave_en_bytes_3des

#Ajustar 3DES IV
tamano_requerido_iv = TAMANO_IV_3DES
if len(iv_en_bytes_3des) > tamano_requerido_iv:
    print(f"IV 3DES truncado. Original: {len(iv_en_bytes_3des)} bytes, Requerido: {tamano_requerido_iv} bytes.")
    iv_3des_bytes_ajustado = iv_en_bytes_3des[:tamano_requerido_iv]
elif len(iv_en_bytes_3des) < tamano_requerido_iv:
    bytes_faltantes_iv = tamano_requerido_iv - len(iv_en_bytes_3des)
    print(f"IV 3DES rellenado. Original: {len(iv_en_bytes_3des)} bytes, Requerido: {tamano_requerido_iv} bytes. (Añadidos {bytes_faltantes_iv} bytes aleatorios)")
    iv_3des_bytes_ajustado = iv_en_bytes_3des + get_random_bytes(bytes_faltantes_iv)
else:
    print(f"IV 3DES tiene el tamaño correcto: {tamano_requerido_iv} bytes.")
    iv_3des_bytes_ajustado = iv_en_bytes_3des
    
print(f"Clave final 3DES (hex): {clave_3des_bytes_ajustada.hex()}")

#Cifrado 3DES
cifrador_3des = DES3.new(clave_3des_bytes_ajustada, DES3.MODE_CBC, iv_3des_bytes_ajustado)
texto_3des_con_relleno = pad(texto_plano_bytes, TAMANO_IV_3DES)
texto_cifrado_3des_bytes = cifrador_3des.encrypt(texto_3des_con_relleno)
texto_cifrado_3des_base64 = base64.b64encode(texto_cifrado_3des_bytes).decode('utf-8')
print(f"3DES Texto Cifrado (Base64): {texto_cifrado_3des_base64}")

#Descifrado 3DES
texto_cifrado_3des_para_descifrar = base64.b64decode(texto_cifrado_3des_base64)
descifrador_3des = DES3.new(clave_3des_bytes_ajustada, DES3.MODE_CBC, iv_3des_bytes_ajustado)
texto_descifrado_3des_con_relleno = descifrador_3des.decrypt(texto_cifrado_3des_para_descifrar)
texto_descifrado_3des_str = unpad(texto_descifrado_3des_con_relleno, TAMANO_IV_3DES).decode('utf-8')
print(f"3DES Texto Descifrado: {texto_descifrado_3des_str}")
    
    
#AES
print("\nAES-256")
clave_en_bytes_aes = clave_unica_str.encode('utf-8')
iv_en_bytes_aes = iv_unico_str.encode('utf-8')

#Ajustar AES Key
tamano_requerido_clave = TAMANO_CLAVE_AES256
if len(clave_en_bytes_aes) > tamano_requerido_clave:
    print(f"Clave AES-256 truncada. Original: {len(clave_en_bytes_aes)} bytes, Requerido: {tamano_requerido_clave} bytes.")
    clave_aes_bytes_ajustada = clave_en_bytes_aes[:tamano_requerido_clave]
elif len(clave_en_bytes_aes) < tamano_requerido_clave:
    bytes_faltantes = tamano_requerido_clave - len(clave_en_bytes_aes)
    print(f"Clave AES-256 rellenada. Original: {len(clave_en_bytes_aes)} bytes, Requerido: {tamano_requerido_clave} bytes. (Añadidos {bytes_faltantes} bytes aleatorios)")
    clave_aes_bytes_ajustada = clave_en_bytes_aes + get_random_bytes(bytes_faltantes)
else:
    print(f"Clave AES-256 tiene el tamaño correcto: {tamano_requerido_clave} bytes.")
    clave_aes_bytes_ajustada = clave_en_bytes_aes

#Ajustar AES IV
tamano_requerido_iv = TAMANO_IV_AES
if len(iv_en_bytes_aes) > tamano_requerido_iv:
    print(f"IV AES-256 truncado. Original: {len(iv_en_bytes_aes)} bytes, Requerido: {tamano_requerido_iv} bytes.")
    iv_aes_bytes_ajustado = iv_en_bytes_aes[:tamano_requerido_iv]
elif len(iv_en_bytes_aes) < tamano_requerido_iv:
    bytes_faltantes_iv = tamano_requerido_iv - len(iv_en_bytes_aes)
    print(f"IV AES-256 rellenado. Original: {len(iv_en_bytes_aes)} bytes, Requerido: {tamano_requerido_iv} bytes. (Añadidos {bytes_faltantes_iv} bytes aleatorios)")
    iv_aes_bytes_ajustado = iv_en_bytes_aes + get_random_bytes(bytes_faltantes_iv)
else:
    print(f"IV AES-256 tiene el tamaño correcto: {tamano_requerido_iv} bytes.")
    iv_aes_bytes_ajustado = iv_en_bytes_aes
    
print(f"Clave final AES-256 (hex): {clave_aes_bytes_ajustada.hex()}")

# Cifrado AES
cifrador_aes = AES.new(clave_aes_bytes_ajustada, AES.MODE_CBC, iv_aes_bytes_ajustado)
texto_aes_con_relleno = pad(texto_plano_bytes, TAMANO_IV_AES)
texto_cifrado_aes_bytes = cifrador_aes.encrypt(texto_aes_con_relleno)
texto_cifrado_aes_base64 = base64.b64encode(texto_cifrado_aes_bytes).decode('utf-8')
print(f"AES-256 Texto Cifrado (Base64): {texto_cifrado_aes_base64}")

# Descifrado AES
texto_cifrado_aes_para_descifrar = base64.b64decode(texto_cifrado_aes_base64)
descifrador_aes = AES.new(clave_aes_bytes_ajustada, AES.MODE_CBC, iv_aes_bytes_ajustado)
texto_descifrado_aes_con_relleno = descifrador_aes.decrypt(texto_cifrado_aes_para_descifrar)
texto_descifrado_aes_str = unpad(texto_descifrado_aes_con_relleno, TAMANO_IV_AES).decode('utf-8')
print(f"AES-256 Texto Descifrado: {texto_descifrado_aes_str}")