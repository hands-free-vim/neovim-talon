from talon import Context, Module, actions, app, settings, ui


class VimDirectInput:
    """For when RPC is not available or we want to insert partial commands

    This relies on a more finnicky method of detecting no changes, stringing
    commands together, which can be a bit buggy. It's supported for people that
    can't use neovim RPC for some reason, like if you are using something with
    a VIM-like mode, like a console with bindkeys -v set"""

    def run_command_mode_command(self, cmd):
        """Run a command in commandline mode using direct keyboard input."""
        v = actions.user.vim_set_command()
        v.insert_command_mode_command(cmd)

    def run_command_mode_command_exterm(self, cmd):
        """Run a command in commandline mode using direct keyboard input."""
        v = actions.user.vim_set_command()
        v.insert_command_mode_command(cmd)

    def run_normal_mode_command(self, cmd):
        actions.insert(cmd)
