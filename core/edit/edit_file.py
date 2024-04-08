from talon import Context, actions

# Context valid in some sort of motion mode, so not including terminal or command mode
ctx_motion = Context()
ctx_motion.matches = r"""
app: neovim
not tag: user.vim_mode_terminal
and not tag: user.vim_mode_command
"""

ctx_terminal = Context()
ctx_terminal.matches = r"""
tag: user.vim_mode_terminal
"""

ctx_visual = Context()
ctx_visual.matches = r"""
tag: user.vim_mode_visual
"""


@ctx_motion.action_class("edit")
class EditActions:
    def file_start():
        actions.user.vim_run_any_motion("gg")

    def file_end():
        actions.user.vim_run_any_motion_key("G")

    def select_all():
        actions.user.vim_run_normal("ggVG")
        # See vim_normal.talon and vim_visual.talon for edit.extend_ commands

    def extend_file_start():
        actions.user.vim_run_visual("gg0")

    def extend_file_end():
        actions.user.vim_run_visual("G")


@ctx_terminal.action_class("edit")
class EditActions:
    # XXX - this might be a bit much if eventually we want this to mean to let
    # everything on the command-line itself, although then we might be able to
    # just use things like select line/graph, etc
    def select_all():
        actions.user.vim_run_normal_exterm("ggVG")


@ctx_visual.action_class("edit")
class EditActions:
    def extend_file_start():
        actions.insert("ogg0o")

    def extend_file_end():
        actions.insert("G")
        # XXX - This should be a callable function so we can do things like:
        #       '.swap on this <highlight motion>'
        #       'swap between line x, y'
        # assumes visual mode
