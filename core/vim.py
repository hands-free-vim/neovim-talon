from talon import Context, Module, actions, app, settings, ui

mod = Module()

# TODO: add code for creating all of the contexts and associated mode assertions by doing what
# we do in language_modes.py
mode_tag_list = [
    "vim_mode_terminal",
    "vim_mode_command",
    "vim_mode_visual",
    "vim_mode_normal",
    "vim_mode_normal_terminal",
    "vim_mode_insert",
    "vim_mode_select",
]
for entry in mode_tag_list:
    mod.tag(entry, f"tag to load {entry} specific commands")
