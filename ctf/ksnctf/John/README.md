# John

* https://ksnctf.sweetduet.info/problem/14

## linux の ユーザー アカウント保持方法

* `/etc/passwd` `/etc/shadow` で保存している

__/etc/passwd__

* 他のユーザーから read 可能
* パスワードは /etc/shadow に暗号化して保存している
  * このファイルは 一般ユーザに読み込みの権限を与えないといけないので、パスワードを別管理にしている
* `:` で区切られている


名前             | 例         | 備考
-----------------|------------|---------
**ログイン名**  | root    |
**パスワード**  | x    | パスワードは保存されていない
**uid**       | 0    |
**gid**       | 0    |
**コメント**   | root    |
**ホームディレクトリ**  | /root    |
**ログイン時実行するコマンド**  | /bin/bash    |


__/etc/shadow__

* root だけ read 可能
* `:` で区切られている

名前             | 例         | 備考
-----------------|------------|-------
**ログイン名**  | test    |
**暗号化パスワード**  | $6$eIaYHAqm$y/.5CEj/m2RDrubIh...(省略)  |
**1970/1/1から最後にパスワードが変更された日までの日数**       | 15316    |
**パスワードが変更できるまでの日数**       | 0    |
**パスワードを変更しないといけなくなるまでの日数**   | 99999    |
**パスワードが有効な期限の前にユーザが警告を受ける日数**  | 7    |
**パスワードが無効になってからアカウントが使えなくなるまでの日数**  | 1   |
**1970/1/1からアカウントが使えなくなるまでの日数**  | 15318    |
**予約フィールド**  | /bin/bash    |


__暗号化されたパスワードの形式__

* `Hash方式 Salt $ Hash化されたパスワード` となっている
* Hash方式 は下記が存在する
  * $1$ MD5
  * $5$ SHA-256
  * $6$ SHA-512


## 解き方

* なんだこの文字列は? と思って色々検索する
* Hash 形式や フィールドの数 から `/etc/shadow` ファイルが表示されていると気づく
* `/etc/shadow` について学習
  * この問題は SHA-512 のhash方式を取っている
* `user99` のURLっぽいやつにアクセスしてみる
  * 辞書っぽい
* 下の順番で解いた

__辞書ファイルを hash化したら正解が見えてくるかも__

* user99 のURLの辞書一覧をテキストの保存して SHA-512 のhash に変換したら、どれかと一緒になるか検証
  * [辞書ファイル](./dictionaly.txt)
* salt値 : EACH
  * 問題の `/etc/shadow` から取得
* パスワード : ffl1bXDBqKUiD
  * [辞書ファイル](./dictionaly.txt) から取得
```
python -c "import crypt, getpass, pwd; print crypt.crypt('EACH','\$6\$ffl1bXDBqKUiD\$')"
```

***全然関係なさそう***

__辞書ファイルは辞書攻撃(Dictionary attack)だったのか__

* [辞書ファイル](./dictionaly.txt) から Hash値を生成して パスワードを作成したらパスワードが分かるはず
* php でやってみよう
  * [dictionaly_arrack.php](./dictionaly_arrack.php)

***なんかうまくいかない***

* python でやってみよう
  * [dictionaly_arrack.php](./dictionaly_arrack.php)

***なんかうまくいかない***

* mac OS の crypt は sha512 対応していないっぽい
* python2 の `hashlib.sha512(salt + word).hexdigest()` はダメっぽい
* python3 の `crypt.crypt()` でやってみよう

***出来た***

```
# 結果
vagrant@vagrant:~/src$ python dictionaly_attack.py
FREQUENT
LATTER
ADDITIONAL
GENDER
__________
applies
SPIRITS
independent
ultimate
JENNY
HELD
SUFFERS
LEAVE
floating
zecht
opinion
QUESTION
karaoke
strange
zero
DELIGHT
```

## まとめ

* linux はパスワードの保存を `/etc/passwd` `/etc/shadow` で保存している
* `/etc/shadow` に暗号化したパスワードが保存されている
* UNIX 系 OS では C言語の `crypt` という関数を使用して暗号化されている
  * [cryptのソース](https://svnweb.freebsd.org/base/head/lib/libcrypt/crypt.c?revision=4246&view=markup)
  * [cryptの説明](http://d.hatena.ne.jp/JULY/20110317)
