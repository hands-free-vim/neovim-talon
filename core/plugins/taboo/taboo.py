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
    def tab_rename(name: str = ""):
        actions.user.vim_run_command_exterm(f":TabooRename {name}")

    def tab_open_with_name(name: str = ""):
        actions.user.vim_run_command_exterm(f":TabooOpen {name}")

    def tab_name_reset():
        actions.user.vim_run_command_exterm(":TabooReset")


# FIXME: TEMPORARY: Once https://github.com/talonhub/community/pull/1446 is merged, this should be removed
@mod.action_class
class Actions:
    def tab_rename(name: str = ""):
        """Renames the current tab"""

    def tab_open_with_name(name: str = ""):
        """Opens a new tab and rename it"""

    def tab_name_reset():
        """Resets the name of the current tab"""
