import mysql.connector as my_sql

# Function to Create Database and Table
def Create():
    mydb=my_sql.connect(host="localhost", user="root", password="admin")
    cursor=mydb.cursor()
    cursor.execute("create database Project")
    cursor.execute("use project")
    cursor.execute('create table Diseases(Category varchar(50), Name varchar(50) primary key, Causes varchar(200), Symptoms varchar(200), Treatment varchar(200), Frequency decimal(4,2), Durantion varchar(30))')
    mydb.close()

# Function to Insert information
def Insert():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    n=int(input("Enter total number of entires"))
    for i in range(n):
        category=input("Enter Category:")
        name=input("Enter Name:")
        causes=input("Enter Causes:")
        symptoms=input("Enter symptoms")
        treatments=input("Enter Treatments:")
        frequency=input("Enter Frequency(Cases in millions per year):")
        duration=input("Enter Duration:")
        ins="insert into diseases values('%s','%s','%s','%s','%s',%s,'%s')"%(category,name,causes,symptoms,treatments,frequency,duration)
        cursor.execute(ins)
        mydb.commit()
    mydb.close()

# Functions to Display the Table
def Display():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    cursor.execute("select * from diseases")
    print("____________________________________________________________________________________________________________________________________________________________")
    print("\nCategory\t\tName\t\tCauses\t\tSymptoms\t\tTreatment\t\tFrequency\t\tDuration")
    print("____________________________________________________________________________________________________________________________________________________________")
    data=cursor.fetchall()
    for row in data:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])
    mydb.close()
def Displaycategory():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    category=input("Enter the Category")
    cursor.execute("select * from diseases where category='%s'"%(category))
    print("____________________________________________________________________________________________________________________________________________________________")
    print("\nCategory\t\tName\t\tCauses\t\tSymptoms\t\tTreatment\t\tFrequency\t\tDuration")
    print("____________________________________________________________________________________________________________________________________________________________")
    data=cursor.fetchall()
    for row in data:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])
    mydb.close()
def Displayname():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    name=input("Enter the Name")
    cursor.execute("select * from diseases where name='%s'"%(name))
    print("____________________________________________________________________________________________________________________________________________________________")
    print("\nCategory\t\tName\t\tCauses\t\tSymptoms\t\tTreatment\t\tFrequency\t\tDuration")
    print("____________________________________________________________________________________________________________________________________________________________")
    data=cursor.fetchall()
    for row in data:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])
    mydb.close()
def Displaycauses():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    causes=input("Enter the Causes")
    cursor.execute("select * from diseases where causes='%s'"%(causes))
    print("____________________________________________________________________________________________________________________________________________________________")
    print("\nCategory\t\tName\t\tCauses\t\tSymptoms\t\tTreatment\t\tFrequency\t\tDuration")
    print("____________________________________________________________________________________________________________________________________________________________")
    data=cursor.fetchall()
    for row in data:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])
    mydb.close()
def Displaysymptoms():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    symptoms=input("Enter the Symptoms")
    cursor.execute("select * from diseases where symptoms='%s'"%(symptoms))
    print("____________________________________________________________________________________________________________________________________________________________")
    print("\nCategory\t\tName\t\tCauses\t\tSymptoms\t\tTreatment\t\tFrequency\t\tDuration")
    print("____________________________________________________________________________________________________________________________________________________________")
    data=cursor.fetchall()
    for row in data:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])
    mydb.close()
def Displaytreatments():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    treatments=input("Enter the Treatments")
    cursor.execute("select * from diseases where treatments='%s'"%(treatments))
    print("____________________________________________________________________________________________________________________________________________________________")
    print("\nCategory\t\tName\t\tCauses\t\tSymptoms\t\tTreatment\t\tFrequency\t\tDuration")
    print("____________________________________________________________________________________________________________________________________________________________")
    data=cursor.fetchall()
    for row in data:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])
    mydb.close()
def Displayfrequency():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    frequency=input("Enter the Frequency")
    cursor.execute("select * from diseases where fequency=%s"%(fequency))
    print("____________________________________________________________________________________________________________________________________________________________")
    print("\nCategory\t\tName\t\tCauses\t\tSymptoms\t\tTreatment\t\tFrequency\t\tDuration")
    print("____________________________________________________________________________________________________________________________________________________________")
    data=cursor.fetchall()
    for row in data:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])
    mydb.close()
def Displayduration():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    duration=input("Enter the Duration")
    cursor.execute("select * from diseases where duration='%s'"%(duration))
    print("____________________________________________________________________________________________________________________________________________________________")
    print("\nCategory\t\tName\t\tCauses\t\tSymptoms\t\tTreatment\t\tFrequency\t\tDuration")
    print("____________________________________________________________________________________________________________________________________________________________")
    data=cursor.fetchall()
    for row in data:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])
    mydb.close()

# Functions to Update the table information
def Updatecategory():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    n=input("Enter name of the disease:")
    c=input("Enter updated category")
    ins="update diseases set category='%s' where name='%s'"%(c,n)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()
def Updatecauses():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    n=input("Enter name of the disease:")
    c=input("Enter updated causes")
    ins="update diseases set causes='%s' where name='%s'"%(c,n)
    cursor.execute(ins)
    mydb.commit()
def Updatesymptoms():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    n=input("Enter name of the disease:")
    s=input("Enter updated symptoms")
    ins="update diseases set symptoms='%s' where name='%s'"%(s,n)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()
