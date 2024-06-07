from talon import Module, Context, actions

mod = Module()

# when lazy main menu is not shown
ctx_off = Context()
ctx_off.matches = r"""
app: neovim
and not win.title: /FILETYPE:\[lazy\]/
"""

# when lazy main menu is shown
ctx_on = Context()
ctx_on.matches = r"""
app: neovim
and win.title: /FILETYPE:\[lazy\]/
"""


# https://github.com/folke/lazy.nvim?tab=readme-ov-file#-usage
@mod.action_class
class Actions:
    def lazy_home():
        """open lazy home menu"""

    def lazy_install():
        """install missing lazy plugins"""

    def lazy_update():
        """update lazy plugins"""

    def lazy_sync():
        """run lazy install, clean and update"""

    def lazy_clean():
        """clean lazy plugins that are no longer needed"""

    def lazy_clear():
        """clear lazy finished tasks"""

    def lazy_check():
        """check for lazy plugins updates and show the log (git fetch)"""

    def lazy_log():
        """show lazy recent updates"""

    def lazy_restore():
        """updates all lazy plugins to the state in the lockfile"""

    def lazy_profile():
        """show lazy detailed profiling"""

    def lazy_debug():
        """show lazy debug information"""

    def lazy_help():
        """toggle the lazy help page"""

    def lazy_health():
        """run :checkhealth lazy"""

    def lazy_close():
        """close lazy home menu"""


@ctx_off.action_class("user")
class Actions:
    def lazy_home():
        actions.user.vim_run_command_exterm(":Lazy home\n")

    def lazy_install():
        actions.user.vim_run_command_exterm(":Lazy install\n")

    def lazy_update():
        actions.user.vim_run_command_exterm(":Lazy update\n")

    def lazy_sync():
        actions.user.vim_run_command_exterm(":Lazy sync\n")

    def lazy_clean():
        actions.user.vim_run_command_exterm(":Lazy clean\n")

    def lazy_clear():
        actions.user.vim_run_command_exterm(":Lazy clear\n")

    def lazy_check():
        actions.user.vim_run_command_exterm(":Lazy check\n")

    def lazy_log():
        actions.user.vim_run_command_exterm(":Lazy log\n")

    def lazy_restore():
        actions.user.vim_run_command_exterm(":Lazy restore\n")

    def lazy_profile():
        actions.user.vim_run_command_exterm(":Lazy profile\n")

    def lazy_debug():
        actions.user.vim_run_command_exterm(":Lazy debug\n")

    def lazy_help():
        actions.user.vim_run_command_exterm(":Lazy help\n")

    def lazy_health():
        actions.user.vim_run_command_exterm(":Lazy health\n")

    # def lazy_close():


@ctx_on.action_class("user")
class Actions:
    def lazy_home():
        actions.user.vim_run_normal("H")

    def lazy_install():
        actions.user.vim_run_normal("I")

    def lazy_update():
        actions.user.vim_run_normal("U")

    def lazy_sync():
        actions.user.vim_run_normal("S")

    def lazy_clean():
        actions.user.vim_run_normal("X")

    # def lazy_clear():

    def lazy_check():
        actions.user.vim_run_normal("C")

    def lazy_log():
        actions.user.vim_run_normal("L")

    def lazy_restore():
        actions.user.vim_run_normal("R")

    def lazy_profile():
        actions.user.vim_run_normal("P")

    def lazy_debug():
        actions.user.vim_run_normal("D")

    def lazy_help():
        actions.user.vim_run_normal("?")

    # def lazy_health():

    def lazy_close():
        actions.user.vim_run_normal("q")
