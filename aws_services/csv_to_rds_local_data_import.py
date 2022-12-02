from sqlalchemy import create_engine
import pandas as pd
name = "database/exam_table.csv"
user='admin'
db_password='Admin123'
endpoint='database-1.ccegryjtyfli.us-east-1.rds.amazonaws.com'
port='3306'
db_name='pearview'

#
df = pd.read_csv(name)
mydb = create_engine('mysql+pymysql://' + user + ':' + db_password + '@' + endpoint + ':' + port + '/' + db_name,echo=False)
df.to_sql(name="exam", con=mydb, if_exists='replace', index=False)
print("Done")