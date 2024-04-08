from .rpc import NeoVimRPC
from .rpc import VimRPC
from .direct_input import VimDirectInput


class VimAPI:
    """Abstraction of calls that go through RPC or not."""

    def __init__(self):
        self.api = self._get_api()
        self.nvrpc = None

    # socket
    def _get_api(self):
        """return a RPC or non-RPC API object"""
        # XXX - This is a hack but just trying to get rid of "DEBUG Using selector:
        # EpollSelector"
        # logging.getLogger("asyncio").setLevel(logging.WARNING)
        self.nvrpc = NeoVimRPC()
        if self.nvrpc.init_ok is True:
            return VimRPC(self.nvrpc)
        else:
            return VimDirectInput()

    def __del__(self):
        """Clean up the RPC Connection"""
        if self.nvrpc and self.nvrpc.init_ok is True:
            self.nvrpc.nvim.close()
