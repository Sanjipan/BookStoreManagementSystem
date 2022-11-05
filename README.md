
# BOOK STORE MANAGEMENT SYSTEM

**A BOOK STORE MANAGEMENT SYSTEM made in python and database MySQL.**
######
*This Program is used to manage a bookstore where we can enter as a Admin or the owner and User as the borrower we have created manny options for the admin and the user for managing and borrowing with better experience.*
## Installation

Install mysql.connector module:

```bash
$ pip install mysql-connector-python
```
Change The Attributes as per your own system:
```bash
con=mysql.connector.connect(host="localhost<host>",user="root<user>",passwd="<password>",database="bookstore<database>")
```


#### **DATABASE NEED TO BE CREATED:**

| **Database**           |
| :------------------------- |
| information_schema |
| *bookstore*          |-------->Database
| mysql              |
| performance_schema |
| test               |

#### TABLES MUST BE CREATED UNDER DATABASE ***"bookstore"***

| **Tables_in_bookstore** |
| :------------------------- |
| booklist            |
| borrowers           |

#### TABLE PARAMETERS OF TABLE booklist:


| **Field**      |**Type**        |**Null** |**Key** |**Default** | **Extra** |
| :--------- | :---------  | :--- |:--- |:------ |:------------
| slno       | int(5)      | YES  |     | NULL    |       |
| bookname   | varchar(30) | YES  |     | NULL    |       |
| authorname | varchar(30) | YES  |     | NULL    |       |
| genre      | varchar(30) | YES  |     | NULL    |       |
| bookid     | varchar(5)  | YES  |     | NULL    |       |
| qty        | int(3)      | YES  |     | NULL    |       |

#### TABLE PARAMETERS OF TABLE borrowers:


| **Field**      |**Type**        |**Null** |**Key** |**Default** | **Extra** |
| :----------- | :---------  | :--- |:--- |:------- |:------------
| slno         | int(3)      | YES  |     | NULL    |       |
| name         | varchar(30) | YES  |     | NULL    |       |
| phone        | int(10)     | YES  |     | NULL    |       |
| address      | varchar(30) | YES  |     | NULL    |       |
| bookname     | varchar(30) | YES  |     | NULL    |       |
| bookid       | varchar(5)  | YES  |     | NULL    |       |
| dateofborrow | date        | YES  |     | NULL    |       |
| dateofreturn | date        | YES  |     | NULL    |       |




## Authors:

- [@Sanjipan](https://github.com/Sanjipan)
- [@Abanteeka](https://github.com/Abanteeka/)

