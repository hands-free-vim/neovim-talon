from talon import Module

from ..rpc.api import VimAPI

mod = Module()


# Actions to modify/set modes
# TODO: rename these function vim_mode_set_* or vim_mode_* instead of vim_set_*?
@mod.action_class
class Actions:
    def vim_set_normal():
        """set normal mode"""
        v = VimAPI()
        v.set_normal_mode()
        return v

    def vim_set_normal_exterm():
        """set normal mode, escaping from the terminal mode"""
        v = VimAPI()
        v.set_normal_mode_exterm()
        return v

    def vim_set_normal_np():
        """set normal mode and don't preserve the previous mode"""
        v = VimAPI()
        v.set_normal_mode_np()
        return v

    def vim_set_visual():
        """set visual mode"""
        v = VimAPI()
        v.set_visual_mode()

    def vim_set_visual_line():
        """set visual line mode"""
        v = VimAPI()
        v.set_visual_line_mode()
        return v

    def vim_set_visual_block():
        """set visual block mode"""
        v = VimAPI()
        v.set_visual_block_mode()

    def vim_set_insert():
        """set insert mode"""
        v = VimAPI()
        v.set_insert_mode()
        return v

    def vim_set_terminal():
        """set terminal mode"""
        v = VimAPI()
        v.set_terminal_mode()
        return v

    def vim_set_command():
        """set command line mode"""
        v = VimAPI()
        v.set_command_mode()
        return v

    def vim_set_command_exterm():
        """set command line mode, escaping from the terminal mode"""
        v = VimAPI()
        v.set_command_mode_exterm()
        return v

    def vim_set_replace():
        """set replace mode"""
        v = VimAPI()
        v.set_replace_mode()
        return v

    def vim_set_visual_replace():
        """set visual replace mode"""
        v = VimAPI()
        v.set_visual_replace_mode()
        return v

    # Why do these exist?
    def vim_set_any_motion_mode():
        """set any motion mode"""
        v = VimAPI()
        v.set_any_motion_mode()
        return v

    def vim_set_any_motion_mode_exterm():
        """set any motion mode, escaping from the terminal mode"""
        v = VimAPI()
        v.set_any_motion_mode_exterm()
        return v
