from talon import Module, Context, actions

mod = Module()

ctx = Context()
ctx.matches = r"""
app: neovim
and not tag: user.vim_mode_command
"""

ctx.tags = ["user.split"]


# https://dev.to/mr_destructive/vim-window-splits-p3p
@ctx.action_class("user")
class UserActions:
    # ----- split creation -----
    def split_move_up():
        pass

    def split_move_down():
        pass

    def split_move_left():
        pass

    def split_move_right():
        pass

    # ----- Split navigation -----
    # TODO: use vim_set_normal_exterm() instead of vim_set_normal() similar
    # to other below?
    def split_focus_up():
        actions.user.vim_run_normal("\\<c-w>k")

    def split_focus_down():
        actions.user.vim_run_normal("\\<c-w>j")

    def split_focus_left():
        actions.user.vim_run_normal("\\<c-w>h")

    def split_focus_right():
        actions.user.vim_run_normal("\\<c-w>l")

    def split_focus_next():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("w")

    def split_focus_last():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("W")

    def split_focus(number: int):
        actions.user.vim_set_normal_exterm()
        actions.insert(f"{number}")
        actions.key("ctrl-w ctrl-w")

    # ----- Split resize -----
    def split_shrink_width():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("<")
        # XXX - This should restore the original mode, as sometimes I use this from
        # terminal mode

    def split_shrink_height():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("-")
        # XXX - This should restore the original mode, as sometimes I use this from
        # terminal mode

    def split_expand_width():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key(">")
        # XXX - This should restore the original mode, as sometimes I use this from
        # terminal mode

    def split_expand_height():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("+")
        # XXX - This should restore the original mode, as sometimes I use this from
        # terminal mode

    # ----- Split layout -----
    def split_layout_toggle():
        pass

    def split_layout_join_two_groups():
        pass

    def split_layout_clear():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("o")

    # Requirement: https://github.com/dhruvasagar/vim-zoom
    def split_layout_toggle_maximize():
        actions.user.vim_run_normal_exterm_key("ctrl-w m")


@mod.action_class
class SplitActions:
    def split_move_next_tab():
        """Move the current window to the next tab"""
        actions.user.vim_run_command_exterm(":call MoveToNextTab()\n")

    def split_move_last_tab():
        """Move the current window to the previous tab"""
        actions.user.vim_run_command_exterm(":call MoveToPrevTab()\n")

    def split_move_new_tab():
        """Move the current window to a new tab"""
        actions.user.vim_run_normal_exterm_key("ctrl-w T")
