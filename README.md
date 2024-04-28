# neovim-talon

Talon user file set for controlling both neovim editing and neovim terminals using Talon voice.

## Installation

NOTE: Atm you need to use the beta branch of this repository.

Download or clone the repo to your Talon user folder:

```
git clone https://github.com/hands-free-vim/neovim-talon
cd neovim-talon
git checkout beta
```

## FAQ

### What's the difference with talon-vim?

If you have never heard of talon-vim, you can ignore it. Otherwise, you just need to know that neovim-talon is the new talon-vim. In other words, neovim-talon is a more barebones refactor of the old fidgetingbits talon-vim repo code.

### Python dependencies?

All Python package dependencies are present in the .subtrees directory so that no pip installations are needed. If packages have been installed manually through pip, these will be preferred (e.g. so that faster binary packages can be used.)
