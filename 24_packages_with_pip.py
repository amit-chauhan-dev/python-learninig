# Installing external packages with pip
# Python has thousands of extra packages (libraries).
# You install them using pip.
# Common commands (run in terminal).


# pip install requests
# pip install pandas
# pip install numpy
# pip list                  # see installed packages
# pip uninstall requests    # remove a package

import requests

response = requests.get("https://api.github.com")
print(response.status_code)