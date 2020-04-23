# CREATE TABLE userimages (
#     imageid int PRIMARY KEY,
#     name varchar(30) DEFAULT NULL,
#     rollno varchar(10) DEFAULT NULL,
#     temprollno varchar(10) DEFAULT NULL
# )

from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
import re

soup = BeautifulSoup(open("arjuna_Participants.html"), "html.parser") #open NFS, Arjuna, DSC++ html files if required
table = soup.findAll('table', attrs = {'class':'userinfobox'})

# Database Connection
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='teleuniv',
                                         user='root',
                                         password='root')
except Error as e:
    print("Error while connecting to MySQL", e)
    exit()

for i in range(len(table)):
    attr_dict = table[i].find('img', attrs = {'class':'userpicture'}).attrs
    img_id = attr_dict['src'].split('/')[4]
    name = attr_dict['alt']
    if img_id == "image.php":
        continue
    if len(table[i].find('div', attrs = {'class':'info'}))==6:
        rollno = table[i].find('div', attrs = {'class':'info'}).find('a').contents[0].split("@")[0]
        temprollno = "null"
        #rollno should be 17bd1a0437
        #temprollno might be 198472922
        if rollno != None and not re.match("([1-9][0-9]([A-Za-z0-9]){8}",rollno):
            temprollno = rollno
            rollno = "null"
    else:
        rollno = "null"
        temprollno = "null" #some other number which I don't know what it is.

    if connection.is_connected():
        cursor = connection.cursor()
        query = "select * from userimages where imageid = %s;"
        val = (img_id,)
        cursor.execute(query,val)
        row = cursor.fetchone()
        if not row: #user doesn't exist. Add directly
            query = "insert into userimages values (%s,%s,%s,%s);"
            val = (img_id,name,rollno,temprollno,)
            cursor.execute(query,val)
            print("insert success",name, img_id, rollno)
        else: #user already present
            if row[2] == "null" and row[3] != 'null' and rollno != "null" and str(row[0]) == img_id:
                query = "update userimages set rollno = %s, temprollno = %s where imageid = %s;"
                val = (rollno, temprollno, img_id,)
                cursor.execute(query, val)
                print("update success", name, img_id, rollno)

    else:
        print("connection fail")
        exit()
connection.commit()
