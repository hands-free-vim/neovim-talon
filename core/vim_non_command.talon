app: neovim
and not tag: user.vim_mode_command
-

# Terminal mode
go term:
    user.vim_set_terminal()
new term:
    user.vim_run_normal_exterm(":term\n")
