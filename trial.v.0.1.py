import os
import datetime
import magic
import sqlite3

conn = sqlite3.connect('/media/sf_Ortak/Kenan.Bolat/SearchQuery.db')
conn.text_factory = str
c = conn.cursor()
table_name = 'SharedSearch'
sql = 'Create Table if not exists ' +table_name + ' (`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 	`USER_NAME`	TEXT, 	`File_Type`	TEXT, 	`File_Exte`	TEXT, 	`Mime_Name`	TEXT, 	`Mime_Type`	TEXT, 	`File_Location`	TEXT, 	`File_Size`	TEXT, 	`Date_Inserted`	TEXT, 	`Date_Deleted`	INTEGER, UNIQUE (File_Location) ON CONFLICT REPLACE);'
c.execute(sql)

START = datetime.datetime.now()
path = "/media/sf_Ortak"
counter = 0
res = []

for root,dir,files in os.walk(path):
    temp = []
    try:
        for file in files:
            temp =os.path.join(root,file)
            user_name  = temp.split('/')[3]
            file_exte  = file.split('.')[-1]
            date_inserted = datetime.datetime.now().strftime('%y%m%d%H%M')
            file_size = os.path.getsize(temp)
            mime = magic.open(magic.MAGIC_MIME)
            mime.load()
            mime_name = mime.file(os.path.join(root, file)).split(";")[0]
            mime_type = mime_name.split('/')[0]
            file_location = '/'.join((temp.split('/')[3:]))
            counter +=1
            temp_2 = [user_name, file_exte, mime_name,mime_type, file_location,str(file_size),date_inserted]
            # res.append()
            c.executemany(
                "INSERT INTO SharedSearch (USER_NAME, File_Exte, Mime_Name,Mime_Type,File_Location,File_Size,Date_Inserted) values(?,?,?,?,?,?,?)",
                [tuple(temp_2)])
            conn.commit()

    except BaseException as BE:
        print BE.message
        print temp
        continue


    # if counter > 2000:
    #     break

conn.close()
END = datetime.datetime.now()
DURATION = END-START;
print DURATION

