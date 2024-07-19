import pathlib
import pynvim

from talon import Context, Module, actions, app, settings, ui, registry
from ..rpc.rpc import NeoVimRPC

mod = Module()


@mod.scope
def scope():
    return {"neovim_plugin": neovim_plugin_list()}


# Cached list of plugins. Refreshable by calling voice command
neovim_plugin_cache = None


def _nixvim_plugin_list(rpc: NeoVimRPC) -> list[str]:
    """Pulls the list of plugins used by nixvim out of the nix store

    nixvim sets up a custom pack dir called myNeovimPackages"""

    runtimepath = rpc.nvim.command_output(":set runtimepath")
    # We get back a string like:
    # runtimepath=<path>,<path>,<path>
    paths = runtimepath.split("=")[1].split(",")
    plugins = []
    for path in paths:
        if path.startswith("/nix/store") and path.endswith("vim-pack-dir"):
            pack_dir = pathlib.Path(path) / "pack" / "myNeovimPackages"
            plugins = [p.stem for p in pack_dir.rglob("*") if p.is_symlink()]
    return plugins


def _lazyvim_plugin_list(rpc: NeoVimRPC) -> list[str]:
    """Pulls the list of plugins used by lazyvim plugin manager"""
    plugins = []
    try:
        # Returns a list of tables like { { "name0", _ = ... }, { "name1", _ = ... }, ...}
        lua = """
        local plugins = require('lazy').plugins()
        local names = {}
        for _, plugin in ipairs(plugins) do
            table.insert(names, plugin[1])
        end
        return names
        """
        plugin_list = rpc.nvim.exec_lua(lua)
        # Returns a list of strings like:
        # ['folke/lazy.nvim', 'nvim-lua/plenary.nvim', 'nvim-telescope/telescope.nvim']
        for plugin in plugin_list:
            name = plugin.split("/")[1]
            if name.endswith(".nvim"):
                name = name[:-5]
            if name.endswith(".vim"):
                name = name[:-4]
            plugins.append(name)
    except pynvim.api.NvimError as e:
        print(e)
        return plugins
    return plugins


def _vundle_plugin_list(rpc: NeoVimRPC) -> list[str]:
    """Pulls the list of plugins used by Vundle plugin manager"""
    plugins = []
    try:
        plugin_list = rpc.nvim.command_output(":PluginList")
    except pynvim.api.NvimError:
        return plugins
    # FIXME: parse output
    app.notify("ERROR: Vundle plugin list not implemented. File an issue on GitHub.")
    return plugins


def _vim_plug_plugin_list(rpc: NeoVimRPC) -> list[str]:
    """Pulls the list of plugins used by vim-plug plugin manager"""
    plugins = []
    try:
        plugin_list = rpc.nvim.command_output(":PlugStatus")
    except pynvim.api.NvimError:
        return plugins
    # FIXME: parse output
    app.notify("ERROR: vim-plug plugin list not implemented. File an issue on GitHub.")
    return plugins


def _packer_plugin_list(rpc: NeoVimRPC) -> list[str]:
    """Pulls the list of plugins used by packer plugin manager"""
    plugins = []
    plugin_list = rpc.nvim.command_output(":lua print(vim.g.packer_plugins)")
    if plugin_list == "nil":
        return plugins
    # FIXME: parse output
    app.notify("ERROR: packer plugin list not implemented. File an issue on GitHub.")
    return plugins


def neovim_update_plugin_list() -> list[str]:
    """Uses neovim RPC to get the list of plugins"""
    if "neovim" not in registry.active_apps():
        return []
    rpc = NeoVimRPC()
    if rpc.init_ok is False:
        return []

    plugin_manager_funcs = [
        _lazyvim_plugin_list,
        _nixvim_plugin_list,
        _vundle_plugin_list,
        _vim_plug_plugin_list,
        _packer_plugin_list,
    ]

    for func in plugin_manager_funcs:
        result = func(rpc)
        if len(result) > 0:
            return result

    return []


def neovim_plugin_list() -> set[str] | None:
    """Returns a cached or new list of installed neovim plugins"""
    if "neovim" not in registry.active_apps():
        return None
    global neovim_plugin_cache
    if neovim_plugin_cache is None:
        neovim_plugin_cache = neovim_update_plugin_list()
    return set(neovim_plugin_cache)


@mod.action_class
class PluginActions:
    def neovim_plugin_list_refresh():
        """Refresh the cached list of installed neovim plugins"""
        global neovim_plugin_cache
        neovim_plugin_cache = neovim_update_plugin_list()
        scope.update()

    def neovim_plugin_list_print():
        """Print the list of installed neovim plugins"""
        if neovim_plugin_cache is None:
            actions.user.neovim_plugin_list_refresh()
        print(neovim_plugin_cache)


ui.register("win_focus", scope.update)
ui.register("win_title", scope.update)
