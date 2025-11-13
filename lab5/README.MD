para realizar la captura se utilizan 2 terminales:

- Terminal 1: Captura.

```bash
sudo docker exec -it nombre_contenedor_cliente bash
tcpdump -i any -w /capturas/captura_completa.pcapng
```

- Terminal 2: Conexión SSH.

```bash
sudo docker exec -it C1 bash  
ssh prueba@nombre_contenedor_server
```

luego poner la contraseña *prueba*