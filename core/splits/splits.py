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
    def split_create():
        actions.user.split_window_horizontally()

    def split_window_vertically():
        actions.user.vim_run_normal("\\<c-w>v")

    def split_window_horizontally():
        actions.user.vim_run_normal("\\<c-w>s")

    # ----- split arrangement ----
    def split_move_up():
        actions.user.vim_run_normal("\\<c-w>K")

    def split_move_down():
        actions.user.vim_run_normal("\\<c-w>J")

    def split_move_left():
        actions.user.vim_run_normal("\\<c-w>H")

    def split_move_right():
        actions.user.vim_run_normal("\\<c-w>L")

    # FIXME: These require talon.nvim, so could be moved to plugins/ since for now talon.nvim isn't hard
    # required.
    def split_move_next_tab():
        actions.user.vim_run_command_exterm(":lua vim.cmd.MoveSplitToNextTab()\n")

    def split_move_previous_tab():
        actions.user.vim_run_command_exterm(":lua vim.cmd.MoveSplitToPreviousTab()\n")

    def split_move_new_tab():
        actions.user.vim_run_normal("\\<c-w>T")

    # ----- Split navigation -----
    def split_focus_up():
        actions.user.vim_run_normal("\\<c-w>k")

    def split_focus_down():
        actions.user.vim_run_normal("\\<c-w>j")

    def split_focus_left():
        actions.user.vim_run_normal("\\<c-w>h")

    def split_focus_right():
        actions.user.vim_run_normal("\\<c-w>l")

    def split_focus_next():
        actions.user.vim_run_normal("\\<c-w>w")

    def split_focus_previous():
        actions.user.vim_run_normal("\\<c-w>W")

    def split_focus_index(index: int):
        actions.user.vim_set_normal_exterm()
        actions.insert(f"{index}")
        actions.key("ctrl-w ctrl-w")

    def split_focus_most_recent():
        actions.user.vim_run_normal("\\<c-w>p")

    # ----- Split resize -----
    # FIXME: These should restore the original mode, as sometimes I use this from
    # terminal mode
    def split_shrink_width():
        actions.user.vim_run_normal("\\<c-w><")

    def split_shrink_height():
        actions.user.vim_run_normal("\\<c-w>-")

    def split_expand_width():
        actions.user.vim_run_normal("\\<c-w>>")

    def split_expand_height():
        actions.user.vim_run_normal("\\<c-w>+")

    # ----- Split layout -----
    def split_toggle_orientation():
        actions.user.vim_run_normal("\\<c-w>r")

    def split_close():
        actions.user.vim_run_normal("\\<c-w>q")

    def split_close_all():
        actions.user.vim_run_normal("\\<c-w>o")

    # FIXME: Move this to vim-zoom
    # Requirement: https://github.com/dhruvasagar/vim-zoom
    def split_toggle_maximize():
        actions.user.vim_run_normal("\\<c-w>m")


# TEMPORARY: Once https://github.com/talonhub/community/pull/1446 is merged, this should be removed
@mod.action_class
class SplitActions:
    # Creation

    ## Empty splits
    def split_create():
        """Creates a new empty split. The default orientation is application dependent"""

    def split_create_right():
        """Create a new empty split to the right"""

    def split_create_left():
        """Create a new empty split to the left"""

    def split_create_down():
        """Create a new empty split to the bottom"""

    def split_create_up():
        """Create a new empty split to the top"""

    def split_create_vertically():
        """Create a new empty vertical split. The left or right orientation is application dependent"""

    def split_create_horizontally():
        """Create a new empty horizontal split. The top or bottom orientation is application dependent"""

    ## Duplicate splits
    def split_clone():
        """Clones the active view into a new split. The default orientation is application dependent"""

    def split_clone_right():
        """Clone the active view into a new split opened to the right"""

    def split_clone_left():
        """Clone the active view into a new split opened to the left"""

    def split_clone_down():
        """Clone the active view into a new split opened to the bottom"""

    def split_clone_up():
        """Clone the active view into a new split opened to the top"""

    def split_clone_vertically():
        """Clone the active view vertically. The left or right orientation is application dependent"""

    def split_clone_horizontally():
        """Clone the active view horizontally. The top or bottom orientation is application dependent"""

    def split_reopen_last():
        """Reopen the most recently closed split at the same orientation"""

    # Destruction
    def split_close():
        """Closes the current split"""

    def split_close_all():
        """Closes all splits"""

    # Navigation
    def split_focus_right():
        """Focus on the split to the right of the current view"""

    def split_focus_left():
        """Focus on the split to the left of the current view"""

    def split_focus_down():
        """Focus on the split below the current view"""

    def split_focus_up():
        """Focus on the split above the current view"""

    def split_focus_next():
        """Focuses on the next available split"""

    def split_focus_previous():
        """Focuses on the previous available split"""

    def split_focus_first():
        """Focuses on the first split"""

    def split_focus_final():
        """Focuses on the final split"""

    def split_focus_most_recent():
        """Focuses on the most recently used split"""

    def split_focus_index(index: int):
        """Focuses on the split at the specified index"""

    def split_focus_negative_index(index: int):
        """Focuses on the split at the specified index, negatively indexed from the end"""

    # Arrangement
    def split_move_right():
        """Move the active split to the right. The creation of a new split is application dependent."""

    def split_move_left():
        """Move the active split to the left. The creation of a new split is application dependent."""

    def split_move_down():
        """Move the active split down. The creation of a new split is application dependent."""

    def split_move_up():
        """Move the active split up. The creation of a new split is application dependent."""

    def split_toggle_zen():
        """Centers the active split (eg: zen mode)"""

    def split_rotate_right():
        """Rotates the splits to the right"""

    def split_rotate_left():
        """Rotates the splits to the left"""

    # Resizing
    def split_toggle_orientation():
        """Flips the orientation of the active split"""

    def split_toggle_maximize():
        """Maximizes the active split"""

    def split_layout_reset():
        """Resets all the split sizes"""

    def split_expand():
        """Expands the both the width and height of the split"""
        actions.user.split_expand_width()
        actions.user.split_expand_height()

    def split_expand_width():
        """Expands the split width"""

    def split_expand_height():
        """Expands the split height"""

    def split_shrink():
        """Shrinks the both the width and height of the split"""
        actions.user.split_shrink_width()
        actions.user.split_shrink_height()

    def split_shrink_width():
        """Shrinks the split width"""

    def split_shrink_height():
        """Shrinks the split height"""

    def split_set_width(width: int):
        """Sets the split width"""

    def split_set_height(height: int):
        """Sets the split height"""

    def split_move_next_tab():
        """Move the current window to the next tab

        This is only applicable to editors that have tabs that contain splits, such
        as neovim, etc"""

    def split_move_previous_tab():
        """Move the current window to the previous tab

        This is only applicable to editors that have tabs that contain splits, such
        as neovim, etc"""

    def split_move_new_tab():
        """Move the current window to a new tab

        This is only applicable to editors that have tabs that contain splits, such
        as neovim, etc"""
