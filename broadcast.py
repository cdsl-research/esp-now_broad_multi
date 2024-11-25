import network
import espnow

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)
peer = b'\xbb\xbb\xbb\xbb\xbb\xbb' #送信先設定
e.add_peer(peer) #送信先追加

e.send(peer, "Hello World") #データ送信
e.send(peer, b'end') #通信終了
