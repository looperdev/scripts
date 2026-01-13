# Dev Windows Machine Install

# Install hyper-v
# Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

# dev software
# winget install -e --id Git.Git
# winget install -e --id Notepad++.Notepad++
# winget install -e --id Microsoft.WindowsTerminal
# winget install -e --id Microsoft.VisualStudioCode
winget install --id=Neovim.Neovim  -e
winget install --id=sharkdp.fd -e
winget install --id=BurntSushi.ripgrep.MSVC -e
winget install --id=junegunn.fzf  -e
winget install -e --id=sharkdp.bat

# Setup git config
git config --global user.email "looperjp@gmail.com"
git config --global user.name "Jonathan Looper"


# Setup ssh key
# ssh-keygen -t ed25519 -C "looperjp@gmail.com"

# Copy ssh key ~/.ssh/id_ed25519.pub to git under Profile | Settings | SSH keys | New SSH key

# Get the scripts repo for further customization
# git clone git@github.com:looperdev/scripts.git
