# Setting up WSL

Make sure you have appropriate dependencies:
```bash
sudo apt-get update
sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4
```

And then install Chrome:
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt -y install ./google-chrome-stable_current_amd64.deb
rm ./google-chrome-stable_current_amd64.deb

# Check working with:
google-chrome --version
```

We should then be able to run Selenium & Playwright tests **in headless mode**.