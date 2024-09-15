# Training: No DNS
# https://www.wechall.net/challenge/training/net/nodns/index.php
from classes.WeChall import WeChall
import socket

w = WeChall()

ip_addr = ""
results = socket.getaddrinfo("wechall.net", None)

for result in results:
    family, _, _, _, sockaddr = result
    address = sockaddr[0]

    if family == socket.AF_INET:
        ip_addr = address


r = w.s.get(f"https://{ip_addr}/challenge/training/net/nodns/etc/hosts.php", headers={'Host': 'make.love.not.war.com'}, cookies=w.cookies, verify=False)

assert 200 == r.status_code
print("challenge submitted")
