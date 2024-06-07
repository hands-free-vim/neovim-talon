app: neovim
-

# requires: https://github.com/folke/lazy.nvim
lazy (open | home):     user.lazy_home()
lazy install:           user.lazy_install()
lazy update:            user.lazy_update()
lazy sync:              user.lazy_sync()
lazy clean:             user.lazy_clean()
lazy clear:             user.lazy_clear()
lazy check:             user.lazy_check()
lazy log:               user.lazy_log()
lazy restore:           user.lazy_restore()
lazy profile:           user.lazy_profile()
lazy debug:             user.lazy_debug()
lazy help:              user.lazy_help()
lazy health:            user.lazy_health()
lazy (close | quit):    user.lazy_close()
