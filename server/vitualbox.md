# vitualbox
開発環境用のvitualboxを作成したので作成方法メモ

1. イメージ
debian の公式サイトでイメージダウンロード

2. sshできるようにする
```
root@debian:/home/user# cat /etc/hosts
# hp web
192.168.56.100    hp

root@debian:~# cat /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
#allow-hotplug enp0s3
auto enp0s3
iface enp0s3 inet dhcp

#web
#allow-hotplug enp0s8
auto enp0s8
iface enp0s8 inet static
  address 192.168.56.100
  gateway 192.168.56.1
  network 192.168.56.0
  netmask 255.255.255.0
  broadcast 192.168.56.255

root@debian:~# /etc/init.d/networking restart
```

3. debian準備
```
# sudo 追加
apt-get install sudo

visudo
user   ALL=(ALL)   ALL
user  ALL=NOPASSWD: ALL
```

4. 共有フォルダ設定
```
# VBoxGuestAdditions インストール
http://download.virtualbox.org/virtualbox/6.0.6/

# ディスクに追加して下記コマンド
user@debian:~$ ls -la /dev/cdrom
lrwxrwxrwx 1 root root 3  4月 24 00:47 /dev/cdrom -> sr0
user@debian:~$ sudo mount /dev/cdrom /media/cdrom
mount: /dev/sr0 is write-protected, mounting read-only
user@debian:~$ ls -la /media/
合計 12
drwxr-xr-x  3 root root 4096  4月 18 21:20 .
drwxr-xr-x 22 root root 4096  4月 23 23:52 ..
lrwxrwxrwx  1 root root    6  4月 18 21:20 cdrom -> cdrom0
drwxr-xr-x  2 root root 4096  4月 18 21:20 cdrom0
user@debian:~$ sudo /media/cdrom/VBoxLinuxAdditions.run

# kernelのヘッダーファイルがないのでビルドできないってことなので、インストールしてやれば解決。
sudo apt-get update
sudo apt-cache search linux-headers-$(uname -r)
sudo apt-get install linux-headers-$(uname -r)

sudo apt-get install gcc
sudo apt-get install make
sudo apt-get install perl

# VirtualBox Guest Additionsが失敗してる
VirtualBox Guest Additions: To build modules for other installed kernels, run
VirtualBox Guest Additions:   /sbin/rcvboxadd quicksetup <version>
VirtualBox Guest Additions: or
VirtualBox Guest Additions:   /sbin/rcvboxadd quicksetup all
VirtualBox Guest Additions: Kernel headers not found for target kernel
4.19.0-5-amd64. Please install them and execute
  /sbin/rcvboxadd setup
VirtualBox Guest Additions: Running kernel modules will not be replaced until
the system is restarted

# 4.19.0-5-amd64 を入れる
root@debian:~# apt-get install linux-image-4.19.0-5-amd64
/sbin/rcvboxadd quicksetup all
```

5. 権限が変えれないので手動マウント
```
umount web
mount -t vboxsf -o uid=0,gid=0,dmode=0777,fmode=777 web /media/sf_web

# シンボリックリンク
ln -s /media/sf_web/ web
```

6. apacheの設定
```
# confファイル作成
root@debian:/etc/apache2/sites-enabled# cd /etc/apache2/sites-available/
root@debian:/etc/apache2/sites-available# ll
合計 20
drwxr-xr-x 2 root root 4096  7月 28 18:20 .
drwxr-xr-x 8 root root 4096  7月 28 18:20 ..
-rw-r--r-- 1 root root 1332 11月  3  2018 000-default.conf
-rw-r--r-- 1 root root 6338 11月  3  2018 default-ssl.conf
root@debian:/etc/apache2/sites-available# cp 000-default.conf iy.conf

root@debian:/etc/apache2/sites-available# cat iy.conf
<VirtualHost *:8080>
        ServerName iy.com
        ServerAdmin webmaster@localhost
        DocumentRoot /home/user/web
        ErrorLog ${APACHE_LOG_DIR}/error.log
      	CustomLog ${APACHE_LOG_DIR}/access.log combined
        <Directory /home/user/web>
          Require all granted
        </Directory>
</VirtualHost>

root@debian:/etc/apache2/sites-enabled# ln -s ../sites-available/iy.conf iy.conf
root@debian:/etc/apache2/sites-enabled# ll
合計 8
drwxr-xr-x 2 root root 4096  7月 28 18:27 .
drwxr-xr-x 8 root root 4096  7月 28 18:20 ..
lrwxrwxrwx 1 root root   35  4月 21 15:46 000-default.conf -> ../sites-available/

root@debian:/etc/apache2# cat apache2.conf
# IncludeOptional sites-enabled/*.conf
IncludeOptional sites-enabled/iy.conf

DirectoryIndex index.html index.html.var index.php

root@debian:~# cat /etc/apache2/ports.conf
NameVirtualHost *:8080
Listen 8080

apt-get install libapache2-mod-rpaf
```

7. nginxの設定
```
root@debian:~# cat /etc/nginx/sites-enabled/iy
upstream web-apache {
  server localhost:8080;
}
server {
  listen       80;
  server_name  iy.com;

  location ~* .*\.(jpg|gif|png|css|js|html|) {
    root   /home/user/web/img;
    index  index.html index.html;
  }

  location / {
    proxy_pass http://web-apache/;
  }
}

root@debian:~# ll /etc/apache2/sites-enabled/iy.conf
lrwxrwxrwx 1 root root 26  7月 28 18:27 /etc/apache2/sites-enabled/iy.conf -> ../sites-available/iy.conf

root@debian:~# ll /etc/nginx/sites-enabled
lrwxrwxrwx 1 root root   29  7月 28 20:38 iy -> /etc/nginx/sites-available/iy
```
