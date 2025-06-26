Goal: Be able to type go ___ in browser and it takes you to the preset websites

SETUP BROWSER go SHORTCUT:
    Brave Browser:
    1.  Go to Settings → Search Engine → Manage Search Engines
        Or just paste this in your address bar: brave://settings/searchEngines
    2.  Scroll to “Site Search” and click “Add”
    3.  Fill in the fields like this:
            Search engine: Go Links
            Keyword: go
            URL with %s: http://go.local/%s
    4. Click Add


SETUP your shortcut file
    1.  Make a shortcuts.json file
    2.  use the following format to make your shortcuts:
{
    "<shortcut name>":      "<URL>",
    "<shortcut name2>":      "<URL2>"
}

Setup For Startup:

    MacOS:
        1.  Make a bin directory in your home directory

        2.  write:
#!/bin/bash
cd /Users/username/Documents/Projects/flask-go-service
source venv/bin/activate  # only if you're using a virtual environment
python3 /Users/username/Documents/Projects/flask-go-service/local-flask-web-redirect.py
        3. Make plist file.