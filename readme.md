__HOW DOES IT WORK AND HOW I CAN RUN IT?__

1. Create a file called "{optional name, it can be empty}.env" on folder "./data/.env"
2. Now add this values inside

[SQL_CFG]
USR = "root/127.0.0.1 or your ip username"
PSWD = "password"
HOST = "localhost/http(s)://domain.ext"
PORT = "port/3306 (MySQL)"
DB = "pylox_db {modify it from all files if you wish to change it}"

[ENCODING]
# __READ THIS IF YOUR NOT FAMILIARIZED WITH FERNET__
# https://cryptography.io/en/latest/fernet/
PSWD_TOKEN = "{generate your own with with Fernet.generate_key()}"

3. Launch your SQL database and make sure you have created your table
4. Run the file "__main__.py"

I'm still an amateur at Python so if you can help me to improve this project it would be an honor
Thank you for trying this project
