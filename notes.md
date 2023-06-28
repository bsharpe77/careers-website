Lorem Ipsum: https://loremipsum.io
Free Stock Images: https://unsplash.com/
Free wireframe tool: https://excalidraw.com/
Bootstrap: https://getbootstrap.com/
Video: https://youtu.be/yBDHkveJUf4?t=4112
  For Wednesday: Chapter 1.6
Mailto link builder: https://mailtolink.me/
Cloud Hosting: render.com - https://render.com/docs/deploy-flask
DB: https://planetscale.com/
  database: joviancareers
  username: 44vir73y6f2fwfuu3sye
  host: aws.connect.psdb.cloud
  password: pscale_pw_1cfgOges2VpnvCMjsspmhrzjmwIXfsq9xMhdP3u2nvV
My SQL Workbench App for DB management
https://www.sqlalchemy.org/ - to connect app to DB
  https://docs.sqlalchemy.org/en/20/intro.html#installation
  https://docs.sqlalchemy.org/en/20/tutorial/engine.html




with engine.connect() as conn:
  result = conn.execute(text("select * FROM jobs"))
  result_all = result.all()
  first_result = result_all
  for row in result_all:
    print(type(row))

for row in result_all:
  if 'location' in row._mapping:
    print("Column 'location': %s" % row._mapping['location'])


