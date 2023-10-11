def clase_ip(ip):
    octetos = int(ip.split('.')[0])
    
    if octetos <= 127:
        return "Clase A"
    elif octetos >= 128 and octetos <= 191:
        return "Clase B"
    elif octetos >= 192 and octetos <= 223:
        return "Clase C"
    elif octetos >= 224 and octetos <= 239:
        return "Clase D (multicast)"
    elif octetos >= 240 and octetos <= 255:
        return "Clase E (experimental)"
    else:
        return "Dirección IP inválida"

direccion_ip = "11.168.0.1"
ip = clase_ip(direccion_ip)
print(f"La dirección IP {direccion_ip} pertenece a {ip}")