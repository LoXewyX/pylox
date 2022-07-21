## :book:__READ THIS IF YOU ARE NOT FAMILIARIZED WITH FERNET__:book:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:point_right: https://cryptography.io/en/latest/fernet/

### __HOW DOES IT WORK AND HOW YOU CAN RUN IT?__
1. Create a file called ```*optional name (it can be empty)*.env``` on folder ```./data/.env```
2. Now add this values inside
```env dotenv.env
[SQL_CFG]
USR = "root || myremoteusr"
PSWD = "mypassword"
HOST = "localhost || 127.0.0.1 || http(s)://domain.ext"
PORT = "myport || 3306 (MySQL)"
DB = "pylox_db {modify it from all files if you wish to change it} || my_db"

[ENCODING]
PSWD_TOKEN = "generate your own token with Fernet.generate_key()"
```
3. Launch your SQL database and make sure you have created your table
4. Run the file "__main__.py"

### __THINGS TO DO__
- [x] Create a python *CRUD* with SQL
- [x] Create a functional login with local storage \*located in ```./data/metadata.json```\*<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](https://progress-bar.dev/5/?title=Create%20the%20main%20page)

- [ ] Create an instant messaging
- [ ] Host a remote server
- [ ] Release the v1.0

I'm still an amateur at Python so...<br />
If you can help me to improve this project it would be an honor :grin:<br />
Much appreciated for trying this project :wave:<br />

<!--My Watermark-->
<p align="center">
  <img src="https://user-images.githubusercontent.com/86871709/179967999-26052aff-0208-48bd-a051-32c8493f4675.png" width=250 height=250
  style="border: 10px solid black; border-radius: 50%; overflow: hidden"/>
</p>
