Goal: Be able to type go/<alias> in browser and it takes you to the preset websites


# Setup the go/ redirect
## For Browser shortcuts:
    Brave Browser:
    1.  Go to Settings → Search Engine → Manage Search Engines
        Or just paste this in your address bar: brave://settings/searchEngines
    2.  Scroll to “Site Search” and click “Add”
    3.  Fill in the fields like this:
            Search engine: Go Links
            Keyword: go
            URL with %s: http://0.0.0.0/%s
    4. Click Add
## OR you can edit your local host alias to include go as an alias as well as localhost
WINDOWS:
    1. notepad %systemroot%\System32\drivers\etc\hosts
    2. 
        <ip adddress> <your alias>
        0.0.0.0 localhost local go
MAC / LINUX
    1. sudo nano /etc/hosts
    2. 
        <ip adddress> <your alias>
        0.0.0.0 localhost local go

SETUP your shortcut file: shortcuts.json
{
    "<shortcut name>":      "<URL>" ,
    "<shortcut name2>":      "<URL2>"
}


Setup python:
    pip install flask


# Setup For Startup without docker:
    MacOS / LINUX:
        1.  Make a bin directory in your home directory
        2.  write:
#!/bin/bash
cd /Users/username/Documents/Projects/flask-go-service
source venv/bin/activate  # only if you're using a virtual environment
python3 /Users/username/Documents/Projects/flask-go-service/local-flask-web-redirect.py
        3. Make plist file.

LINUX have flask app work on startup:

    sudo nano /etc/systemd/system/web-aliases.service

    [Unit]
    Description=My Python Script
    After=network.target

    [Service]
    ExecStart=/usr/bin/python3 /usr/local/bin/my_script.py
    Restart=always

    [Install]
    WantedBy=multi-user.target

    sudo systemctl daemon-reload
    sudo systemctl start web-aliases.service
    sudo systemctl enable web-aliases.service


# Docker setup\
    install docker
    cd <working dir>
    docker compose up



