class VimApiInternal:
    """Internal API base class for specific actions.
    In practice, the implementations are RPC or direct input."""

    def run_command_mode_command(self, cmd):
        """Run a command in command line mode."""
        pass

    def run_command_mode_command_exterm(self, cmd):
        """Exit terminal mode and run a command in command line mode."""
        pass

    def run_normal_mode_command(self, cmd):
        """Exit terminal mode and run a command in normal mode."""
        pass

    def mode(self):
        """Get the current mode."""
        pass

    def wait_mode_change(self, wanted):
        """Wait for the mode to change to the wanted mode"""
        pass
