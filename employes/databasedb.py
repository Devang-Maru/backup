import sqlite3

conn = sqlite3.connect('Emp.db')
print("create database successfull done")

conn.execute("create table employes (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,password TEXT NOT NULL)")
print("create table successfull done")

conn.close()