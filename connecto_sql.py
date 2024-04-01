import psycopg2

conn_details = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123456",
    port='5432'
)

cursor = conn_details.cursor()
list_data = '''
select * from product
LEFT JOIN sales
ON product.product_id = sales.product_id;
'''

cursor.execute(list_data)

conn_details.commit()
data = cursor.fetchall()
cursor.close()
conn_details.close()





