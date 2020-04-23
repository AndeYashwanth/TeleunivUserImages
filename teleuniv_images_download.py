import requests
import concurrent.futures
import mysql.connector
from mysql.connector import Error

arr = []
username = ''
password = ''
#if userids are available in sql table
# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='teleuniv',
#                                          user='root',
#                                          password='root')
#     if connection.is_connected():
#         cursor = connection.cursor()
#         query = "select imageid from userimages;"
#         cursor.execute(query)
#         arr = [item[0] for item in cursor.fetchall()]

# except Error as e:
#     print("Error while connecting to MySQL", e)
#     exit()

with requests.Session() as c:
    payload = {'username': username, 'password': password}
    r = c.post("https://teleuniv.net/login/index.php", data = payload)

    def download_image(num):
        img_bytes = c.get(f"https://teleuniv.net/pluginfile.php/{num}/user/icon/universo/f3").content
        img_name = f"images/{num}.jpg"
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
            print(f'{num} was downloaded...')
    with concurrent.futures.ThreadPoolExecutor() as executor:
        arr=[i for i in range(909,22000)] #there are no images below 909 and above 22000
        executor.map(download_image, arr)
