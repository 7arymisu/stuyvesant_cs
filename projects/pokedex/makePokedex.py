#! /usr/bin/python3
print("Content-Type: text/html\n\n")

# used when debugging on the web
import os # import for chmod
import cgitb # import to catch HTTP errors (when running on the web)
cgitb.enable() # enable your error output for HTTP

# constant
INDENT = "  "

# global variable
page = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Metadata -->
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    
    <!-- Stylesheet -->
    <link rel="stylesheet" href="_STYLE_" />
    
    <!-- Title -->
    <title>_TITLE_</title>
  </head>
  <body>
    _NAVBAR_
    _BODY_
  </body>
</html>
'''