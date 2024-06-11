app: neovim
tag: user.tabs
-
# TEMPORARY: Once https://github.com/talonhub/community/pull/1446 is merged, these should be removed
tab rename [<user.text>]: user.tab_rename_wrapper(text or "")
tab flip: user.tab_focus_most_recent()
tab move left: user.tab_move_left()
tab move right: user.tab_move_right()
