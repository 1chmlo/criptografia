para configurar el usuario prueba se utiliza el comando

```bash
useradd -m -s /bin/bash prueba && \
    echo 'prueba:prueba' | chpasswd
```

para realizar la captura se utilizan 2 terminales:

- Terminal 1: Captura.

```bash
sudo docker exec -it nombre_contenedor_cliente bash
tcpdump -i any -w /capturas/captura.pcapng
```

- Terminal 2: Conexión SSH.

```bash
sudo docker exec -it C1 bash  
ssh prueba@nombre_contenedor_server
```

luego poner la contraseña *prueba*