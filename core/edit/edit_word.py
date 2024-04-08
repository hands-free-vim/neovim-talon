from talon import Context, actions

# Context valid in some sort of motion mode, so not including terminal or command mode
ctx_motion = Context()
ctx_motion.matches = r"""
app: neovim
not tag: user.vim_mode_terminal
and not tag: user.vim_mode_command
"""

ctx_command = Context()
ctx_command.matches = r"""
tag: user.vim_mode_command
"""

ctx_visual = Context()
ctx_visual.matches = r"""
tag: user.vim_mode_visual
"""


@ctx_motion.action_class("edit")
class EditActions:
    def word_left():
        actions.user.vim_run_any_motion_key("b")

    def word_right():
        actions.user.vim_run_any_motion_key("w")

    def select_word():
        actions.user.vim_run_visual("e")

    def extend_word_left():
        actions.user.vim_run_visual("b")

    def extend_word_right():
        actions.user.vim_run_visual("e")

    def delete_word():
        actions.user.vim_run_normal("dw")


@ctx_motion.action_class("user")
class UserActions:
    def delete_word_left():
        actions.user.vim_run_normal("db")

    def delete_word_right():
        actions.user.vim_run_normal("dw")


@ctx_command.action_class("edit")
class EditActions:
    def word_left():
        actions.key("shift-left")

    def word_right():
        actions.key("shift-right")


@ctx_command.action_class("user")
class UserActions:
    def delete_word_left():
        actions.key("ctrl-w")


@ctx_visual.action_class("edit")
class EditActions:
    def select_word():
        actions.insert("e")

    def extend_word_left():
        actions.insert("obo")

    def extend_word_right():
        actions.insert("e")
