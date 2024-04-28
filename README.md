<!-- vim-markdown-toc GFM -->

- [neovim-talon](#neovim-talon)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [FAQ](#faq)
    - [What's the difference with talon-vim?](#whats-the-difference-with-talon-vim)

<!-- vim-markdown-toc -->

# neovim-talon

Talon user file set for controlling both neovim editing and neovim terminals using Talon voice.

## Prerequisites

- neovim Python package: https://github.com/neovim/pynvim (installed in Talon Python)

On Windows:

```
%APPDATA%\talon\venv\3.11\Scripts\python.exe -s -m pip install pynvim
```

On Linux:

TBC

On OS X:

TBC

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
