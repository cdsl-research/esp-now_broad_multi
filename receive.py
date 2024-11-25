import network
import espnow

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)

while True:
    host, msg = e.recv() #データ受信
    if msg:
        print(host, msg)
        if msg == b'end': #通信終了
            break
