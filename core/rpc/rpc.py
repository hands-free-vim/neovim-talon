from talon import Context, Module, actions, app, settings, ui

from .direct_input import VimDirectInput

import logging

# TODO: make sure pynvim is installed in talon python environment
import pynvim


class VimRPC:
    """Implementation of functionality when RPC is available."""

    def __init__(self, nvrpc):
        self.nvrpc = nvrpc

    def run_command_mode_command(self, cmd):
        """Run a command in commandline mode using RPC.

        This requires some special casing because of support for direct key
        input. This means that certain commands will come in a newline
        character if the command is meant to be executed immediately, otherwise
        the intention is actually to let the user continue to interact after
        the input goes in, in which case we actually redirect back to the
        direct input from here.

        NOTE: This has some pretty significant quirks compared to is running
        commands with direct input. For instance if you have a command declared
        that maps to a function, like "command! :Files fzf#blah" you need a
        very specific invocation for this to work, which is `:exe ":Files"\n` .
        Since we want these comments to work generically across systems that
        have both RPC and not, unfortunately it means we need to rely on the
        more complicated invocation even for when were not using RPC, to avoid
        the duplication... there might be some better way to do this but I
        haven't figured it out yet.
        """
        if cmd[-1] != "\n":
            v = VimDirectInput()
            v.run_command_mode_command(cmd)
        else:
            try:
                # print(f"sending: {cmd}")
                self.nvrpc.nvim.command(cmd, async_=True)
            # I sometimes get this for things like needing a w! for write...
            except pynvim.api.common.NvimError as e:
                print("NvimError START")
                actions.user.notify(e)
                self.nvrpc.nvim.err_write(str(e))
                print(e)
                print("NvimError END")
            except Exception as e:
                actions.user.notify("Unknown Neovim API error. See talon log")
                print("NvimError START")
                print(e)
                print("NvimError END")

    def run_command_mode_command_exterm(self, cmd):
        """Exit terminal mode and run a command in commandline mode using RPC."""
        if actions.user.vim_is_terminal():
            actions.user.vim_set_normal_exterm()
        self.run_command_mode_command(cmd)

    def run_normal_mode_command(self, cmd):
        cmd = cmd.replace('"', r"\"")
        self.nvrpc.nvim.command(f':exe "normal" "{cmd}"', async_=True)


class NeoVimRPC:
    """For setting/pulling the modes using RPC"""

    def __init__(self):
        self.init_ok = False
        self.nvim = None

        if settings.get("user.vim_use_rpc") == 0:
            return

        self.rpc_path = self.get_active_rpc()
        if self.rpc_path is not None:
            try:
                # XXX - I'm not sure why but suddenly talon is automatically
                # setting the loggers associated with pynvim to DEBUG, so I
                # need to set them to WARNING every time
                loggers = logging.root.manager.loggerDict.keys()
                for l in loggers:
                    # if l.startswith("pynvim"):
                    # print(f"DEBUG: Resetting log level for {l}")
                    nvim_logger = logging.getLogger(l)
                    nvim_logger.setLevel(logging.ERROR)
                # loggers = [
                #     logging.getLogger(name) for name in logging.root.manager.loggerDict
                # ]

                # NOTE: This is used to avoid "Using selector: EpollSelector" spam
                from pprint import pprint

                # pprint("Detected loggers:")
                # pprint(loggers)
                self.nvim = pynvim.attach("socket", path=self.rpc_path)
            except RuntimeError:
                return
            self.init_ok = True
        else:
            return

    def get_active_rpc(self):
        title = ui.active_window().title
        if "RPC" in title:
            named_pipe = title.split("RPC:")[1].split(" ")[0]
            return named_pipe
        return None

    def get_active_mode(self):
        # print("get_active_mode()")
        mode = self.nvim.request("nvim_get_mode")
        # print(f"get_active_mode(): {mode:}")
        return mode
