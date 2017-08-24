# Basic_is_secure

* wget http://ksnctf.sweetduet.info/q/8/q8.pcap
* tcpdump -s 0 -n -e -x -vvv -r q8.pcap
* curl http://ksnctf.sweetduet.info/q/8/q8.pcap -o q8.pcap

* wireshark と tcpdump でパケットの流れを確認

1. 192.168.107.128 => 49.212.153.157
1. 49.212.153.157 => 192.168.107.128
  * 401 Authorization Required を返している
  * Basic認証っぽい
1. 192.168.107.128 => 49.212.153.157
  * ここで認証に必要なパスワードとuser を送っているっぽい
1. 49.212.153.157 => 192.168.107.128
  * 200 OK を返している
  * Congratulations を返しているから、一つ前にリクエストに答えがある

```
# 確認した curl コマンド
curl -v ctfq.sweetduet.info:10080

curl -v -H "Authorization: Basic cTg6RkxBR181dXg3eksyTktTSDhmU0dB" \
ctfq.sweetduet.info:80

curl -v -H "Authorization: Basic cTg6RkxBR181dXg3eksyTktTSDhmU0dB" \
-H "Credentials: true"  \
-H "q8:FLAG_5ux7zK2NKSH8fSGA" \
ctfq.sweetduet.info:80

curl -v -H "Authorization: Basic cTg6RkxBR181dXg3eksyTktTSDhmU0dB\r\n" \
-H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
-H "Accept-Encoding: gzip,deflate,sdch" \
-H "Accept-Language: ja,en-US;q=0.8,en;q=0.6" \
-H "Accept-Charset: Shift_JIS,utf-8;q=0.7,*;q=0.3" \
ctfq.sweetduet.info:10080
```

```
# wireshark で確認したら下記を認証に送っていた
Authorization: Basic cTg6RkxBR181dXg3eksyTktTSDhmU0dB\r\n
Credentials: q8:FLAG_5ux7zK2NKSH8fSGA
```

