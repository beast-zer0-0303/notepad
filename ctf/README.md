# ctf

## 目次

* [Hackme](./Hackme/)
* [ksnctf](./ksnctf/)

## 環境構築

### gdb-peda 導入

```
■使用するOS(※絶対にこれ使ってください)
- Ubuntu14.04 x86_64


■環境セットアップ
x64環境でx86バイナリを動かすパッケージ
$ dpkg --add-architecture i386
$ apt-get update
$ apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386
$ apt-get install gcc-multilib g++-multilib

ELF解析用
$ apt-get install binutils

Python，perl
$ apt-get install python2.7 perl

ROPガジェット探索用
$ wget https://github.com/downloads/0vercl0k/rp/rp-lin-x86
$ chmod +x rp-lin-x86; mv rp-lin-x86 /usr/local/bin

その他
$ apt-get install binutils python2.7 perl socat git build-essential gdb gdbserver nasm

gdb-peda導入
$ git clone https://github.com/longld/peda.git ~/peda
$ echo "source ~/peda/peda.py" >> ~/.gdbinit

gdbを起動して "gdb-peda$" というプロンプトが出ていればインストール完了です．
```
