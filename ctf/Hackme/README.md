# Hackme

* http://hackme.netfire.jp/start
  * beast_zer0_0303
  * `tr******`

## Lv1

* curl -L http://hackme.netfire.jp/Lv1/
  * curl で user 情報 を送信すれば webページが見れる
* curl -H
* Chrome 使っているので、メニューからソースを表示されてみたら、パスワードあった

## Lv2

* password に `'` を入れたらエラーになる
  * `Warning: pg_query() [function.pg-query]: Query failed: ERROR: syntax error at or near "'"`
* SQL インジェクション

たぶんこんなプログラム
```
$password = $_REQUEST['password'];
$result   = pg_query($conn, "select * from password where password = '{password}'");
```

* 不正解
  * `' or 1 = '1`
  * `' or 1 = '1 --`
* 正解
  * `' or 1 = 1--;`

## Lv3

* http://hackme.netfire.jp/Lv3/login にアクセスしたら
  * `cannot access : No such file or directory.` になる
