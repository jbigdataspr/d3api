

import sys, psycopg2


    
conn = psycopg2.connect("dbname=polls user=postgres password=YW1974")
cur = conn.cursor()

sql = "COPY (SELECT * FROM polls_choice WHERE id<58) TO STDOUT WITH CSV DELIMITER ','"
with open("C:/temp/choice.csv", "w") as file:
    cur.copy_expert(sql, file)
cur.close()