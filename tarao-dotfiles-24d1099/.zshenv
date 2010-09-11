ZDOTDIR=~/.zsh

if [ "`id -u`" -eq 0 ]; then
  PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
else
  PATH="/usr/local/bin:/usr/bin:/bin:/usr/games"
fi
export PATH=$HOME/bin:$PATH

umask 022
unsetopt nomatch

function xsel() {
    [[ -n "$DISPLAY" ]] && env xsel $@
}
