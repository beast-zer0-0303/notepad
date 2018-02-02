# vim

以前作成した `vimrc` を記載する。あとで綺麗にする

```
"---------------------------
" Start Neobundle Settings.
"---------------------------
" bundleで管理するディレクトリを指定
set runtimepath+=~/.vim/bundle/neobundle.vim/

" Required:
call neobundle#begin(expand('~/.vim/bundle/'))

" neobundle自体をneobundleで管理
NeoBundleFetch 'Shougo/neobundle.vim'

NeoBundle 'Shougo/unite.vim'
NeoBundle 'Shougo/vimfiler'

call neobundle#end()

" Required:
"filetype plugin indent on

" 未インストールのプラグインがある場合、インストールするかどうかを尋ねてくれるようにする設定
" 毎回聞かれると邪魔な場合もあるので、この設定は任意です。
NeoBundleCheck

"-------------------------
" End Neobundle Settings.
"-------------------------

" Configuration file for vim
"set modelines=0		" CVE-2007-2438

" Normally we use vim-extensions. If you want true vi-compatibility
" remove change the following statements
"set nocompatible	" Use Vim defaults instead of 100% vi compatibility
"set backspace=2		" more powerful backspacing

" Don't write backup file if vim is being called by "crontab -e"
"au BufWrite /private/tmp/crontab.* set nowritebackup nobackup
" Don't write backup file if vim is being called by "chpass"
"au BufWrite /private/etc/pw.* set nowritebackup nobackup

" -----------------------------
" default 設定追加
" -----------------------------
"行番号の表示
set number
"新しい行のインデントを現在行と同じにする
" set autoindent
"タブ文字、行末など不可視文字を表示
set list
"シフト移動幅
set shiftwidth=4
"行頭の余白内でTabを打ち込むと、'shiftwidth'の数だけインデントする
"set smartindent
" カーソル行の背景色を変える
"set cursorline
" カーソル位置のカラムの背景色を変える
"set cursorcolumn
" 対応する括弧を強調表示
set showmatch
"外部でファイルに変更がされた場合は読みなおす
set autoread
"クリップボードをWindowsと連携
" TODO 出来ないので対応する
" set clipboard=unnamed
"入力モード時、ステータスラインのカラーを変更
augroup InsertHook
" -----------------------------
" キーバインド
" -----------------------------
" Vimfiler を 起動$
nnoremap <Space><Space> :VimFiler -split -simple -winwidth=35 -no-quit<CR>$
"タブコマンドに別のキーバインドを割り当てる$
map  <C-b> :tabnext<CR>$
map  <C-p> :tabprevious<CR>$
map  :e :tabnew$
map <C-w> <C-w><C-w>$
"nomalモードでOで空行追加$
nnoremap O :<C-u>call append(expand('.'), '')<Cr>j
```
