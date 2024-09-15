# Training: Programming 1
# https://www.wechall.net/challenge/training/programming1/index.php

from classes.WeChall import WeChall
w = WeChall()

r = w.s.get(f"{w.base_url}/challenge/training/programming1/index.php?action=request", cookies=w.cookies)

message = r.text
print(message)

r = w.s.post(f"{w.base_url}/challenge/training/programming1/index.php?answer={message}", cookies=w.cookies)

assert 200 == r.status_code, "return code was not 200, failed"
print("challenge submitted")
