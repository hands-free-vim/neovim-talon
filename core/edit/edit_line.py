from talon import Context, actions, app

import time

# Context valid in some sort of motion mode, so not including terminal or command mode
ctx_motion = Context()
ctx_motion.matches = r"""
app: neovim
not tag: user.vim_mode_terminal
and not tag: user.vim_mode_command
"""

ctx_normal = Context()
ctx_normal.matches = r"""
tag: user.vim_mode_normal
"""


ctx_insert = Context()
ctx_insert.matches = r"""
tag: user.vim_mode_insert
"""

ctx_command = Context()
ctx_command.matches = r"""
tag: user.vim_mode_command
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
    def line_start():
        actions.user.vim_run_any_motion_key("^")

    def line_end():
        actions.user.vim_run_any_motion_key("$")

    def select_line(n: int = None):
        actions.user.vim_run_visual("V")

    def extend_line_up():
        actions.user.vim_run_visual("k^")

    def extend_line_down():
        actions.user.vim_run_visual("j^")

    def extend_line_start():
        actions.user.vim_run_visual("^")

    def extend_line_end():
        actions.user.vim_run_visual("$")


@ctx_motion.action_class("user")
class UserActions:
    def delete_line_start():
        actions.user.vim_run_normal("d0")

    def delete_line_end():
        actions.user.vim_run_normal("d$")


@ctx_normal.action_class("edit")
class EditActions:
    # These differ slightly if we're in normal mode versus visual mode. in normal
    # mode we select up we want to select the current line in the one above, as
    # otherwise there is no current selection
    def extend_line_up():
        actions.insert("Vk")

    def extend_line_down():
        actions.insert("Vj")

    def delete_line():
        actions.insert("dd")


@ctx_insert.action_class("edit")
class EditActions:
    def delete_line():
        actions.user.vim_run_normal("dd")


@ctx_command.action_class("edit")
class EditActions:
    def line_start():
        actions.key("ctrl-b")

    def line_end():
        actions.key("ctrl-e")

    def delete_line():
        actions.key("ctrl-u")


@ctx_terminal.action_class("edit")
class EditActions:
    def select_line(n: int = None):
        if n is not None:
            app.notify("select_line() with argument not implemented")
            return
        actions.user.vim_run_normal_exterm("V")
        time.sleep(1)


@ctx_visual.action_class("edit")
class EditActions:
    # when we're extending a selection in the opposite direction (backwards) we
    # need to a prefix an  beforehand so that it actually extends, rather than
    # changing directions.
    def extend_line_up():
        actions.insert("ok^o")

    def extend_line_down():
        actions.insert("j^")

    def extend_line_start():
        actions.insert("o^o")

    def extend_line_end():
        actions.insert("$")

    def delete_line():
        actions.insert("D")
