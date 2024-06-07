# FIXME: TEMPORARY: Once https://github.com/talonhub/community/pull/1449 is merged, this file shoulid be removed
# @see tags/line_commands/line_commands.talon in community
find <user.unmodified_key>:
    user.line_find_forward(unmodified_key)

find last <user.unmodified_key>:
    user.line_find_backward(unmodified_key)
