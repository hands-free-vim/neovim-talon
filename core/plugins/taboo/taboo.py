from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = r"""
app: neovim
and not tag: user.vim_mode_command
and user.neovim_plugin: taboo
"""


@ctx.action_class("user")
class TabActions:
    def tab_rename(name: str):
        # Requires the Taboo plugin
        actions.user.vim_run_normal_exterm(f":TabooRename {name}")
