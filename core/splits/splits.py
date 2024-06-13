from talon import Module, Context, actions

mod = Module()

ctx = Context()
ctx.matches = r"""
app: neovim
and not tag: user.vim_mode_command
"""

ctx.tags = ["user.splits"]


# https://dev.to/mr_destructive/vim-window-splits-p3p
@ctx.action_class("user")
class UserActions:
    # ----- split creation -----
    def split_window_vertically():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("v")

    def split_window_horizontally():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("s")

    # ----- split arrangement ----
    def split_move_up():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("K")

    def split_move_down():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("J")

    def split_move_left():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("H")

    def split_move_right():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("L")

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

    def split_focus_number(index: int):
        actions.user.vim_set_normal_exterm()
        actions.insert(f"{index}")
        actions.key("ctrl-w ctrl-w")

    # FIXME: This name is subject to change pending  https://github.com/talonhub/community/pull/1446 decisions
    def split_focus_most_recent():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("p")

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
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("r")

    def split_clear():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("q")

    def split_clear_all():
        actions.user.vim_set_normal_exterm()
        actions.key("ctrl-w")
        actions.key("o")

    # Requirement: https://github.com/dhruvasagar/vim-zoom
    def split_maximize():
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

    # TEMPORARY: Once https://github.com/talonhub/community/pull/1446 is merged, this should be removed
    def split_focus_right():
        """Focus on the split to the right of the current window"""

    def split_focus_left():
        """Focus on the split to the left of the current window"""

    def split_focus_down():
        """Focus on the split below the current window"""

    def split_focus_up():
        """Focus on the split above the current window"""

    def split_focus_next():
        """Goes to next split"""

    def split_focus_last():
        """Goes to last split"""

    def split_focus_number(index: int):
        """Navigates to the specified split"""

    def split_focus_most_recent():
        """Focus on the most recently focused split"""

    # Arrangement
    def split_move_right():
        """Move the split to the right"""

    def split_move_left():
        """Move the split to the left"""

    def split_move_down():
        """Move the split down"""

    def split_move_up():
        """Move the split up"""

    def split_layout_toggle():
        """Flips the orientation of the active split"""

    def split_center():
        """Centers the active split (eg: zen mode)"""

    def split_rotate_right():
        """Rotates the splits to the right"""

    def split_rotate_left():
        """Rotates the splits to the left"""

    # Resizing
    def split_maximize():
        """Maximizes the active split"""

    def split_reset():
        """Resets all the split sizes"""

    def split_expand_width():
        """Expands the split width"""

    def split_expand_height():
        """Expands the split height"""

    def split_shrink_width():
        """Shrinks the split width"""

    def split_shrink_height():
        """Shrinks the split height"""

    def split_set_width(width: int):
        """Sets the split width"""

    def split_set_height(height: int):
        """Sets the split height"""
