from talon import Context, Module, actions, app, settings, ui

from ..rpc.api import VimAPI
from ..rpc.modes import VimMode

mod = Module()


# Actions to run commands in specific modes
# TODO: move the v = VimMode() + switch of mode to mode.py and just call them here
@mod.action_class
class Actions:
    def vim_run_insert(cmd: str):
        """run a given list of commands in normal mode, preserve mode"""
        actions.user.vim_set_insert()
        actions.insert(cmd)

    def vim_run_insert_key(cmd: str):
        """run a given list of commands in normal mode, preserve mode"""
        actions.user.vim_set_insert()
        actions.key(cmd)

    def vim_run_normal(cmd: str):
        """run a given list of commands in normal mode, preserve INSERT"""
        # XXX - This needs to be abstracted for the case where we don't have
        # RPC
        # This is required despite using the nvim.command() method because we
        # can access that mode from terminal mode:
        #  https://github.com/neovim/neovim/issues/4895#issuecomment-303073838
        if actions.user.vim_is_terminal():
            actions.user.vim_set_normal_exterm()
        vapi = VimAPI()
        vapi.api.run_normal_mode_command(cmd)

    def vim_run_normal_np(cmd: str):
        """run a given list of commands in normal mode, don't preserve
        INSERT"""
        actions.user.vim_set_normal_np(auto=True)
        actions.insert(cmd)

    def vim_run_normal_exterm(cmd: str = None):
        """run a given list of commands in normal mode, don't preserve INSERT,
        escape from terminal mode"""
        actions.user.vim_set_normal_exterm()
        if cmd is not None:
            actions.insert(cmd)

    def vim_run_normal_key(cmd: str):
        """press a given key in normal mode"""
        actions.user.vim_set_normal(auto=False)
        actions.key(cmd)

    def vim_run_normal_exterm_key(cmd: str):
        """press a given key in normal mode, and escape terminal"""
        actions.user.vim_set_normal_exterm()
        actions.key(cmd)

    def vim_run_normal_keys(keys: str):
        """press a given list of keys in normal mode"""
        actions.user.vim_set_normal(auto=False)
        for key in keys.split(" "):
            # print(key)
            actions.key(key)

    def vim_run_normal_exterm_keys(keys: str, term_return: str = "False"):
        """press a given list of keys in normal mode"""
        v = actions.user.vim_set_normal_exterm()
        for key in keys.split(" "):
            # print(key)
            actions.key(key)
        if term_return == "True":
            v.set_insert_mode()

    def vim_run_visual(cmd: str):
        """run a given list of commands in visual mode"""
        actions.user.vim_set_visual()
        actions.insert(cmd)

    def vim_run_command(cmd: str):
        """run string of commands in command line mode.

        Preserves INSERT
        """
        vapi = VimAPI()
        vapi.api.run_command_mode_command(cmd)

    def vim_run_command_exterm(cmd: str):
        """run string of commands in command line mode.

        - Preserves INSERT
        - Exits terminal mode
        """
        vapi = VimAPI()
        vapi.api.run_command_mode_command_exterm(cmd)

    # Sometimes the .talon file won't know what mode to run something in, just
    # that it needs to be a mode that supports motions like normal and visual.
    def vim_run_any_motion(cmd: str):
        """run a given list of commands in normal mode"""
        actions.user.vim_set_any_motion_mode()
        actions.insert(cmd)

    # Sometimes the .talon file won't know what mode to run something in, just
    # that it needs to be a mode that supports motions like normal and visual.
    def vim_run_any_motion_exterm(cmd: str):
        """run a given list of commands in some motion mode"""
        actions.user.vim_set_any_motion_mode_exterm()
        actions.insert(cmd)

    def vim_run_any_motion_key(cmd: str):
        """run a given list of commands in normal mode"""
        actions.user.vim_set_any_motion_mode()
        actions.key(cmd)

    def vim_run_any_motion_exterm_key(cmd: str):
        """run a given list of commands in normal mode"""
        actions.user.vim_set_any_motion_mode_exterm()
        actions.key(cmd)
