from sqlite3 import Error, connect


def Mahsulotlar():
    try:
        con = connect("mahsulot.db")
        cursor = con.cursor()
        cursor.execute("select * from mahsulot")
        information = cursor.fetchall()
        return information
    except (Exception, Error) as error:
        print("Wrong", error)
    finally:
        if con:
            cursor.close()
            con.close()



def karz(user_id):
    try:
        con = connect("mahsulot.db")
        cursor = con.cursor()
        cursor.execute("select * from karzinka where user_id = ?", (user_id,))
        information = cursor.fetchall()
        return information
    except (Exception, Error) as error:
        print("Wrong", error)
    finally:
        if con:
            cursor.close()
            con.close()


def add(user_id, name, username):
    try:
        con = connect("mahsulot.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO users(user_id, name, username) values (?, ?, ?)", (user_id, name, username))
        con.commit()
        return "done"
    except (Exception, Error) as error:
        print("Wrong", error)
    finally:
        if con:
            cursor.close()
            con.close()



def MaxsulotlarAdds(user_id, name, price, count):
    try:
        con = connect("mahsulot.db")
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO karzinka(user_id, name, price, count) values(?, ?, ?, ?) 
            """, (user_id, name, price, count))
        con.commit()
        return "mission completed"
    except (Exception, Error) as error:
        print("Wrong", error)
    finally:
        if con:
            cursor.close()
            con.close()




# def MahsulotAdd(name, price, image, dec):
#     try:
#         con = connect("mahsulot.db")
#         cursor = con.cursor()
#         cursor.execute("""
#             INSERT INTO mahsulot(name, price, image, dec) values(?, ?, ?, ?)
#             """, (name, price, image, dec))
#         con.commit()
#         return "bajarildi"
#     except (Exception, Error) as error:
#         print("Wrong", error)
#     finally:
#         if con:
#             cursor.close()
#             con.close()

# name = input("Name: ")
# price = float(input("Price: "))
# image = input("Image: ")
# dec = input("About: ")
# print(MahsulotAdd(name, price, image, dec))











# try:
#     con = connect("mahsulot.db")
#     cursor = con.cursor()
#     cursor.execute("""
#             CREATE TABLE karzinka(
#                    id integer primary key not null,
#                    user_id int unique,
#                    name text not null,
#                    price real not null,
#                    count int not null
#                    );
#             """)
#     con.commit()
# except (Exception, Error) as error:
#     print("Wrong", error)
# finally:
#     if con:
#         cursor.close()
#         con.close()





# try:
#     con = connect("mahsulot.db")
#     cursor = con.cursor()
#     cursor.execute("""
#             CREATE TABLE mahsulot(
#                    id integer primary key not null,
#                    name text not null,
#                    price real not null,
#                    image text not null,
#                    dec text not null
#                    );
#            """)
#     con.commit()
# except (Exception, Error) as error:
#     print("Wrong", error)
# finally:
#     if con:
#         cursor.close()
#         con.close()








# try:
#     con = connect("mahsulot.db")
#     cursor = con.cursor()
#     cursor.execute("""
#            CREATE TABLE users(
#                    id integer primary key not null,
#                    user_id int unique,
#                    name text not null,
#                    username text
#                    );  
#            """)
#     con.commit()
# except (Exception, Error) as error:
#     print("Wrong", error)
# finally:
#     if con:
#         cursor.close()
#         con.close() 
