# Laboratorio 2 - Script de Fuerza Bruta

## Cómo ejecutar

1. Instalar dependencias:
```bash
pip install requests
```

2. Ejecutar DVWA:
```bash
cd DVWA
docker-compose up -d
```

3. Ejecutar el script:
```bash
cd lab2
python script.py
```

El script probará combinaciones de usuarios y contraseñas contra DVWA en `http://localhost:4280`.
