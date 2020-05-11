# vm

## 設定

```
#network アダプター１
NAT
#network アダプター2
ホストオンリーアダプタ

#ホストドメイン
localdomain

#アカウント
root:root
```

## ゲストマシン　コマンド

```
apt-get update
apt-get install openssh-server

apt-get install nginx
apt-get install apache2
apt-get install lsb-release
apt-get install apt-transport-https
apt-get install wget
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list
apt-get update
apt-get install php7.0

apt-get install mysql-server
apt-get install mysql-client

sudo apt-cache search php-zip
sudo apt-get install unzip
```
