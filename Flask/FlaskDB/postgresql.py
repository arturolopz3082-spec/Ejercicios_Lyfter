import psycopg2


connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="user",
    dbname="postgres"
)

def format_user(user_record):
    return{
        "id": user_record[0],
        "username": user_record[1],
        "email": user_record[2],
        "first_name": user_record[3],
    }

print("Connected to the database")

request_body = {
    "full_name": "José Antonio Aguilar",
    "email": "joseaa154@gmail.com",
    "password": "dafasdafas"
}

full_name = request_body.get("full_name")
email = request_body.get("email")
password = request_body.get("password")

cursor = connection.cursor()

cursor.execute(
    f"INSERT INTO lyfter_duad.users (full_name, email, password) VALUES ('{full_name}', '{email}', '{password}');"
)

print("Query execute")

connection.commit()
print("Connection changes committed")