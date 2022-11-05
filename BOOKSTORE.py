import mysql.connector
import pickle
import os
from datetime import datetime
from datetime import timedelta
con=mysql.connector.connect(host="localhost<host>",user="root<user>",passwd="<password>",database="bookstore<database>")
cur=con.cursor()
def admin():
    def passwordd():
        pp=0
        def pv(pp):
            attampts=3
            p=open("pass.dat","rb")
            i=""
            try:
                while True:
                    mm=pickle.load(p)
                    i=mm[0]
            except EOFError:
                print("")
            while True:    
                a=input("ENTER PASSWORD:")
                c=str(hash(a))
                if i==c:
                    print("correct password")
                    pp=1
                    p.close()
                    break
                else:  
                    print("incorrect password")
                    print("You have "+str(attampts)+str(" attempts left"))
                    attampts=attampts-1
                    if attampts==0:
                        p.close()
                        break
        def pc():
            attampts=3
            a=input("ENTER PASSWORD:")
            p=open("pass.dat","ab+")
            i=""
            try:
                while True:
                    mm=pickle.load(p)
                    i=mm[0]
            except EOFError:
                print("")
            if i==a:
                print("correct password")
                b=open("temp.dat","wb")
                while True:
                    n=input("Enter new password:")
                    m=input("Conferm new password:")
                    if n==m:
                        pickle.dump(str(hash(n)),b)
                        b.close()
                        p.close()
                        os.remove("pass.dat")
                        os.rename("temp.dat","pass.dat")
                        print("Password changed")
                        break
                    else:
                        print("Password not matched")
                        h=input("Want to Try again?[y/n]")
                        if h=="N" or h=="n":
                            break
            else:  
                print("incorrect password")
                print("You have"+str(attampts)+str("attempts left"))
                attampts=attampts-1
                if attampts==0:
                    p.close()
        while True:
            print("1.PASSWERD VERIFY")
            print("2.PASSWROD CHANGE")
            m=int(input("ENTER YOUR CHOICE:"))
            if m==1:
                pv(pp)
            if m==2:
                pc()
                break
            else:
                break
        return(pp)
    passe=passwordd()
    if passe==1:    
        def listofbooks():
                cur.execute("""select * from booklist;""")
                r=cur.fetchall()
                print("+--------------------------------------------------------------------------------------------------------------+")
                print("|SLNo. |BOOKNAME                      |AUTHOR's NAME                 |GENRE                         |BOOKID|QTY|")
                print("+--------------------------------------------------------------------------------------------------------------+")
                s="|{:^6}|{:^30}|{:^30}|{:^30}|{:^6}|{:^3}|"
                l=[]
                for i in r:
                    for j in i:
                        l.append(j)
                    print(s.format(l[0],l[1],l[2],l[3],l[4],l[5]))
                    l=[]
                    print("+--------------------------------------------------------------------------------------------------------------+")
        def listofbookborrowers():
                cur.execute("""select * from borrowers;""")
                r=cur.fetchall()
                print("+----------------------------------------------------------------------------------------------------------------------------------------------------+")
                print("|slno.|NAME                          |PHONE NO. |ADDRESS                       |BOOKNAME                      |BOOK ID.|DATE OF BORROW|DATE OF RETURN|")
                print("+----------------------------------------------------------------------------------------------------------------------------------------------------+")
                s="|{:^5}|{:^30}|{:^10}|{:^30}|{:^30}|{:^8}|{:^14}|{:^14}|"
                l=[]
                for i in r:
                    for j in i:
                        l.append(str(j))
                    print(s.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7]))
                    l=[]
                    print("+----------------------------------------------------------------------------------------------------------------------------------------------------+")
        def addbook():
                while True:
                    sl=int(input("ENTER THE SL NO.:"))
                    b=input("ENTER THE BOOKNAME:")
                    a=input("ENTER THE AUTHOR:")
                    g=input("ENTER THE GENRE:")
                    i=input("ENTER THE BOOKID:")
                    q=input("ENTER THE QUANTITY:")
                    s="""insert into booklist values(%s,%s,%s,%s,%s,%s);"""
                    l=[sl,b,a,g,i,q]
                    cur.execute(s,l)
                    n=input("want to save?[y/n]")
                    if n=="y" or n=="Y":
                        con.commit()
                    k=input("want to enter more?[y/n]")
                    if k=="N" or k=="n":
                        break            
        while True:
                print("+-----------------------------+")
                print("|          WELCOME            |")
                print("|         ADMIN MENU          |")
                print("|1.LIST OF THE BOOKS          |")
                print("|2.LIST OF BOOK BORROWERS     |")
                print("|3.ADD BOOKS TO THE BOOKLIST  |")
                print("|4.EXIT TO CHOICES            |")
                print("+-----------------------------+")
                n=int(input("ENTER YOUR CHOICE:"))
                if n==4:
                    break
                elif n==1:
                    listofbooks()
                elif n==2:
                    listofbookborrowers()
                elif n==3:
                    addbook()
                else:
                    print("INVALID CHOICE")
    else:
        print("INCORRECT PASSWORD")
