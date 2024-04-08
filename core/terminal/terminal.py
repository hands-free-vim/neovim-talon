from talon import Context, Module, actions

mod = Module()
ctx_normal_terminal = Context()


ctx_normal_terminal.matches = r"""
tag: user.vim_mode_normal_terminal
"""


# this allows using "bring" in normal terminal mode and that will insert
# into the previous position in the terminal mode
@ctx_normal_terminal.action_class("main")
class MainActions:
    def insert(text):
        actions.user.vim_set_insert()
        actions.next(text)
