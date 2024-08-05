from talon import Context, Module, actions, app, settings, ui

from .api_internal import VimApiInternal

import time


class VimDirectInput(VimApiInternal):
    """For when RPC is not available or we want to insert partial commands

    This relies on a more finnicky method of detecting no changes, stringing
    commands together, which can be a bit buggy. It's supported for people that
    can't use neovim RPC for some reason, like if you are using something with
    a VIM-like mode, like a console with bindkeys -v set"""

    def __init__(self):
        self.wait_mode_timeout = 0.25

    def run_command_mode_command(self, cmd):
        """Run a command in command line mode using direct keyboard input."""
        v = actions.user.vim_set_command()
        v.insert_command_mode_command(cmd)

    def run_command_mode_command_exterm(self, cmd):
        """Run a command in command line mode using direct keyboard input."""
        v = actions.user.vim_set_command()
        v.insert_command_mode_command(cmd)

    def run_normal_mode_command(self, cmd):
        """Run a command in normal mode using direct keyboard input."""
        actions.insert(cmd)

    def mode(self):
        """Get the current mode using direct keyboard input."""
        title = ui.active_window().title
        mode = None
        if "MODE:" in title:
            mode = title.split("MODE:")[1].split(" ")[0]
            if mode not in self.vim_modes.keys():
                return None
        return mode

    def wait_mode_change(self, wanted):
        """Wait for the mode to change to the wanted mode using direct keyboard input."""
        time.sleep(self.wait_mode_timeout)
        return True
