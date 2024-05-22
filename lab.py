import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database
import subprocess
from tkinter import PhotoImage


app = customtkinter.CTk()
app.title('Gestion des Employes')
app.geometry('900x800')
app.config(bg='#161C25')
app.resizable(True,True)

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

def add_to_treeview():
    employes = database.fetch_employes()
    tree.delete(*tree.get_children())
    for employes in employes:
        tree.insert('', END, values=(employes))
def insert():
    id = id_entry.get()
    nom = name_entry.get()
    prenom = prenom_entry.get()
    role = variable1.get()
    gender = variable2.get()
    status = status_entry.get()
    if not(id and nom and prenom and role and gender and status):
        messagebox.showerror('Error', 'Enter all fields')
    elif database.id_exists(id):
        messagebox.showerror('Error', 'Id already exists')
    else:
        database.insert_employes(id,nom,prenom,role,gender,status)
        add_to_treeview()
        messagebox.showinfo('Success','Data has been saved')

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    prenom_entry.delete(0,END)
    variable1.set('Select')
    variable2.set('Select')
    status_entry.delete(0,END)
def display_data(event):
    selected_item = tree.focus()
    if selected_item :
        row = tree.item(selected_item)['values']
        clear()
        id_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        prenom_entry.insert(0, row[2])
        variable1.set(row[3])
        variable2.set(row[4])
        status_entry.insert(0, row[5])
    else:
        pass

def delete():
    selected_item = tree.focus()
    if not selected_item :
        messagebox.showerror('Error','Please you need to select an employee first')
    else:
        id_delete = tree.item(selected_item)['values'][0]
        database.delete_employes(id_delete)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Employee has been deleted')

def update():
    selected_item = tree.focus()
    if not selected_item :
        messagebox.showerror('Error', 'Please you need to select an employee first')
    else :
        id_updt = tree.item(selected_item)['values'][0]
        nv_nom = name_entry.get()
        nv_prenom = prenom_entry.get()
        nv_role = variable1.get()
        nv_gender = variable2.get()
        nv_status = status_entry.get()
        database.update_employes(nv_nom,nv_prenom,nv_role,nv_gender,nv_status, id_updt)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Employee has been updated')

def run_main_script():
    subprocess.Popen(["C:\\Users\\pc\\Desktop\\PFA\\.venv\\Scripts\\python.exe", "C:\\Users\\pc\\Desktop\\PFA\\main.py"])

def record_attendance():
    subprocess.Popen(["C:\\Users\\pc\\Desktop\\PFA\\.venv\\Scripts\\python.exe","C:\\Users\\pc\\Desktop\\PFA\\Attendance.py"])

camera_icon = PhotoImage(file="C:\\Users\\pc\\desktop\\PFA\\images\\camera.png")

def fetch_attendance():
    return database.fetch_attendance()

# Fonction pour créer et afficher le tableau d'assiduité
def display_attendance():
    attendance_data = fetch_attendance()

    for row in attendance_tree.get_children():
        attendance_tree.delete(row)

    for data in attendance_data:
        attendance_tree.insert('', END, values=data)
def delete_attendance():
    database.delete_attendance()
    display_attendance()


# Créer un Treeview pour afficher les données d'assiduité
attendance_tree = ttk.Treeview(app, height=10)
attendance_tree['columns'] = ('Id', 'Employe Name', 'Time')
attendance_tree.column('#0', width=0, stretch=tk.NO)
attendance_tree.column('Id', anchor=tk.CENTER, width=200)
attendance_tree.column('Employe Name', anchor=tk.CENTER, width=200)
attendance_tree.column('Time', anchor=tk.CENTER, width=200)
attendance_tree.heading('Employe Name', text='Employe Name')
attendance_tree.heading('Time', text='Time')
attendance_tree.place(x=300, y=600)


id_label = customtkinter.CTkLabel(app, font=font1, text='ID', text_color='#fff', bg_color='#161C25')
id_label.place(x=20, y=20)
id_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=200)
id_entry.place(x=120, y=20)

name_label = customtkinter.CTkLabel(app, font=font1, text='NOM', text_color='#fff', bg_color='#161C25')
name_label.place(x=20, y=80)
name_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=200)
name_entry.place(x=120, y=80)

prenom_label = customtkinter.CTkLabel(app, font=font1, text='PRENOM', text_color='#fff', bg_color='#161C25')
prenom_label.place(x=20, y=140)
prenom_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=200)
prenom_entry.place(x=120, y=140)

