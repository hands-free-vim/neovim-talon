app: neovim
tag: user.splits
-

(split|buf) move new tab: user.split_move_new_tab()
(split|buf) move next tab: user.split_move_next_tab()
(split|buf) move last tab: user.split_move_last_tab()

# TEMPORARY: Once https://github.com/talonhub/community/pull/1446 is merged, these should be removed
# Navigation
cross right: user.split_focus_right()
cross left: user.split_focus_left()
cross down: user.split_focus_down()
cross up: user.split_focus_up()
cross next: user.split_focus_next()
cross last: user.split_focus_last()
cross flip: user.split_focus_most_recent()
(go split | cross) <number>: user.split_focus_number(number)

# Arrangement
split move right: user.split_move_right()
split move left: user.split_move_left()
split move down: user.split_move_down()
split move up: user.split_move_up()
split toggle: user.split_layout_toggle()
split center: user.split_center()
split rotate right: user.split_rotate_right()
split rotate left: user.split_rotate_left()

# Resizing
split wider: user.split_expand_width()
split taller: user.split_expand_height()
split thinner: user.split_shrink_width()
split shorter: user.split_shrink_height()
split set width <number>: user.split_set_width(number)
split set height <number>: user.split_set_height(number)
