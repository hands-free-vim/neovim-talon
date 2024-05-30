from talon import Context, Module, actions

# TODO: should we also match tag: user.tabs or tabs are always present anyway so does not matter?
mod = Module()
ctx = Context()
ctx.matches = r"""
app: neovim
and not tag: user.vim_mode_command
"""

ctx.tags = ["user.tabs"]


# https://vim.fandom.com/wiki/Using_tab_pages
# https://vim.fandom.com/wiki/Move_current_window_between_tabs
@ctx.action_class("app")
class AppActions:
    def tab_previous():
        actions.user.vim_run_command_exterm(":tabprevious\n")

    def tab_next():
        actions.user.vim_run_command_exterm(":tabnext\n")

    def tab_open():
        actions.user.vim_run_command_exterm(":tabnew\n")

    def tab_close():
        actions.user.vim_run_command_exterm(":tabclose\n")

    # def tab_reopen():


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        actions.user.vim_run_normal_exterm(f"{number}gt\n")

    # def tab_jump_from_back(number: int):

    def tab_final():
        actions.user.vim_run_command_exterm(":tablast\n")

    def tab_move_left():
        actions.user.vim_run_command_exterm(":tabmove -\n")

    def tab_move_right():
        actions.user.vim_run_command_exterm(":tabmove +\n")

    # def tab_duplicate():

    # def tab_back():

    def tab_focus_most_recent():
        actions.user.vim_normal_mode_exterm("g\t")

    def tab_rename():
        # Requires the Taboo plugin
        actions.user.vim_normal_mode_exterm(":TabooRename ")


@mod.action_class
class TabActions:
    def tab_rename():
        """Renames the current tab."""

    def tab_focus_most_recent():
        """Jumps to the most recently viewed tab."""

    def tab_move_left():
        """Moves the current tab to the left."""

    def tab_move_right():
        """Moves the current tab to the right."""