role_label = customtkinter.CTkLabel(app, font=font1, text='ROLE', text_color='#fff', bg_color='#161C25')
role_label.place(x=20, y=200)
options = ['Developpeur', 'Technicien', 'Chef de projet', 'Directeur General', 'Designer']
variable1 = StringVar()
options_combobox = customtkinter.CTkComboBox(app, font=font1, text_color='#000', button_color='#0C9295',width=200,variable=variable1,values=options,state='readonly')
options_combobox.set('Developpeur')
options_combobox.place(x=120, y=200)

gender_label = customtkinter.CTkLabel(app, font= font1, text='GENDER', text_color='#fff', bg_color='#161C25')
gender_label.place(x=20, y=260)
options2 = ['Homme', 'Femme']
variable2 = StringVar()
options2_combobox = customtkinter.CTkComboBox(app, font=font1, text_color='#000', button_color='#0C9295',width=200,variable=variable2,values=options2,state='readonly')
options2_combobox.set('Homme')
options2_combobox.place(x=120, y=260)

status_label = customtkinter.CTkLabel(app, font=font1, text='STATUS', text_color='#fff', bg_color='#161C25')
status_label.place(x=20, y=310)
status_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=200)
status_entry.place(x=120, y=310)


add_button = customtkinter.CTkButton(app,command=insert, font=font1, text_color='#fff', text='Add Employe', fg_color='#05A312', hover_color='#00850B',bg_color='#161C25', cursor='hand2',corner_radius=15,width=260)
add_button.place(x=20 , y=370)

clear_button = customtkinter.CTkButton(app,command=lambda:clear(True),font=font1, text_color='#fff', text='Reset', fg_color='#161C25', hover_color='#FF5002',bg_color='#161C25',border_color='#F15707',border_width=2 ,cursor='hand2',corner_radius=15,width=260)
clear_button.place(x=20 , y=430)

update_button = customtkinter.CTkButton(app,command=update ,font=font1, text_color='#fff', text='Update Employe', fg_color='#161C25', hover_color='#FF5002',bg_color='#161C25',border_color='#F15704', border_width=2, cursor='hand2',corner_radius=15,width=260)
update_button.place(x=300 , y=430)

delete_button = customtkinter.CTkButton(app, command=delete, font=font1, text_color='#fff', text='Delete Employe', fg_color='#E40404', hover_color='#AE0000',bg_color='#161C25',border_color='#E40404', border_width=2, cursor='hand2',corner_radius=15,width=260)
delete_button.place(x=300 , y=370)

record_attendance_button = customtkinter.CTkButton(app, command=record_attendance, font=font1, text_color='#fff', text='Record Attendance', fg_color='#0000FF', hover_color='#00FFFF', bg_color='#161C25', cursor='hand2', corner_radius=15, width=260)
record_attendance_button.place(x=580, y=370)

run_button = customtkinter.CTkButton(app, command=run_main_script, font=font1, text_color='#fff', text='Start Camera', fg_color='#05A312', hover_color='#00850B', bg_color='#161C25', cursor='hand2', corner_radius=15, width=260, image=camera_icon, compound="left")
run_button.place(x=580, y=430)

fetch_button = customtkinter.CTkButton(app, command=display_attendance, font=font1, text_color='#fff', text='Fetch Attendance', fg_color='#0000FF', hover_color='#00FFFF', bg_color='#161C25', cursor='hand2', corner_radius=15, width=160)
fetch_button.place(x=20, y=500)
delete_attendance_button = customtkinter.CTkButton(app, command=delete_attendance, font=font1, text_color='#fff', text='Delete Attendance', fg_color='#0000FF', hover_color='#00FFFF', bg_color='#161C25', cursor='hand2', corner_radius=15, width=160)
delete_attendance_button.place(x=20, y=560)


style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview', font=font2,foreground='#fff',background='#000',fieldbackground='#313837')
style.map('Treeview',background=[('selected', '#1A8F2D')])

tree = ttk.Treeview(app,height=20)
tree['columns'] = ('ID', 'NOM', 'PRENOM', 'ROLE', 'GENDER', 'STATUS')
tree.column('#0', width=0, stretch=tk.NO)
tree.column('ID', anchor=tk.CENTER, width=120)
tree.column('NOM', anchor=tk.CENTER, width=120)
tree.column('PRENOM', anchor=tk.CENTER, width=120)
tree.column('ROLE', anchor=tk.CENTER, width=120)
tree.column('GENDER', anchor=tk.CENTER, width=100)
tree.column('STATUS', anchor=tk.CENTER, width=120)

tree.heading('ID',text='ID')
tree.heading('NOM',text='NOM')
tree.heading('PRENOM',text='PRENOM')
tree.heading('ROLE',text='ROLE')
tree.heading('GENDER',text='GENDER')
tree.heading('STATUS',text='STATUS')

tree.place(x=420 , y=20)



tree.bind('<ButtonRelease>', display_data)
add_to_treeview()
app.mainloop()


