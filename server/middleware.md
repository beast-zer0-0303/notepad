# middleware

## git

### コミットメッセージで変更ファイルのみ grep

```
# = の後が正規表現  --all-match オプションでgrep が and デフォルトは or
git log --grep="[grep文字列]" --name-only | grep -v -E "commit|Author|Date|^\ |^$" | sort -n | uniq > ./test.txt
```

### ファイル差分で ファイル一覧取得

```
git diff --name-only master..feature > ./test.txt
```

### stash

https://qiita.com/akasakas/items/768c0b563b96f8a9be9d

## mysql

### ログ周り
```
SHOW VARIABLES LIKE "general_log%"
SET GLOBAL general_log = 'OFF';

SHOW GLOBAL VARIABLES LIKE '%log_queries_not_using_indexes%';
SHOW GLOBAL VARIABLES LIKE '%long_query_time%';
SET GLOBAL log_queries_not_using_indexes = 'ON';
SET GLOBAL long_query_time = 1.000000;
```

### dump オプション

```
ionice -c2 -n7 mysqldump \
  -u hoge -h localhost -p -P 3311 -C \
  --add-drop-table=false \
  --no-create-info \
  --hex-blob \
  --default-character-set=utf8 \
  --skip-tz-utc \
  --extended-insert \
  --quick \
  --where="data1 like '%hogehoge%'" \
  database table > ./test.sql
```

```
mysqldump \
  -u hoge -p hoge -h localhost \
  --default-character-set=utf8 \
  --single-transaction \
  --skip-lock-tables \
  --extended-insert \
  --quick \
  database table > ./test.sql
```

### 管理系
```
# ユーザー一覧
select Host, User, Password from mysql.user;

# ユーザー追加
GRANT ALL PRIVILEGES ON *.* TO username IDENTIFIED BY '*****' WITH GRANT OPTION;

# ホスト変更
update mysql.user set host='hostname2' where User='hostname1';
```

### その他
```
# Blob 内検索用クエリ

SELECT player_id, MAX(damage)
FROM
    (SELECT *
     FROM
         (SELECT t2.player_id, t2.data2
              , CAST(SUBSTRING(CAST(t2.data2 AS CHAR), (t2.START_POS + 9), (t2.END_POS - t2.START_POS - 9)) AS SIGNED) AS damage
          FROM
             (SELECT LOCATE(",", CAST(t1.data2 AS CHAR), t1.START_POS) AS END_POS
                   , t1.START_POS, t1.player_id, t1.data2
              FROM
                 (SELECT *, LOCATE("\"damage\":", CAST(data2 AS CHAR)) AS START_POS
                  FROM test.raid_boss_players_log
                 ) t1
              WHERE t1.START_POS > 0
             ) t2
         ) t3
     WHERE t3.damage >= 100000000
    ) t4
GROUP BY player_id
ORDER BY player_id;
```

```
# コマンドから csv
/usr/local/mysql/bin/mysql -h localhost -u root -p usename \
  -e "SELECT player_id, next_num FROM player_bingo" | \
  awk '{gsub("\"","\\\""); $0="\""$0"\""; gsub("\t", "\",\""); print $0}' \
  > './test.csv'
```

```
# テーブル作り直し
mysqldump -d -u root -P 3311 -p database | sed -e 's/AUTO_INCREMENT=[0-9]*//' > ./insert.sql
cat insert.sql | mysql -d -u root -P 3311 -p database
```

## ワイヤーシャーク

```
# 端末の UUID を取得 例 xxxxxxxxxxxx
rvictl -s xxxxxxxxxxxx
```

```
# rvi0 このポートが開いているのを確認
ifconfig -l
lo0 gif0 stf0 en0 en1 en2 p2p0 awdl0 bridge0 vboxnet0 vboxnet1 rvi0

# ワイヤーシャーク の方にも追加されている
rvi0 をダブルクリック
rvictl -x xxxxxxxxxxxx
```
