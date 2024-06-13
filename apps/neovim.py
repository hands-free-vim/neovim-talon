from talon import Context, Module, actions, app, settings, ui


mod = Module()

windows_shortcut = "ctrl-shift-f12"
linux_and_mac_shortcut = "ctrl-`"
default_shortcut = windows_shortcut if app.platform == "windows" else linux_and_mac_shortcut
mod.setting(
    "neovim_command_server_shortcut",
    type=str,
    default=default_shortcut,
    desc="The keyboard shortcut to trigger RPC interaction with the command server",
)
ctx = Context()

# Relies on using talon.nvim
mod.apps.neovim = """
win.title: /VIM MODE/
and win.title: /nvim/
"""

# e.g. nvim.exe 0.9.5 on Windows
mod.apps.neovim = """
app.exe: conhost.exe
and win.title: /VIM MODE/

app.exe: conhost.exe
and win.title: /Neovim/

app.exe: conhost.exe
and win.title: /nvim.exe/
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
        shortcut = settings.get("user.neovim_command_server_shortcut")
        actions.key(shortcut)


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
