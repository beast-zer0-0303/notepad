# mac

## bash

```
# ~/.bash_profile
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

```
# ~/.bashrc
# default
alias ll='ls -la'
alias lock='/System/Library/Frameworks/ScreenSaver.framework/Resources/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine'

# git 補完
source '/Applications/Xcode.app/Contents/Developer/usr/share/git-core/git-completion.bash'
source '/Applications/Xcode.app/Contents/Developer/usr/share/git-core/git-prompt.sh'
export GIT_PS1_SHOWDIRTYSTATE=1

# コマンドライン表示変更
PS1="\[\033[36m\]\u@local:\[\033[0m\]\[\033[36m\] \w\[\033[0m\] \n$ "
```

## コマンド
```
# クリップボード コピ
$ echo hoge | pbcopy

# クリップボード出力
$ pbpaste > ./test.txt
```

## brew

* brew 公式 http://brew.sh/
* cask ghe https://github.com/caskroom/homebrew-cask

### コマンド

```
# パッケージ検索
$ brew search <パッケージ名>

# パッケージインストール・アンインストール
$ brew install <パッケージ名>
$ brew uninstall <パッケージ名>

# パッケージの有効化・無効化
$ brew link <パッケージ名>
$ brew unlink <パッケージ名>

# パッケージされたリストの表示
$ brew list

# デッドリンクになっているものを削除
$ brew prune

# インストールの問題をチェック
$ brew doctor

# brewの設定確認
$ brew --config
```

### install list

```
# brew
brew install curl
brew install nkf
brew install bzip2
brew install go
brew install tmux
brew install mysql

# cask
brew cask install atom
brew cask install google-chrome
brew cask install alfred
brew cask install sourcetree
brew cask install virtualbox
brew cask install virtualbox-extension-pack
brew cask install go
brew cask install macvim
brew cask install dockertoolbox
brew cask install firefox-ja
```
