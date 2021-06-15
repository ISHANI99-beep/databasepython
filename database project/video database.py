import sqlite3

class dbclass:
    
    def __init__(self,filename):
        global conn
        try:
            conn = sqlite3.connect(f"db files/{filename}")
            # conn = sqlite3.connect(":memory:")
            with conn:
                cur = conn.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS videos 
                            (Id INTEGER AUTOINCREAMENT PRIMARY KEY DEFAULT 1,
                             name TEXT,
                             description TEXT)
                            """)
                print("Database Op")
        except:
            print("Unable to Create Database")

    def insert_data(self,id,name,description):
        try:
            with conn:
                cur=conn.cursor()
                cur.execute("INSERT INTO videos VALUES(?,?,?)",(id ,name,description))
                print("Data Inserted")
        except:
            print("Failed to insert data")

    def show_data(self):
        try:
            with conn:
                cur=conn.cursor()
                cur.execute("SELECT * FROM videos")
                if cur.fetchall()==[]:
                    print("Empty List")
                else:
                    cur.execute("SELECT * FROM videos")
                    for dataset in cur.fetchall():
                        print(f"id : {dataset[0]}",end="")
                        print(f"  |  name  :  {dataset[1]}",end="")
                        print(f"  |  description  :  {dataset[2]}",end="")
                        print()

        except:
            print("Failed to read data")

    def delete_data(self,name):
        try:
            with conn:
                cur=conn.cursor()
                cur.execute("DELETE FROM videos WHERE name= ? ",[name])
                print("Data deleted ")
        except:
            print("Failed to delete data")

    def update_data(self):
        try:
            with conn:
                cur=conn.cursor()
                id=input("Enter video id to be updated: ")
                cur.execute("SELECT * FROM videos WHERE Id=?",[id])
                n=cur.fetchall()[0][1]
                cur.execute("SELECT * FROM videos WHERE Id=?", [id])
                d = cur.fetchall()[0][2]
                if input("Do You Want to Chnage Video Name(Y/N) : ").lower() =='y':
                    n=input("Enter video name: ")
                if input("Do You Want to Chnage Video Description(Y/N) : ").lower() =='y':
                    d=input("Enter video Description : ")
                cur.execute("UPDATE videos SET name= ?, description= ? WHERE Id=? ",[n,d,id])
                print("Data updated ")
        except:
            print("Failed to update data")



def print_promp(db):
    print("\n\nCurrent Database:")
    db.show_data()
    print('\n//////////////////////////////////////////////////////////////////////')
    print("\nPLEASE CHOOSE FROM THE FOLLOWING : ")
    print("1 : Insert")
    print("2 : Delete")
    print("3 : Update")
    print("4 : Quit")
    return input()




###################################################################################################################################



db1=dbclass(input("Enter file to be Opened : "))
# db1=dbclass()
stop_loop=True


while stop_loop:
    
    try:
        a=int(print_promp(db1))
    except:
        print("\nWrong Input | Please Try Again")
        continue
    
    
    if a==1:
        id=input("Enter ID : ")
        name=input("Enter Name of the video : ")
        desc=input("Enter a short description for the video : ")
        db1.insert_data(id,name,desc)
    elif a==2:
        name=input("Enter Name of the video to be deleted : ")
        db1.delete_data(name)
    elif a==3:
        db1.update_data()
    elif a==4:
        stop_loop=False
    else:
        print("\nWrong Input | Please Enter Again")





