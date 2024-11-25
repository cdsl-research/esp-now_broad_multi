import network
import espnow

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)
peer1 = mac1 #送信先設定
e.add_peer(peer1) #送信先追加
peer2 = mac2 #送信先設定
e.add_peer(peer2) #送信先追加

e.send(None, "Hello World") #データ送信
e.send(peer, b'end') #通信終了
