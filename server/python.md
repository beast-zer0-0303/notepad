# python

## 環境構築

```
# pyenv install 方法
$ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

# ~/.bash_profile に追加する
export PATH="/Users/ishii-no/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

$ pyenv install --list
$ pyenv install 3.6.0
$ virtualenv -p /Users/ishii-no/.pyenv/shims/python3.6 --no-site-packages python3.6

# 環境に入る
$ . [環境名]/bin/activate

# 環境から出る
$ deactivate
```
