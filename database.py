from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row)
    return jobs


#fixed from tutorial code -- had to change the way the variable was handled (id) and change the return statement
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = " + id))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]


#had to refactor how this collected and submitted the variables from the form
def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    values = job_id + ",'" + data['full_name'] + "','" + data[
      'email'] + "','" + data['linkedIn'] + "','" + data[
        'education'] + "','" + data['work_experience'] + "','" + data[
          'resume_url'] + "'"
    query = text(
      "INSERT INTO applications (job_id,full_name,email,linkedin_url,education,work_experience,resume_url) VALUES ("
      + values + ")")

    conn.execute(query)
