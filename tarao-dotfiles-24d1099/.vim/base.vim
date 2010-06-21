syntax on
set nocompatible
set ignorecase
set smartcase
set hlsearch
set tabstop=4
set expandtab
set autoindent
set backspace=2
set ruler
set whichwrap=b,s,h,l,<,>,[,]
set list
set lcs=tab:>\ ,trail:_,precedes:<,extends:\
set laststatus=2
set showcmd
set statusline=%<%f\ %m%r%h%w%{'['.(&fenc!=''?&fenc:&enc).']['.&ff.']'}%=%l,%c%V%8P
set foldlevelstart=99
set viminfo='50,<50,s10,h,n~/.vim/info
set encoding=utf-8
set fileencodings=ucs-bom,euc-jp,sjis,cp932,utf-8

if $TERM == 'xterm-256color'
    set t_Co=256
    colorscheme railscasts
endif

noremap ; :
noremap j gj
noremap k gk
noremap J <C-d>
noremap K <C-u>
