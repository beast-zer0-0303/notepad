# John

* https://ksnctf.sweetduet.info/problem/6

## linux の ユーザー アカウント保持方法

```
/etc/passed
他のユーザーから read 可能
パスワードは /etc/shadow に暗号化して保存している
```

ログイン名
パスワード
uid
gid
コメント
ホームディレクトリ
ログイン時実行するコマンド


/etc/shadow
root だけ read 可能

ユーザ名（ログイン名）
暗号化されたパスワード
パスワードの最終変更日
変更可能最短期間（この期間を越えないと変更不可）
未変更可能最長期間（この期間を越えたら変更必要）
警告日（上記期日の何日前に警告するか）
インアクティブ（ログインしないと無効になる日数）
失効日（アカウント失効までの日数）
フラグ（未使用）


暗号化されたパスワードの形式
Hash方式 Salt $ Hash化されたパスワード

Hash方式
$1$ MD5
$5$ SHA-256
$6$ SHA-512

SHA-512 のhash方式を取っている

http://ksnctf.sweetduet.info/q/14/dicti0nary_8Th64ikELWEsZFrf.txt
を SHA-512 のhash に変換したら、どれかと一緒になるかと思ったけど ならなかった


python -c 'import crypt, random, hashlib; random.seed(); print crypt.crypt("PASSWORD", "$6$" + hashlib.sha1(str(random.random())).hexdigest())';


python -c "
import crypt, getpass, pwd;
print crypt.crypt('test','\$6\$SALTsalt\$')"





php -r 'echo crypt("PASSWORD","$6$".hash("sha512", uniqid(mt_rand(),true))), PHP_EOL;'

hash( 'SHA256', 'pass'.'salt' );

$ php -r 'echo crypt("PASSWORD","$6$".sha1(uniqid(mt_rand(),true))), PHP_EOL;'

# sha512 版
$ php -r 'echo crypt("PASSWORD","$6$".hash("sha512", uniqid(mt_rand(),true))), PHP_EOL;'

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

FLAG_aSiuJHSLfzoQkszD
aSiuJHSLfzoQkszD

http://docs.python.jp/2/library/crypt.html
このモジュールは修正 DES アルゴリズムに基づいた一方向ハッシュ関数である crypt(3) ルーチンを実装しています

http://docs.python.jp/2/library/hashlib.html
このモジュールは、セキュアハッシュやメッセージダイジェスト用のさまざまなアルゴリズムを実装したものです。FIPSのセキュアなハッシュアルゴリズムである SHA1、SHA224、SHA256、SHA384およびSHA512 (FIPS 180-2 で定義されているもの) だけでなくRSAのMD5アルゴリズム (Internet RFC 1321 で定義されています)も実装しています

上述のcryptは、linuxのshadow passwordの作成と同じ方式。

Congratulation! Flag FLAG_aSiuJHSLfzoQkszD is correct.


--wordlist=~/src/dictionaly.txt
