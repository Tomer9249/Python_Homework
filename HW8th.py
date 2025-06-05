
import sqlite3 #שימוש באס קיו לייט
#SQL
# CREATE TABLE customers( #פקודת יצירת טבלה, והשם שלה
#     id INT
#     name VARCHAR(50)
#     email VARCHAR(100)
# );

# #נשים לב שהסימן ; מסמל הפרדה בין פקודות, הוא קריטי אחרי כל פקודה. בנוסף, אין הבדל אם נכתוב באותיות קטנות או גדולות

# INSERT INTO customers (id, name, email) #פקודה להכנסת מידע לטבלה
# VALUES (1, 'John Doe', 'Johndoe@example.com'), (2,'Jane Doe', 'Jane@example.com'); #התוכן שנרצה להכניס

# SELECT name, email FROM customers; #פקודה לקבלת מידע ממקום מסוים בטבלה, במקרה הזה מטורים של שם ואימייל

# UPDATE customers #מציינת שאנחנו מעדכנים את הטבלה הספציפית הזו
# SET email= 'newemail@example.com' #משנים ספציפית את האימייל
# WHERE id=1; #היכן שהתז הוא 1

# DELETE FROM customers #מציין שאנחנו מוחקים מהטבלה הספציפית הזו
# WHERE id=1; #את השורה שבה התז הוא 1

conn = sqlite3.connect("Tomer.db") #מתחברים פה לדאטהבייס בשם שבמרכאות. אם הוא לא קיים, הוא יווצר אוטומטית

#example for creating and deleting data:
cursor=conn.cursor() #create a cursor object to execute SQL commands
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
name TEXT,
email TEXT
)
''') # execute an SQL command to create a table named "users"

cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe','john@example.com'),('Jane Doe', 'Jane@example.com')"); #insert a row of data into table
conn.commit() #Commits the changes to the database

#example for retrieving data:
cursor.execute("SELECT * FROM users") #Execute an SQL command to select data from the table
#כוכבית אומר הכל
rows=cursor.fetchall() #Fetch all the rows as a list of tuples
for row in rows: #Print the retrieved data
    print(row)
conn.close () #Close the connection

