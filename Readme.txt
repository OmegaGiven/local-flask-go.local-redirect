Goal: Be able to type go/<alias> in browser and it takes you to the preset websites

SETUP BROWSER go SHORTCUT in case you dont want to setup a go alias on your local computer:
    Brave Browser:
    1.  Go to Settings → Search Engine → Manage Search Engines
        Or just paste this in your address bar: brave://settings/searchEngines
    2.  Scroll to “Site Search” and click “Add”
    3.  Fill in the fields like this:
            Search engine: Go Links
            Keyword: go
            URL with %s: http://0.0.0.0/%s
    4. Click Add


SETUP your shortcut file

{
    "<shortcut name>":      "<URL>",
    "<shortcut name2>":      "<URL2>"
}

Setup python:
    pip install flask


Setup For Startup:

    MacOS / LINUX:
        1.  Make a bin directory in your home directory

        2.  write:
#!/bin/bash
cd /Users/username/Documents/Projects/flask-go-service
source venv/bin/activate  # only if you're using a virtual environment
python3 /Users/username/Documents/Projects/flask-go-service/local-flask-web-redirect.py
        3. Make plist file.


add a custom localhost alias so you can do <localhost alias>/<shortcut alias>

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