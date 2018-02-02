# EasyCipher

* https://ksnctf.sweetduet.info/problem/2

## 解き方

* 全然意味わからないけど、問題的に 暗号分っぽい
* 暗号分を検索したら 暗号化の形式が沢山ある
* 同じ単語が複数回出てきているので、アルファベット1文字が別のアルファベットに対応してそう

__シーザー暗号にあたりを付けて、アルファベット1文字ずつずらしていこう__

* [cipher_decod.py](./cipher_decod.py) を利用して 1文字ずつずらしていった
* 13回目に 意味がありそうな文字列になった

```
$ python cipher_decod.py
['E', 'B', 'G', ' ', 'K', 'V', 'V', 'V', ' ', 'v', 'f', ' ', 'n', ' ', 'f', 'v', 'z', 'c', 'y', 'r', ' ', 'y', 'r', 'g', 'g', 'r', 'e', ' ', 'f', 'h', 'o', 'f', 'g', 'v', 'g', 'h', 'g', 'v', 'b', 'a', ' ', 'p', 'v', 'c', 'u', 'r', 'e', ' ', 'g', 'u', 'n', 'g', ' ', 'e', 'r', 'c', 'y', 'n', 'p', 'r', 'f', ' ', 'n', ' ', 'y', 'r', 'g', 'g', 'r', 'e', ' ', 'j', 'v', 'g', 'u', ' ', 'g', 'u', 'r', ' ', 'y', 'r', 'g', 'g', 'r', 'e', ' ', 'K', 'V', 'V', 'V', ' ', 'y', 'r', 'g', 'g', 'r', 'e', 'f', ' ', 'n', 's', 'g', 'r', 'e', ' ', 'v', 'g', ' ', 'v', 'a', ' ', 'g', 'u', 'r', ' ', 'n', 'y', 'c', 'u', 'n', 'o', 'r', 'g', '.', ' ', 'E', 'B', 'G', ' ', 'K', 'V', 'V', 'V', ' ', 'v', 'f', ' ', 'n', 'a', ' ', 'r', 'k', 'n', 'z', 'c', 'y', 'r', ' ', 'b', 's', ' ', 'g', 'u', 'r', ' ', 'P', 'n', 'r', 'f', 'n', 'e', ' ', 'p', 'v', 'c', 'u', 'r', 'e', ',', ' ', 'q', 'r', 'i', 'r', 'y', 'b', 'c', 'r', 'q', ' ', 'v', 'a', ' ', 'n', 'a', 'p', 'v', 'r', 'a', 'g', ' ', 'E', 'b', 'z', 'r', '.', ' ', 'S', 'y', 'n', 't', ' ', 'v', 'f', ' ', 'S', 'Y', 'N', 'T', 'F', 'j', 'm', 't', 'k', 'O', 'W', 'F', 'N', 'Z', 'd', 'j', 'k', 'k', 'N', 'H', '.', ' ', 'V', 'a', 'f', 'r', 'e', 'g', ' ', 'n', 'a', ' ', 'h', 'a', 'q', 'r', 'e', 'f', 'p', 'b', 'e', 'r', ' ', 'v', 'z', 'z', 'r', 'q', 'v', 'n', 'g', 'r', 'y', 'l', ' ', 'n', 's', 'g', 'r', 'e', ' ', 'S', 'Y', 'N', 'T', '.']
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
ROT XIII is a simple letter substitution cipher that replaces a letter with the letter XIII letters after it in the alphabet  ROT XIII is an example of the Caesar cipher  developed in ancient Rome  Flag is FLAGSwzgxBJSAMqwxxAU  Insert an underscore immediately after FLAG
```

## まとめ

* シーザー暗号の問題だったみたい
  * 全部13文字分ずらしただけのROT13という暗号らしい
* pythonは標準でROT13をデコードする機能がある らしい
  * [cipher_rot13.py](./cipher_rot13.py) がその機能を使って問いたスクリプト
