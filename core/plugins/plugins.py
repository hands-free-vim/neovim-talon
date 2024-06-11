from talon import Context, Module, actions, app, settings, ui
from ..rpc.api import VimAPI

mod = Module()


@mod.scope
def scope():
    return {"neovim_plugin": neovim_plugin_list()}


# Cached list of plugins. Refreshable by calling voice command
neovim_plugin_cache = None


def neovim_update_plugin_list():
    """Uses neovim RPC to get the list of plugins"""
    vapi = VimAPI()
    # vapi.nvim.request("nvim_get_mode")
    print("Would get plugin list here")

    # Vundle: ":PluginList"
    # vim-plug: ":PlugStatus" or "vim.g.plugs"
    # lazy: ":lua require('lazy').plugins()"
    # packer: " _G.packer_plugins"
    return {plugin for plugin in ["taboo"]}


def neovim_plugin_list():
    """Returns a cached or new list of installed neovim plugins"""
    print("Checking for plugin list")
    global neovim_plugin_cache
    if neovim_plugin_cache is None:
        print("Empty cache, updating")
        neovim_plugin_cache = neovim_update_plugin_list()
    else:
        print("Using cached plugin list")
    print(neovim_plugin_cache)
    return neovim_plugin_cache


@mod.action_class
class PluginActions:
    def neovim_plugin_list_refresh():
        """Refresh the cached list of installed neovim plugins"""
        global neovim_plugin_cache
        neovim_plugin_cache = neovim_update_plugin_list()
