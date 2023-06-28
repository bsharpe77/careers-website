from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://44vir73y6f2fwfuu3sye:pscale_pw_1cfgOges2VpnvCMjsspmhrzjmwIXfsq9xMhdP3u2nvV@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

