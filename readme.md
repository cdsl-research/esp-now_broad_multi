# ESP-NOWでブロードキャスト，マルチキャスト

ESP-NOWでブロードキャストやマルチキャストで通信を行うためのプログラムです．

## 環境
複数のESP32を使用しMicroPython1.22.1で実装しました．

## broadcast.py
ブロードキャストでデータを送信するプログラムです．
図に表すと以下のようになります．

![image](https://github.com/user-attachments/assets/030904a5-3bd3-4bb5-8ccc-7ca37bac8f4e)

送信元のデバイスに本プログラムを実装します．
実装したらexecfile("broadcast.py")で実行できます．

![image](https://github.com/user-attachments/assets/508e991a-6705-4313-8d48-dfa6a01cf643)


受信側には以下のように受信したデータが表示されます．

![image](https://github.com/user-attachments/assets/d4e14da3-2170-4c95-9f29-acdecb4cba67)


## multicast.py

マルチキャストでデータを送信するプログラムです．
図に表すと以下のようになります．

![image](https://github.com/user-attachments/assets/3cb6a85f-15a0-4b42-bfb8-b4d596fb4522)
この図では赤色のデバイスを送信対象としています．
送信元のデバイスに本プログラムを実装します．
mac1，mac2の部分は送信先のESP32のmacアドレスに変更してください．
実装したらexecfile("multicast.py")で実行できます．

![image](https://github.com/user-attachments/assets/6871f652-9566-40f4-9083-c5ce01ab8d13)


受信側には以下のように受信したデータが表示されます．

![image](https://github.com/user-attachments/assets/d4e14da3-2170-4c95-9f29-acdecb4cba67)

受信対象でないデバイスには何も表示されません．

![image](https://github.com/user-attachments/assets/41948d76-8550-427f-8d69-ae84122ed3e4)

## receive.py

ESP-NOWで送信されたデータを受信するプログラムです．
broadcast.pyで送信されたデータもmulticast.pyで送信されたデータもこのコードで受け取れます．
送信先のデバイスに本プログラムを実装します．
実装したらexecfile("receive.py")で実行できます．

受信できれば以下のように受信したデータが表示されます．

![image](https://github.com/user-attachments/assets/d4e14da3-2170-4c95-9f29-acdecb4cba67)

受信できない場合は何も表示されません

![image](https://github.com/user-attachments/assets/41948d76-8550-427f-8d69-ae84122ed3e4)

## 注意

multicast.pyでpeerにブロードキャストアドレスを指定してもブロードキャストにはなりません．
