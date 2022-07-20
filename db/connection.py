import mysql.connector
import data.secrets as secrets

secret_usr  = secrets.secret_usr
secret_pswd = secrets.secret_pswd
secret_host = secrets.secret_host
secret_port = secrets.secret_port
secret_db   = secrets.secret_db

db = mysql.connector.connect (
    user        = secret_usr,
    password    = secret_pswd,
    host        = secret_host,
    port        = secret_port,
    database    = secret_db
)