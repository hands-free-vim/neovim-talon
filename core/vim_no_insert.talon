app: neovim
# tag: user.vim_mode_command
# tag: user.vim_mode_normal
# tag: user.vim_mode_normal_terminal
# TODO: commenting above for now as this is also needed in insert mode as otherwise we can't dictate things properly
-

# insert() will never use paste(). This is needed in lots of modes like command/normal/normal terminal to be
# able to insert text without triggering the paste from clipboard
tag(): user.insert_paste_disabled
