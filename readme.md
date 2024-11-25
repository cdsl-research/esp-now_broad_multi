# ESP-NOWでブロードキャスト，マルチキャスト

ESP-NOWでブロードキャストやマルチキャストで通信を行うためのプログラムです．

## 環境
複数のESP32を使用しMicroPython1.22.1で実装しました．

## broadcast.py
ブロードキャストでデータを送信するプログラムです．
図に表すと以下のようになります．

![image](https://github.com/user-attachments/assets/030904a5-3bd3-4bb5-8ccc-7ca37bac8f4e)

図の左側のデバイスに本プログラムを実装します．
実装したら下記のコマンドで実行できます．

```
execfile("broadcast.py")
```

受信側には以下のように受信したデータが表示されます．

![image](https://github.com/user-attachments/assets/aa06028a-5fb9-498a-90ad-4b91cbf6f77c)

## multicast.py

マルチキャストでデータを送信するプログラムです．
図に表すと以下のようになります．

![image](https://github.com/user-attachments/assets/3cb6a85f-15a0-4b42-bfb8-b4d596fb4522)
この図では赤色のデバイスを送信対象としています．
図の左側のデバイスに本プログラムを実装します．
mac1，mac2の部分は送信先のESP32のmacアドレスに変更してください．
実装したら下記のコマンドで実行できます．
```
execfile("broadcast.py")
```
受信側には以下のように受信したデータが表示されます．

![image](https://github.com/user-attachments/assets/aa06028a-5fb9-498a-90ad-4b91cbf6f77c)

## receive.py

ESP-NOWで送信されたデータを受信するプログラムです．
broadcast.pyで送信されたデータもmulticast.pyで送信されたデータもこのコードで受け取れます．
先ほどの図の右側のデバイスに本プログラムを実装します．
実装したら下記のコマンドで実行できます．
```
execfile("receive.py")
```
受信できれば以下のように受信したデータが表示されます．

![image](https://github.com/user-attachments/assets/aa06028a-5fb9-498a-90ad-4b91cbf6f77c)
