# :book:__READ THIS IF YOU ARE NOT FAMILIARIZED WITH FERNET__:book:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:point_right: https://cryptography.io/en/latest/fernet/

### __HOW DOES IT WORK AND HOW YOU CAN RUN IT?__

1. Create a file called ```*optional name (it can be empty)*.env``` on folder ```./data/.env```
2. Now add this values inside
```env
[SQL_CFG]
-USR = "root/127.0.0.1 or your ip username"
-PSWD = "password"
-HOST = "localhost/http(s)://domain.ext"
-PORT = "port/3306 (MySQL)"
-DB = "pylox_db {modify it from all files if you wish to change it}"

[ENCODING]
-PSWD_TOKEN = "{generate your own with with Fernet.generate_key()}"
```
3. Launch your SQL database and make sure you have created your table
4. Run the file "__main__.py"

### __THINGS TO DO__
- [x] Create a python CRUD with SQL
- [x] Create a functional login with local storage (metadata.json)
<br /><br />
![](https://progress-bar.dev/5/?title=Create%20the%20main%20page)

- [ ] Create an instant messaging
- [ ] Host a remote server
- [ ] Release the v1.0

I'm still an amateur at Python so...<br />
If you can help me to improve this project it would be an honor :grin:<br />
Much appreciated for trying this project :wave:
