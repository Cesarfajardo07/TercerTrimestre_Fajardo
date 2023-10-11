def tipo_ip(ip):
    octetos = [int(octeto) for octeto in ip.split('.')]
    
    if octetos[0] == 10:
        return "Privada"
    elif octetos[0] == 172 and octetos[1] >= 16 and octetos[1] <= 31:
        return "Privada"
    elif octetos[0] == 192 and octetos[1] == 168:
        return "Privada"
    else:
        return "Pública"


direccion_ip = "180.168.0.1"
ip = tipo_ip(direccion_ip)
print(f"La dirección IP {direccion_ip} es {ip}")