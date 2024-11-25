# ESP-NOWでブロードキャスト，マルチキャスト

ESP-NOWでブロードキャストやマルチキャストで通信を行うためのプログラムです．

## broadcast.py

ブロードキャストでデータを送信するプログラムです．送信元のESP32にこのコードを実装し，execfile("broadcast.py")と入力すると実行できます．受信側には以下のように受信したデータが表示されます．
![image](https://github.com/user-attachments/assets/aa06028a-5fb9-498a-90ad-4b91cbf6f77c)

## multicast.py

マルチキャストでデータを送信するプログラムです．mac1，mac2の部分は送信先のESP32のmacアドレスに変更してください．送信元のESP32にこのコードを実装し，execfile("multicast.py")と入力すると実行できます．受信側には以下のように受信したデータが表示されます．
![image](https://github.com/user-attachments/assets/aa06028a-5fb9-498a-90ad-4b91cbf6f77c)

## receive.py

ESP-NOWで送信されたデータを受信するプログラムです．broadcast.pyで送信されたデータもmulticast.pyで送信されたデータもこのコードで受け取れます．送信先のESP32にこのコードを実装し，execfile("receive.py")と入力すると実行できます．受信できれば以下のように受信したデータが表示されます．
![image](https://github.com/user-attachments/assets/aa06028a-5fb9-498a-90ad-4b91cbf6f77c)
