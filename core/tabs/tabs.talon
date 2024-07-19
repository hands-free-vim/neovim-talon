app: neovim
tag: user.tabs
-

# FIXME: TEMPORARY: Once https://github.com/talonhub/community/pull/1446 is merged, this should be removed
# requires: https://github.com/gcmt/taboo.vim/
tab (open | new) named [<user.text>]: user.tab_open_with_name(text or "")
tab rename [<user.text>]: user.tab_rename(text or "")
tab [name] reset: user.tab_name_reset()