def Updatetreatments():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    n=input("Enter name of the disease:")
    t=input("Enter updated treatments")
    ins="update diseases set treatments='%s' where name='%s'"%(t,n)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()
def Updatefrequency():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    n=input("Enter name of the disease:")
    f=input("Enter updated frequency")
    ins="update diseases set frequency='%s' where name='%s'"%(f,n)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()
def Updateduration():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    n=input("Enter name of the disease:")
    d=input("Enter updated duration")
    ins="update diseases set duration='%s' where name='%s'"%(d,n)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()

# Functions to Delete row information
def Deletecategory():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    c=input("Enter Category")
    ins="delete from diseases where category='%s'"%(c)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()
def Deletename():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    n=input("Enter Name")
    ins="delete from diseases where name='%s'"%(n)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()
def Deletecauses():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    c=input("Enter Causes")
    ins="delete from diseases where causes='%s'"%(c)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()
def Deletesymptoms():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    s=input("Enter Symptoms")
    ins="delete from diseases where symptoms='%s'"%(s)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()
def Deletetreatments():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    t=input("Enter Treatments")
    ins="delete from diseases where treatments='%s'"%(t)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()
def Deletefrequency():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    f=input("Enter Frequency")
    ins="delete from diseases where frequency=%s"%(f)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()
def Deleteduration():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    d=input("Enter Duration")
    ins="delete from diseases where duration='%s'"%(d)
    cursor.execute(ins)
    mydb.commit()
    mydb.close()

# Functions to Alter table
def Alteradd():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    col=input("Enter column name to be added")
    ty=input("Enter type of the column")
    ins="alter table diseases add "+col+""+ty
    cursor.execute(ins)
    mydb.close()
def Altermod():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    col1=input("Enter old column")
    col2=input("Enter new column")
    ty=input("Enter type of the column")
    ins="alter table diseases change "+col+""+col2+""+ty
    cursor.execute(ins)
    mydb.close()
def Alterrem():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    col=input("Enter column name")
    ins="alter table diseases drop "+col
    cursor.execute(ins)
    mydb.close()

# Functions to Drop Table and Drop Database
def Droptable():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    ins="drop table diseases"
    cursor.execute(ins)
    mydb.close()
def Dropdatabase():
    mydb=my_sql.connect(host="localhost", user="root", password="admin", database="project")
    cursor=mydb.cursor()
    ins="drop database project"
    cursor.execute(ins)
    mydb.close()

# Main Program
ch="y"
while ch=="y" or ch=="Y":
    print("1: Create\n\n2: Insert\n\n3: Display\n\n4: Update\n\n5: Delete\n\n6: Alter \n\n7: Drop\n")
    c=int(input("Enter your choice:"))
    if c==1:
        Create()
    elif c==2:
        Insert()
    elif c==3:
        print("1: Display full table\n\n 2: Display table based on Category\n\n 3: Display table based on Name\n\n 4: Display table based on Causes\n\n 5: Display table based on Symptoms\n\n 6: Display table basesd on Treatment\n\n 7: Display table based on Frequency\n\n 8: Display table based on Duration\n")
        ch=int(input("Enter your choice:"))
        if ch==1:
            Display()
        elif ch==2:
            Displaycategory()
        elif ch==3:
            Displayname()
        elif ch==4:
            Displaycauses()
        elif ch==5:
            Displaysymptoms()
        elif ch==6:
            Displaytreatments()
        elif ch==7:
            Displayfrequency()
        elif ch==8:
            Displayduration()
        else:
            print("Wrong input\n")
    elif c==4:
        print("1: Update Category\n\n 2: Update Causes\n\n 3: Update Symptoms\n\n 4: Update Treatments\n\n 5: Update Frequency\n\n 6: Update Duration\n")
        ch=int(input("Enter your choice:"))
        if ch==1:
            Updatecategory()
        elif ch==2:
            Updatecauses()
        elif ch==3:
            Updatesymptoms()
        elif ch==4:
            Updatetreatments()
        elif ch==5:
            Updatefrequency()
        elif ch==6:
            Updateduration()
        else:
            print("Wrong input\n")
    elif c==5:
        print("1: Delete by Category\n\n2: Delete by Name\n\n3: Delete by Causes\n\n4: Delete by Symptoms\n\n5: Delete by Treatments\n\n6: Delete by Frequency\n\n7: Delete by Duration\n")
        ch=int(input("Enter your choice:"))
        if ch==1:
            Deletecategory()
        elif ch==2:
            Deletename()
        elif ch==3:
            Deletecauses()
        elif ch==4:
            Deletesymptoms()
        elif ch==5:
            Deletetreatments()
        elif ch==6:
            Deletefrequency()
        elif ch==7:
            Deleteduration()
        else:
            print("Wrong input\n")
    elif c==6:
        print("1: Add new column\n\n2: Modify existing column\n\n3: Remove existing column\n")
        ch=int(input("Enter your choice:"))
        if ch==1:
            Alteradd()
        elif ch==2:
            Altermod()
        elif ch==3:
            Alterrem()
        else:
            print("Wrong input\n")
    elif c==7:
        print("1: Drop table\n\n2: Drop database\n")
        ch=int(input("Enter your choice:"))
        if ch==1:
            Droptable()
        elif ch==2:
            Dropdatabase()
        else:
            print("Wrong input\n")
    else:
        print("Wrong input\n")
    ch=input("Do you want to continue?[Y/N]\n")
