import json

current_dir = "\\".join(__file__.split('\\')[0:-1]) + "\\metadata.json"

f = open(current_dir)
json_meta = json.load(f)

app_title = json_meta['project_name']
my_version = json_meta['my_version']
git_url = json_meta['git_url']
git_version = json_meta['git_version']

f.close()