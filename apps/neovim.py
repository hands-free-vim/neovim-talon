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

# Neovim (commandline version) and nvim-qt.exe (GUI version)
mod.apps.neovim = """
os: windows
and win.title: /Neovim/
and app.exe: nvim.exe

os: windows
and win.title: /VIM MODE/
and app.exe: nvim.exe

os: windows
and win.title: /VIM MODE/
and app.exe: conhost.exe

os: windows
and win.title: /Neovim/
and app.exe: conhost.exe

os: windows
and app.exe: nvim-qt.exe

os: linux
and win.title: /VIM MODE/
and win.title: /nvim/
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
