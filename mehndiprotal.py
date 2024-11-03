import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import psycopg2

class WelcomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Mehndi Portal")
        self.root.geometry("600x500")

        # Define colors
        background_color = "#f1f1f1"
        text_color = "#0000FF"
        button_color = "#f1f1f1"
        button_text_color = "#0000FF"

        # Load and set background image
        self.bg_image = Image.open(r"C:\Users\a\Pictures\mehndi protal\b691e8205f99347320de8cf0b141f79c.jpg")  # Replace with your actual image path
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.root.configure(background=background_color)

        self.label_welcome = tk.Label(self.root, text="Welcome to Mehndi Portal", font=("Arial", 30, "bold"), fg=button_text_color, bg=background_color)
        self.label_welcome.pack(pady=30)

        self.label_info = tk.Label(self.root, text="Please login to access the system", font=("Arial", 19), fg=text_color, bg=background_color)
        self.label_info.pack(pady=10)

        self.button_login = tk.Button(self.root, text="Login", font=("Arial", 18, "bold"), bg=button_color, fg=button_text_color, command=self.open_login_window)
        self.button_login.pack(pady=20)

    def open_login_window(self):
        self.root.destroy()
        login_window = tk.Tk()
        LoginWindow(login_window)
        login_window.mainloop()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("600x500")

        # Load and set background image
        self.bg_image = Image.open(r"C:\Users\a\Pictures\mehndi protal\b691e8205f99347320de8cf0b141f79c.jpg")  # Replace with your actual image path
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        self.frame_login = tk.Frame(self.root, bg="beige")
        self.frame_login.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.label_username = tk.Label(self.frame_login, text="Username:", fg="black", font=("Arial", 22, "bold"), bg="beige")
        self.label_username.grid(row=0, column=0, padx=5, pady=5)
        self.entry_username = tk.Entry(self.frame_login, font=("Arial", 16))
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)

        self.label_password = tk.Label(self.frame_login, text="Password:", fg="black", font=("Arial", 22, "bold"), bg="beige")
        self.label_password.grid(row=1, column=0, padx=5, pady=5)
        self.entry_password = tk.Entry(self.frame_login, show="*", font=("Arial", 16))
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        self.button_login = tk.Button(self.frame_login, text="Login", command=self.login, bg="black", fg="white", font=("Arial", 16, "bold"))
        self.button_login.grid(row=2, columnspan=2, padx=5, pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "1" and password == "1":
            self.root.destroy()
            app = MehndiManagementApp(tk.Tk())
            app.root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password")


class MehndiManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mehndi Management System")
        self.root.geometry("800x700")

        # Load and set background image
        self.bg_image = Image.open(r"C:\Users\a\Pictures\mehndi protal\b691e8205f99347320de8cf0b141f79c.jpg")  # Replace with your actual image path
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        try:
            self.db_connection = psycopg2.connect(
                dbname="postgres",  # Modify with your database name
                user="postgres",    # Modify with your username
                password="1234",    # Modify with your password
                host="localhost"
            )
            self.cursor = self.db_connection.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not connect to database: {e}")
            self.root.destroy()

        self.frame_design_info = tk.Frame(self.root, bg="beige")
        self.frame_design_info.place(relx=0.3, rely=0.1)

        self.label_design_name = tk.Label(self.frame_design_info, text="Design Name:", bg="beige", fg="black", font=("Arial", 16, "bold"))
        self.label_design_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_design_name = tk.Entry(self.frame_design_info, font=("Arial", 16))
        self.entry_design_name.grid(row=0, column=1, padx=5, pady=5)

        self.button_add_design = tk.Button(self.frame_design_info, text="Add Design", command=self.add_design, bg="black", fg="white", font=("Arial", 16, "bold"))
        self.button_add_design.grid(row=0, column=2, padx=5, pady=5)

        self.button_show_designs = tk.Button(self.frame_design_info, text="Show Designs", command=self.show_designs, bg="black", fg="white", font=("Arial", 16, "bold"))
        self.button_show_designs.grid(row=1, column=0, padx=5, pady=5)

        self.button_delete_design = tk.Button(self.frame_design_info, text="Delete Design", command=self.delete_design, bg="black", fg="white", font=("Arial", 16, "bold"))
        self.button_delete_design.grid(row=1, column=1, padx=5, pady=5)

        self.create_treeview()
        self.show_designs()  # Load designs on startup

    def create_treeview(self):
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=1, relheight=0.4)

        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Design Name"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Design Name", text="Design Name")

        self.tree.column("ID", width=50)
        self.tree.column("Design Name", width=250)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def add_design(self):
        design_name = self.entry_design_name.get()
        if not design_name:
            messagebox.showwarning("Warning", "Please enter a design name")
            return

        sql = "INSERT INTO CategoriesMehndi (category_name ) VALUES (%s)"
        values = (design_name,)
        self.execute_query(sql, values)
        messagebox.showinfo("Success", "Design added successfully")
        self.show_designs()  # Update Treeview after adding

    def delete_design(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a design to delete")
            return

        design_id = self.tree.item(selected_item)['values'][0]
        sql = "DELETE FROM CategoriesMehndi WHERE id = %s"
        values = (design_id,)
        self.execute_query(sql, values)
        messagebox.showinfo("Success", "Design deleted successfully")
        self.show_designs()  # Update Treeview after deletion

    def show_designs(self):
        sql = "SELECT * FROM CategoriesMehndi"
        designs = self.fetch_data(sql)
        self.display_treeview(designs)

    def fetch_data(self, sql, values=None):
        try:
            if values:
                self.cursor.execute(sql, values)
            else:
                self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def execute_query(self, sql, values=None):
        try:
            if values:
                self.cursor.execute(sql, values)
            else:
                self.cursor.execute(sql)
            self.db_connection.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_treeview(self, data):
        self.tree.delete(*self.tree.get_children())
        for row in data:
            self.tree.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    WelcomePage(root)
    root.mainloop()
