import psycopg2;


conn = psycopg2.connect(database="Test_DB", user="postgres", password="password", host="database-2.cl1y0mpjd96j.us-east-1.rds.amazonaws.com", port="5432");
cur = conn.cursor();

filename = 'company2.csv';
fhandle = open(filename,'r');


for line in fhandle:
    data = line.split(',');
    insert_statement = "Insert Into company Values ("+data[0]+",'"+data[1]+"',"+data[2]+",'"+data[3]+"',"+data[4]+");";
    cur.execute(insert_statement);
    conn.commit();

print('Process Terminated');

conn.close();
fhandle.close();

