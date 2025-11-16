import psycopg2

conn = psycopg2.connect(
    database="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

cur = conn.cursor()

data = [
    {
        'patent_number': '10000000',
        'patent_date': '2018-06-19',
        'patent_title': 'Coherent LADAR using intra-pixel quadrature detection'
    },
    {
        'patent_number': '10000001',
        'patent_date': '2018-06-19',
        'patent_title': 'Injection molding machine and mold thickness control method'
    },
    {
        'patent_number': '10000002',
        'patent_date': '2018-06-19',
        'patent_title': 'Method for manufacturing polymer film and co-extruded film'
    },
    {
        'patent_number': '10000003',
        'patent_date': '2018-06-19',
        'patent_title': 'Method for producing a container from a thermoplastic'
    },
    {
        'patent_number': '10000004',
        'patent_date': '2018-06-19',
        'patent_title': 'Process of obtaining a double-oriented film, co-extruded, and of low thickness made by a three bubble process that at the time of being thermoformed provides a uniform thickness in the produced tray'
    }
]

for item in data:
    columns = ', '.join(item.keys())
    values = ', '.join(['%s'] * len(item))
    query = f"INSERT INTO your_table_name ({columns}) VALUES ({values})"
    cur.execute(query, tuple(item.values()))

conn.commit()

cur.close()
conn.close()
