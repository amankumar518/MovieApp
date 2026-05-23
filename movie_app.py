import sqlite3

conn = sqlite3.connect("C:\\Users\\AMAN KUMAR\\Documents\\movies.db")
cursor = conn.cursor()

print("Connected successfully!")

conn.close()

import sqlite3

def connect_db():
    conn = sqlite3.connect("C:\\Users\\AMAN KUMAR\\Documents\\movies.db")
    return conn

def add_movie():
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter movie name: ")
    rating = float(input("Enter rating (0–10): "))
    cursor.execute("INSERT INTO movies (name, rating) VALUES (?, ?)", (name, rating))
    conn.commit()
    print("Movie added successfully!")
    conn.close()

def show_movies():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    print("\n--- Movie List ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Rating: {row[2]}")
    conn.close()

def recommend_movies():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, rating FROM movies WHERE rating >= 8")
    rows = cursor.fetchall()
    print("\n🎯 Recommended Movies (Rating ≥ 8)")
    for row in rows:
        print(f"{row[0]} — Rating: {row[1]}")
    conn.close()

while True:
    print("\n===== Movie Menu =====")
    print("1. Add Movie")
    print("2. Show All Movies")
    print("3. Show Recommended Movies")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        show_movies()
    elif choice == "3":
        recommend_movies()
    elif choice == "4":
        print("Goodbye Aman! 👋")
        break
    else:
        print("Invalid choice, please try again.")
