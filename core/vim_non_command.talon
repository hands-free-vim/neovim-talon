app: neovim
and not tag: user.vim_mode_command
-

# insert() will never use paste(). This is needed in lots of places to be
# able to insert text without triggering the paste from clipboard
tag(): user.insert_paste_disabled

# Terminal mode
go term:
    user.vim_set_terminal()
new term:
    user.vim_run_normal_exterm(":term\n")
