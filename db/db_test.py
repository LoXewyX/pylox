import db.db_config as dfg
from utils.ip import get_public_ip as ip

def create_essentials(dropIfExists = False, reg = False):
    dfg.create_table(
        "usrdata",
        f"""
        `id_usr` INT NOT NULL AUTO_INCREMENT,
        `id_contacts` VARCHAR(45) NOT NULL DEFAULT 0,
        `id_messages` VARCHAR(45) NOT NULL DEFAULT 0,
        `username` VARCHAR(45) NOT NULL,
        `password` VARCHAR(255) NOT NULL,
        `ip` VARCHAR(39) NOT NULL DEFAULT '{ip()}',
        `image` VARCHAR(45) NULL DEFAULT 'noimage.png',
        `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`id_usr`, `id_contacts`, `id_messages`)
        """,
        dropIfExists = dropIfExists,
        reg = reg
    )