# https://github.com/gcmt/taboo.vim
from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = r"""
user.neovim_plugin: taboo
and not tag: user.vim_mode_command
"""


@ctx.action_class("user")
class TabActions:
    def tab_rename(name: str):
        actions.user.vim_run_normal_exterm(f":TabooRename {name}")

    def tab_new_named(name: str = ""):
        actions.user.vim_run_command_exterm(f":TabooOpen {name}")

    def tab_reset():
        actions.user.vim_run_command_exterm(":TabooReset")
