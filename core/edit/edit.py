from talon import Context, actions, clip

# TODO: can we merge ctx, ctx_normal and ctx_motion into one context?
# otherwise, how does talon prioritize which to use in case of conflicts?

# Context valid for most modes
ctx = Context()
ctx.matches = r"""
app: neovim
and not tag: user.vim_mode_command
"""

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


# Since this file includes anything that could by running in terminal mode or
# other modes, they should use the exterm version of the API in almost all
# cases.
@ctx.action_class("edit")
class EditActions:
    # ----- Navigation -----
    def up():
        actions.key("up")

    def down():
        actions.key("down")

    def left():
        actions.key("left")

    def right():
        actions.key("right")

    def page_up():
        # Use ctrl-u for half page. Use ctrl-b for full page

        # actions.user.vim_run_normal_exterm_key("ctrl-u")
        actions.user.vim_run_normal_exterm_key("ctrl-b")

    def page_down():
        # Use ctrl-d for half page. Use ctrl-f for full page
        # actions.user.vim_run_normal_exterm_key("ctrl-d")
        actions.user.vim_run_normal_exterm_key("ctrl-f")

    # ----- Find -----
    def find(text: str = None):
        actions.user.vim_run_normal_exterm_key("/")
        # TODO: support inserting text to find
        # if text:
        #     actions.insert(text)

    # ----- Zoom -----
    # FIXME: This wrong depending on the terminal. Gnome is ctrl--
    def zoom_out():
        actions.key("ctrl-shift--")

    def zoom_in():
        actions.key("ctrl-shift-+")


@ctx_motion.action_class("edit")
class EditActions:
    # ----- Selection -----
    def extend_left():
        actions.user.vim_run_visual("h")

    def extend_right():
        actions.user.vim_run_visual("l")

    # ----- Save -----
    def save():
        actions.user.vim_run_command(":w\n")

    # ----- Delete, Undo, Redo -----
    def delete():
        actions.user.vim_run_insert_key("backspace")

    def undo():
        actions.user.vim_run_normal_key("u")

    def redo():
        actions.user.vim_run_normal_key("ctrl-r")

    # ----- Cut, Copy, Paste -----
    # Note following two are for mouse/highlighted copy/paste. shouldn't be
    # used for actual vim commands
    def copy():
        actions.key("ctrl-shift-c")

    def paste():
        # actions.user.vim_normal_mode("p")
        actions.key("ctrl-shift-v")
        # NOTE: There is it delay that happens inside of vim that can cause out
        # of order key pressing, in it seems to be that it's because the output
        # of this key press actually happens after other key presses start
        # getting interpreted? in example would be "sit graves pasty round".
        # typically the output of this will be something like:
        # `(<pasted content>)`
        # but the intended output would be
        # `<pasted content>()`
        # for now the only way i see to fix this is to introduce an artificial
        # delay to allow vim to actually paste the content...
        # time.sleep(0.800)
        #  XXX - This might be one solution for it, but i haven't got it to
        #  work yet
        # actions.user.vim_normal_mode('"+p')

    # ----- Find -----
    def find_next():
        actions.user.vim_run_any_motion_key("n")


@ctx_normal.action_class("edit")
class EditActions:
    # ----- Indent -----
    def indent_more():
        actions.insert(">>")

    def indent_less():
        actions.insert("<<")


@ctx_command.action_class("edit")
class EditActions:
    # ----- Cut, Copy, Paste -----
    def paste():
        actions.key("ctrl-shift-v")


@ctx_terminal.action_class("edit")
class EditActions:
    # ----- Navigation -----
    def page_up():
        actions.key("ctrl-\\ ctrl-n ctrl-b")

    # ----- Cut, Copy, Paste -----
    def paste():
        actions.key("ctrl-shift-v")


@ctx_visual.action_class("edit")
class EditActions:
    # ----- Selection -----
    def extend_left():
        actions.insert("oho")

    def extend_right():
        actions.insert("l")

    # ----- Indent -----
    def indent_less():
        actions.insert("<")

    def indent_more():
        actions.insert(">")

    # ----- Miscellaneous -----
    def selected_text() -> str:
        # gv to reselect
        actions.insert("ygv")
        return clip.get()
