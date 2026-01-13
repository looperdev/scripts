cat pkglist.txt | xargs sudo apt-get -y install
sudo systemctl enable ssh
sudo systemctl start ssh 
curl -LsSf https://astral.sh/uv/install.sh | sh
