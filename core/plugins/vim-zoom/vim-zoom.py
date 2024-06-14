# https://github.com/dhruvasagar/vim-zoom

from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = r"""
user.neovim_plugin: vim-zoom
and not tag: user.vim_mode_command
"""


@ctx.action_class("user")
class SplitActions:
    def split_toggle_maximize():
        actions.user.vim_run_normal("\\<c-w>m")
