app: neovim
tag: user.tabs
-

# requires: https://github.com/gcmt/taboo.vim/
tab rename [<user.text>]:   user.tab_rename(text or "")
tab new named [<user.text>]: user.tab_new_named(text or "")
tab reset:                  user.tab_reset()
