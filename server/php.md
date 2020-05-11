# php

## 環境構築

```
# phpbrew install
cd /usr/local/bin/
curl -L -O https://github.com/phpbrew/phpbrew/raw/master/phpbrew
sudo chmod +x phpbrew
phpbrew init

# .bashrc に下記を追加
if [[ -f $HOME/.phpbrew/bashrc ]]; then
  source $HOME/.phpbrew/bashrc
  phpbrew switch php-5.4.45
fi
# brew docktor がWaning 出るので対応
alias brew="env PATH=${PATH/${HOME}\/\.phpbrew\/php\/php-5.4.45\/bin:/} brew"
```

```
# php 5.4系を install
brew install automake autoconf curl pcre bison re2c mhash libtool icu4c gettext jpeg openssl libxml2 mcrypt gmp libevent
brew link curl --force
brew link icu4c --force
brew link libxml2 --force
brew link openssl --force

phpbrew install 5.4.0 +default +mysql +fpm +opcache +intl +iconv
phpbrew switch php-5.4.45

# redis install
phpbrew ext install redis 2.2.7

# xdebug install
phpbrew ext install xdebug 2.4.0

# timezone の設定追加
vi /Users/jenkins/.phpbrew/php/php-5.4.45/etc/php.ini
date.timezone = Asia/Tokyo

# メモリ上限変更
vi /Users/jenkins/.phpbrew/php/php-5.4.45/etc/php.ini
memory_limit = 1024M #に変更
```

```
# 特定バージョンのphpunit インストール
curl -L -O https://phar.phpunit.de/phpunit-4.8.21.phar
chmod +x phpunit-4.8.21.phar
sudo mv phpunit-4.8.21.phar /usr/local/bin/phpunit

# バージョンの指定はないはずなので、最新をインストール
brew install homebrew/php/phploc
brew install homebrew/php/phpcpd

# phpcb インストール
curl -L -O https://github.com/mayflower/PHP_CodeBrowser/releases/download/1.1.1/phpcb-1.1.1.phar
mv phpcb-1.1.1.phar /usr/local/bin/phpcb
chmod a+x /usr/local/bin/phpcb

# pdepend インストール
pear channel-discover pear.pdepend.org
pear install pear.pdepend.org/PHP_Depend

# phpmd インストール
pear channel-discover pear.phpmd.org
pear install phpmd/PHP_PMD

# apigen インストール
curl -L -O http://apigen.org/apigen.phar
chmod +x apigen.phar
mv apigen.phar /usr/local/bin/apigen

# vfsStream インストール
pear channel-discover pear.bovigo.org
pear install bovigo/vfsStream-beta
```

## 設定

```
# 拡張モジュール確認
php -m

# 設定確認
php -i

# 設定ファイル確認
php --ini

# 拡張モジュールディレクトリ確認
php -i | grep -i extension_dir

# インストールされている php version
phpbrew list

# インストール出来るバージョン一覧
phpbrew known

# インストール
phpbrew install 5.6.22 +default

# 一時的に使用するphpのバージョンの指定
phpbrew use [バージョン]

# デフォルトで使用するphpのバージョンの指定
phpbrew switch [バージョン]
```


## 環境構築

### composer install

```
curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/local/bin/composer

# 確認
composer
```

```
(プロジェクトルート)/
  ├ composer.json
  ├ composer.lock  
  └ vendor/

# install and update
composer update
```

### laravel 環境構築

```
＃ laravel install
composer global require laravel/installer

# Laravelアプリを新規作成する
laravel new basic-crud
```

##cake PHP
```
composer create-project --prefer-dist app iy
```

```
# composer がうまくいかなかった時
composer update -vvv
```
