192.168.56.100

ssh user@192.168.56.100
su root

shutdown -h now
reboot

sudo tail -f  /var/log/apache2/access.log

sudo tail -f /var/log/nginx/access.log

root@debian:~# sh /etc/init.d/apache2 stop
[ ok ] Stopping apache2 (via systemctl): apache2.service.
root@debian:~# sh /etc/init.d/apache2 start
[ ok ] Starting apache2 (via systemctl): apache2.service.

user@debian:~$ sudo /etc/init.d/nginx start
[ ok ] Starting nginx (via systemctl): nginx.service.
