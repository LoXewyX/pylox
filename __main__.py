########################
registerOnConsole = True
dropDatabase =      False
########################

from db.db_test import create_essentials
create_essentials(dropIfExists=dropDatabase, reg=registerOnConsole)

# Get main folder route
import pathlib
main_path = str(pathlib.Path(__file__).parent.resolve())

from data.metadata import my_version, git_version, git_url
from data.update import update_from_repo
import requests

# Get version from git
response = requests.get(git_version)
curr_vers = response.text.strip()

branch = 'main'

if my_version != curr_vers:

    from tkinter.messagebox import askyesno

    answer = askyesno(title='Update found',
        message=f"Your version is not up to date. Would you like to update it to version {curr_vers}")
        
    if answer:
        update_from_repo(my_version, curr_vers, git_url, main_path, branch, reg=registerOnConsole)

elif registerOnConsole:
    print(f"Version {curr_vers} is up to date")

# Start login
import frame.login as login
login.main_screen(main_path, registerOnConsole)