def bookborrower(): #bookborrowermenu
    while True:
        print("+--------------------------------------------+")
        print("|                 WELCOME                    |")
        print("|           BOOK BORROWER's CHOICE           |")
        print("|1.LIST OF THE BOOKS CAN BE BORROWED         |")
        print("|2.EXIT TO CHOICES                           |")
        print("+--------------------------------------------+")
        n=int(input("ENTER YOUR CHOICE:"))
        def bookshowcase():
            def b1():
                cur.execute("""select * from booklist;""")
                m=cur.fetchall()
                print("+--------------------------------------------------------------------------------------------------------------+")
                print("|SLNo. |BOOKNAME                      |AUTHOR's NAME                 |GENRE                         |BOOKID|QTY|")
                print("+--------------------------------------------------------------------------------------------------------------+")
                s="|{:^6}|{:^30}|{:^30}|{:^30}|{:^6}|{:^3}|"
                l=[]
                for i in m:
                    for j in i:
                        l.append(j)
                    print(s.format(l[0],l[1],l[2],l[3],l[4],l[5]))
                    l=[]
                    print("+--------------------------------------------------------------------------------------------------------------+")
                print()
                print("########################################################")
                print("# THE BOOKS WITH QUANTITY 0 ARE NOT AVAILABLE FOR NOW  #")
                print("# CHOOSE BY BOOKID                                     #")
                print("# A BORROWER CAN BORROW ONE BOOK AT A TIME             #")
                print("########################################################")
                list=[]
                while True:
                    book=input("ENTER BOOKID TO BORROW:")
                    list.append(book)
                    n=input("WANT TO CHANGE THE BOOK?[Y/N]:")
                    if n=="n" or n=="N":
                        break
                def bookfinal(list):
                    def updateborrowerlist(h):
                        qry="""select slno from borrowers;"""
                        cur.execute(qry)
                        sl=cur.fetchall()
                        c=0
                        for i in sl:
                            for j in i:
                                c=j
                        slno=c+1
                        name=input("ENTER YOUR NAME:")
                        phone=int(input("ENTER PHONE NO(10 DIGITS):"))
                        addr=input("ENTER YOUR ADDRESS(30 LETTERS LIMIT):")
                        bookn,bookid=h[1],h[4]
                        d1=str(datetime.now())
                        d2=d1.split()
                        date=d2[0]
                        w1=str(datetime.now() + timedelta(days=15))
                        w2=w1.split(" ")
                        w=w2[0] 
                        qry2="""insert into borrowers values(%s,%s,%s,%s,%s,%s,%s,%s);"""
                        l3=[slno,name,phone,addr,bookn,bookid,date,w]
                        cur.execute(qry2,l3)
                        con.commit()
                        print("|_________________________________________________________________|")
                        print("+-----------------------------------------------------------------+")
                        print("|                 BOOK STORE                                      |")
                        print("|                                                                 |")
                        print("|NAME:{:^30}   DATE:{:^10}            |".format(name,date))
                        print("|BOOKID:{:^5}                                                     |".format(bookid))
                        print("|BOOKBORROWED:{:^30}                      |".format(bookn))
                        print("|                                                                 |")
                        print("|DATE OF RETURN:{:^10}                                        |".format(w))
                        print("|*AFTER COMPLITION OF RETURNING DATE A FINE OF Rs.15 WILL BE      |")
                        print("|CHARGED PER DAY.                                                 |")
                        print("|*INCASE OF BOOK LOST OR DAMAGE THE FULL PRICE OF BOOK WILL BE    |")
                        print("|CHARGED AS FINE                                                  |")
                        print("+-----------------------------------------------------------------+")
                        print("|_________________________________________________________________|")
                    while True:    
                        qry="""select * from booklist where bookid=%s;"""
                        print("THE BOOK YOU CHOOSE:")
                        h=[]
                        for l in list:
                            cur.execute(qry,[str(l)])
                            k=cur.fetchall()
                            for j in k:
                                for o in j:
                                    h.append(o)
                                    print(o,end=" | ")
                                print()
                        ll=input("DO YOU WANT TO CONFIRM[y/n]")
                        if ll=="n" or ll=="N":
                            list=[]
                            break
                        elif ll=="Y" or ll=="y":
                            updateborrowerlist(h)
                            break
                        else:
                            print("INVALID CHOICE")
                bookfinal(list)
            def b2():
                g=input("ENTER GENRE:")
                cur.execute("""select * from booklist where genre like "{}%";""".format(g))
                m=cur.fetchall()
                print("+--------------------------------------------------------------------------------------------------------------+")
                print("|SLNo. |BOOKNAME                      |AUTHOR's NAME                 |GENRE                         |BOOKID|QTY|")
                print("+--------------------------------------------------------------------------------------------------------------+")
                s="|{:^6}|{:^30}|{:^30}|{:^30}|{:^6}|{:^3}|"
                l=[]
                for i in m:
                    for j in i:
                        l.append(j)
                    print(s.format(l[0],l[1],l[2],l[3],l[4],l[5]))
                    l=[]
                    print("+--------------------------------------------------------------------------------------------------------------+")
                print()
                print("########################################################")
                print("# THE BOOKS WITH QUANTITY 0 ARE NOT AVAILABLE FOR NOW  #")
                print("# CHOOSE BY BOOKID                                     #")
                print("# A BORROWER CAN BORROW ONE BOOK AT A TIME             #")
                print("########################################################")
                list=[]
                while True:
                    book=input("ENTER BOOKID TO BORROW:")
                    list.append(book)
                    n=input("WANT TO CHANGE THE BOOK?[Y/N]:")
                    if n=="n" or n=="N":
                        break
                def bookfinal(list):
                    def updateborrowerlist(h):
                        qry="""select slno from borrowers;"""
                        cur.execute(qry)
                        sl=cur.fetchall()
                        c=0
                        for i in sl:
                            for j in i:
                                c=j
                        slno=c+1
                        name=input("ENTER YOUR NAME:")
                        phone=int(input("ENTER PHONE NO(10 DIGITS):"))
                        addr=input("ENTER YOUR ADDRESS(30 LETTERS LIMIT):")
                        bookn,bookid=h[1],h[4]
                        d1=str(datetime.now())
                        d2=d1.split()
                        date=d2[0]
                        w1=str(datetime.now() + timedelta(days=15))
                        w2=w1.split(" ")
                        w=w2[0]
                        qry2="""insert into borrowers values(%s,%s,%s,%s,%s,%s,%s,%s);"""
                        l3=[slno,name,phone,addr,bookn,bookid,date,w]
                        cur.execute(qry2,l3)
                        con.commit()
                        print("|_________________________________________________________________|")
                        print("+-----------------------------------------------------------------+")
                        print("|                 BOOK STORE                                      |")
                        print("|                                                                 |")
                        print("|NAME:{:^30}   DATE:{:^10}            |".format(name,date))
                        print("|BOOKID:{:^5}                                                     |".format(bookid))
                        print("|BOOKBORROWED:{:^30}                      |".format(bookn))
                        print("|                                                                 |")
                        print("|DATE OF RETURN:{:^10}                                        |".format(w))
                        print("|*AFTER COMPLITION OF RETURNING DATE A FINE OF Rs.15 WILL BE      |")
                        print("|CHARGED PER DAY.                                                 |")
                        print("|*INCASE OF BOOK LOST OR DAMAGE THE FULL PRICE OF BOOK WILL BE    |")
                        print("|CHARGED AS FINE                                                  |")
                        print("+-----------------------------------------------------------------+")
                        print("|_________________________________________________________________|")
                    while True:    
                        qry="""select * from booklist where bookid=%s;"""
                        print("THE BOOK YOU CHOOSE:")
                        h=[]
                        for l in list:
                            cur.execute(qry,[str(l)])
                            k=cur.fetchall()
                            for j in k:
                                for o in j:
                                    h.append(o)
                                    print(o,end=" | ")
                                print()
                        ll=input("DO YOU WANT TO CONFIRM[y/n]")
                        if ll=="n" or ll=="N":
                            list=[]
                            break
                        elif ll=="Y" or ll=="y":
                            updateborrowerlist(h)
                            break
                        else:
                            print("INVALID CHOICE")
                bookfinal(list)
            def b3():
                g=input("ENTER BOOKNAME:")
                cur.execute("""select * from booklist where bookname like "{}%";""".format(g))
                m=cur.fetchall()
                print("+--------------------------------------------------------------------------------------------------------------+")
                print("|SLNo. |BOOKNAME                      |AUTHOR's NAME                 |GENRE                         |BOOKID|QTY|")
                print("+--------------------------------------------------------------------------------------------------------------+")
                s="|{:^6}|{:^30}|{:^30}|{:^30}|{:^6}|{:^3}|"
                l=[]
                for i in m:
                    for j in i:
                        l.append(j)
                    print(s.format(l[0],l[1],l[2],l[3],l[4],l[5]))
                    l=[]
                    print("+--------------------------------------------------------------------------------------------------------------+")
                print()
                print("########################################################")
                print("# THE BOOKS WITH QUANTITY 0 ARE NOT AVAILABLE FOR NOW  #")
                print("# CHOOSE BY BOOKID                                     #")
                print("# A BORROWER CAN BORROW ONE BOOK AT A TIME             #")
                print("########################################################")
                list=[]
                if len(list)!=0:
                    while True:
                        book=input("ENTER BOOKID TO BORROW:")
                        list.append(book)
                        n=input("WANT TO CHANGE THE BOOK?[Y/N]:")
                        if n=="n" or n=="N":
                            break
                    def bookfinal(list):
                        def updateborrowerlist(h):
                            qry="""select slno from borrowers;"""
                            cur.execute(qry)
                            sl=cur.fetchall()
                            c=0
                            for i in sl:
                                for j in i:
                                    c=j
                            slno=c+1
                            name=input("ENTER YOUR NAME:")
                            phone=int(input("ENTER PHONE NO(10 DIGITS):"))
                            addr=input("ENTER YOUR ADDRESS(30 LETTERS LIMIT):")
                            bookn,bookid=h[1],h[4]
                            d1=str(datetime.now())
                            d2=d1.split()
                            date=d2[0]
                            w1=str(datetime.now() + timedelta(days=15))
                            w2=w1.split(" ")
                            w=w2[0]
                            qry2="""insert into borrowers values(%s,%s,%s,%s,%s,%s,%s,%s);"""
                            l3=[slno,name,phone,addr,bookn,bookid,date,w]
                            cur.execute(qry2,l3)
                            con.commit()
                            print("|_________________________________________________________________|")
                            print("+-----------------------------------------------------------------+")
                            print("|                 BOOK STORE                                      |")
                            print("|                                                                 |")
                            print("|NAME:{:^30}   DATE:{:^10}            |".format(name,date))
                            print("|BOOKID:{:^5}                                                     |".format(bookid))
                            print("|BOOKBORROWED:{:^30}                      |".format(bookn))
                            print("|                                                                 |")
                            print("|DATE OF RETURN:{:^10}                                        |".format(w))
                            print("|*AFTER COMPLITION OF RETURNING DATE A FINE OF Rs.15 WILL BE      |")
                            print("|CHARGED PER DAY.                                                 |")
                            print("|*INCASE OF BOOK LOST OR DAMAGE THE FULL PRICE OF BOOK WILL BE    |")
                            print("|CHARGED AS FINE                                                  |")
                            print("+-----------------------------------------------------------------+")
                            print("|_________________________________________________________________|")
                        while True:    
                            qry="""select * from booklist where bookid=%s;"""
                            print("THE BOOK YOU CHOOSE:")
                            h=[]
                            for l in list:
                                cur.execute(qry,[str(l)])
                                k=cur.fetchall()
                                for j in k:
                                    for o in j:
                                        h.append(o)
                                        print(o,end=" | ")
                                    print()
                            ll=input("DO YOU WANT TO CONFIRM[y/n]")
                            if ll=="n" or ll=="N":
                                list=[]
                                break
                            elif ll=="Y" or ll=="y":
                                updateborrowerlist(h)
                                break
                            else:
                                print("INVALID CHOICE")
                else:
                    print("NO BOOK FOUND PLEASE TRY AGAIN")
                bookfinal(list)
            while True:
                print("+-------------------------------------+")
                print("|1.ALL BOOKS                          |")
                print("|2.FILTER BY GENRE                    |")
                print("|3.SEARCH BY BOOK NAME                |")
                print("|4.EXIT TO BOOK BORROWER's CHOICE     |")
                print("+-------------------------------------+")
                m=int(input("ENTER YOUR CHOICE:"))
                if m==4:
                    break
                elif m==1:
                    b1()
                elif m==2:
                    b2()
                elif m==3:
                    b3()
                else:
                    print("INVALID CHOICE")
        if n==2:
            break
        elif n==1:
            bookshowcase()
        else:
            print("INVALID CHOICE")
while True:
    print("+------------------------------+")
    print("|           BOOKSTORE          |")
    print("|1.ADMIN                       |")
    print("|2.BOOK BORROWER               |")
    print("|3.EXIT                        |")
    print("+------------------------------+")
    n=int(input("ENTER YOUR CHOICE:"))
    if n==3:
        print("~~~~~~~~~~~~~~~~~~~~THANKYOU~~~~~~~~~~~~~~~~~~~~~")
        con.close()
        break
    elif n==1:
        admin()
    elif n==2:
        bookborrower()
    else:
        print("INVALID CHOICE")