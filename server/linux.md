# linux

## 設定等

### 起動時設定 確認コマンド
```
sysv-rc-conf
```

### 起動時に実行される処理
```
/etc/inittab
```

### 起動時の設定変更
```
# 永続的に変更する場合
/etc/sysctl.conf  に記述

# 一時的な変更
sysv-rc-conf コマンドを使用

# ランレベルに合わせた変更
# 例 update-rc.d -f httpd-y2hgr-mv defaults
/etc/sysctl.conf

chkconfigコマンドを使う
update-rc.d -f mysql defaults
```

### rcスクリプト
```
ランレベルごとに起動時に執行される
/etc/rc.local　にスクリプトを書くと起動時に実行される
```

### 環境設定
```
# このフォルダ以下のファイルは起動時に全て読み込まれるので、ここに定義
# .bashrc も読み込むので.bashrcでもいい
/etc/profile.d/*

# 保管機能拡張
/etc/bash_completion
```

### 各種設定ファイル
```
# 使用しているポートの設定ファイル
/etc/services

# 各ホストのホスト名とIPアドレスの対応
/etc/hosts
```

## コマンド

### locate
```
# ファイル名で検索 正規表現を使用
locate -r ".sock"
```

### strace
```
# プロセスを標準出力に表示する
strace -f -p 1220 -tt -s 256 2>&1 | grep "\.rb"
strace -f -p 474476 -e write -tt -s 1024 2>&1

# こんなオプションがいいかもしれない
strace -fi
```

### ネットワーク周り
```
# ポート指定プロセスを調べる
lsof -i:[ポート番号]

# 環境変数を調べる
printenv

# ドメイン情報をDNSサーバーから取得する
dig www.yahoo.co.jp

# ネットワーク関連の統計情報を表示する
netstat

# ルーティングテーブルの表示／設定を行う
route

# ホストまでの経路を調べる
traceroute yahoo.co.jp

# DNS サーバーの応答性を確認
nslookup

# io の負荷を確認する場合はiowaitじゃなくて iostat を使う
iostat
```

### xargs
```
grep -E "cd[0-9]{7}" ./a.txt | awk '{print $1}' | grep -E "cd[0-9]{7}" \
  | xargs -I% echo "{:kind => 'card', :item_id => '"%"', :qty => 2},"
```

### awk
```
# オプション
-F 区切り文字指定
# スペース区切りで 1番目を出力
例 awk -F " " '{ print $1}'
```

```
# 500件数
zcat httpd_access.log.gz | awk -F " " '{ if ($10 ~ /^500$/) print }' | wc -l
```

```
# 集計
awk '{
    if ( $14 in status ) {
        status[$14] += 1;
    } else {
        status[$14] = 1;
    }
}
END {
    for (i in status) { print i, "\t", status[i] }
}'

awk '{
    sub(/[0-9]{6}/,"",$2);
    acc_time[$3, "\t", $12, "\t", $14]+=1;
} END {
    for (i in acc_time) { print i, "\t", acc_time[i] }
}' | tr "," "\t" | sort -n -r -t$'\t' -k4 | head -n 1000
```

### tr
```
# カンマをタブに置換する
cat CSVファイル名 | tr "," "\t"

# タブ区切り 第4フィールド 降順ソート
sort -n -r -t$'\t' -k4
```


### ユーザーごとのプロセス確認
```
ps -f -U username -u username --forest
```

### oom-killer
```
# ログ確認
/var/log/kern.log
grep 'oom-killer' /var/log/kern.log
```

## mysql 起動しなくなった

```
# アンインストール
sudo apt-get remove --purge mysql-server*
mysql-common
sudo apt-get autoremove --purge
sudo rm -r /etc/mysql
sudo rm -r /var/lib/mysql
```

```
$ sudo apt-get update
$ sudo apt-get install mysql-server
$ mysql_secure_installation
```

```
$ sudo apt-get install aptitude
$ sudo aptitude update
$ sudo aptitude safe-upgrade

$ sudo aptitude install mysql-server
```

## myswql パスワード設定
```
use mysql
UPDATE user SET authentication_string=password('root') WHERE user='root';
flush privileges;
```

## 文字コード確認
```
nkf --guess　ファイル名
file -i　ファイル名
```

```
mysql> SET character_set_server=utf8;
Query OK, 0 rows affected (0.00 sec)

mysql> SET character_set_database=utf8;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> show variables like '%char%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | utf8                       |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | utf8                       |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.00 sec)
```
