import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        # Create a dictionary to store contacts
        self.contacts = {}
        
        # Create a listbox to display contacts
        self.contact_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.contact_listbox.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contact", command=self.view_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        
        self.add_button.pack(padx=10, pady=10, side=tk.TOP, fill=tk.X)
        self.view_button.pack(padx=10, pady=10, side=tk.TOP, fill=tk.X)
        self.update_button.pack(padx=10, pady=10, side=tk.TOP, fill=tk.X)
        self.delete_button.pack(padx=10, pady=10, side=tk.TOP, fill=tk.X)
        
        # Bind double-click event to view_contact function
        self.contact_listbox.bind("<Double-1>", lambda event: self.view_contact())
        
    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter Name:")
        if name:
            phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
            if phone:
                self.contacts[name] = phone
                self.contact_listbox.insert(tk.END, name)
                
    def view_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            name = self.contact_listbox.get(selected_index[0])
            phone = self.contacts.get(name, "N/A")
            messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {phone}")
            
    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            name = self.contact_listbox.get(selected_index[0])
            new_phone = simpledialog.askstring("Update Contact", f"Update Phone Number for {name}:")
            if new_phone:
                self.contacts[name] = new_phone
            
    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            name = self.contact_listbox.get(selected_index[0])
            confirm = messagebox.askyesno("Delete Contact", f"Delete {name}?")
            if confirm:
                del self.contacts[name]
                self.contact_listbox.delete(selected_index[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
