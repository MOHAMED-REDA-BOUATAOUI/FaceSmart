import sqlite3

def create_table():
    conn = sqlite3.connect("C:\\Users\\pc\\Desktop\\PFA\\face4.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Emp(
                   id INTEGER PRIMARY KEY,
                   nom TEXT NOT NULL,
                   prenom TEXT,
                   role TEXT,
                   gender TEXT,
                   status TEXT)''')
    conn.commit()
    conn.close()

def insert_attendance(employee_name, time):
    conn = sqlite3.connect("C:\\Users\\pc\\Desktop\\PFA\\face4.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Attendance (employee_name, time) VALUES (?, ?)', (employee_name, time))
    conn.commit()
    conn.close()

def fetch_attendance():
         conn = sqlite3.connect("C:\\Users\\pc\\Desktop\\PFA\\face4.db")
         cursor = conn.cursor()
         cursor.execute('SELECT * FROM Attendance')
         attendance = cursor.fetchall()
         conn.close()
         return attendance
def delete_attendance():
    conn = sqlite3.connect("C:\\Users\\pc\\Desktop\\PFA\\face4.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Attendance WHERE id >= 1')
    conn.commit()
    conn.close()

def fetch_employes():
        conn = sqlite3.connect("C:\\Users\\pc\\Desktop\\PFA\\face4.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Emp')
        employes = cursor.fetchall()
        conn.close()
        return employes
def insert_employes(id, nom, prenom, role, gender, status):
        conn=sqlite3.connect("C:\\Users\\pc\\Desktop\\PFA\\face4.db")
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Emp (id, nom, prenom, role, gender, status) VALUES(?, ?, ?, ?, ?, ?)',
                       (id, nom, prenom, role, gender, status))
        conn.commit()
        conn.close()

def delete_employes(id):
        conn=sqlite3.connect("C:\\Users\\pc\\Desktop\\PFA\\face4.db")
        cursor= conn.cursor()
        cursor.execute('DELETE FROM Emp WHERE id = ? ', (id,))
        conn.commit()
        conn.close()
        create_table()

def update_employes(nv_nom, nv_prenom , nv_role, nv_gender, nv_status, id):
        conn = sqlite3.connect("C:\\Users\\pc\\Desktop\\PFA\\face4.db")
        cursor = conn.cursor()
        cursor.execute('UPDATE Emp SET nom = ?, prenom= ?, role= ?, gender= ?, status= ? WHERE id= ? ',
                       (nv_nom, nv_prenom, nv_role, nv_gender, nv_status, id))
        conn.commit()
        conn.close()
        create_table()
def id_exists(id):
        conn = sqlite3.connect("C:\\Users\\pc\\Desktop\\PFA\\face4.db")
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM Emp WHERE id = ? ', (id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] > 0

create_table()




