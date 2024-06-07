from talon import Context, Module, actions, app, settings, ui

mod = Module()
ctx = Context()

# Relies on using talon.nvim
mod.apps.neovim = """
win.title: /VIM MODE/
and win.title: /nvim/
"""

# e.g. nvim.exe 0.9.5 on Windows
mod.apps.neovim = """
win.title: /VIM MODE/
win.title: /Neovim/
win.title: /nvim.exe/
and app.exe: conhost.exe
"""

ctx.matches = r"""
app: neovim
"""


ctx.tags = ["user.command_client"]


@ctx.action_class("user")
class CommandClientActions:
    def command_server_directory() -> str:
        return "neovim-command-server"

    def trigger_command_server_command_execution():
        actions.key("ctrl-shift-f12")


# Based on you using a custom titlestring see doc/vim.md
@ctx.action_class("win")
class win_actions:
    def filename():
        title = actions.win.title()
        result = title.split(")")
        if len(result) > 1:
            # Assumes the last word after the last ) entry has the filename
            result = result[-1]
            # print(f"vim.filename(): {result.strip()}")
            return result.strip()
        else:
            return ""
