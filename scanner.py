# Simple Port Scanner - IUT FV Bandjoun
# By DAGHELA WABO WILFRIED DURAND
import socket

def scan_port(ip, port):
  try:
    s = socket.socket()
    s.settimeout(0.5)
    s.connect((ip, port))
    s.close()
    return True
  except:
    return False

target = "127.0.0.1"
print(f"Scan de {target}...")
for port in [22, 80, 443, 8080]:
  if scan_port(target, port):
    print(f"Port {port} OUVERT")
  else:
    print(f"Port {port} fermé")
