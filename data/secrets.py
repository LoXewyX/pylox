# Secrets
import os
from dotenv import load_dotenv

load_dotenv()

# SQL_CFG
secret_usr      = os.getenv( "USR",     "SQL_CFG"   )
secret_pswd     = os.getenv( "PSWD",    "SQL_CFG"   )
secret_host     = os.getenv( "HOST",    "SQL_CFG"   )
secret_port     = os.getenv( "PORT",    "SQL_CFG"   )
secret_db       = os.getenv( "DB",      "SQL_CFG"   )

# GITHUB
github_usr      = os.getenv( "GIT_USR",     "GITHUB"    ) 
github_token    = os.getenv( "GIT_TOKEN",   "GITHUB"    )

# ENCODING
pswd_token      = os.getenv( "PSWD_TOKEN",  "ENCODING"  )