from talon import Context, Module, actions, app, settings, ui

mod = Module()
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
"""

ctx.matches = r"""
app: neovim
"""


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
