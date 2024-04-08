from talon import Module

from ..rpc.modes import VimMode

mod = Module()


# Actions to detect modes
@mod.action_class
class Actions:
    def vim_is_terminal():
        """check if currently in terminal mode"""
        v = VimMode()
        return v.is_terminal_mode()

    def vim_is_visual():
        """check if currently in visual mode"""
        v = VimMode()
        return v.is_visual_mode()
