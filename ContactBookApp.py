import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"

class ContactBookGUI:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        self.contacts = []

        # Labels and Entry fields
        tk.Label(master, text="Name:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, sticky=tk.E)

        tk.Label(master, text="Phone:").grid(row=1, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1, sticky=tk.E)

        tk.Label(master, text="Email:").grid(row=2, column=0, sticky=tk.W)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1, sticky=tk.E)

        tk.Label(master, text="Address:").grid(row=3, column=0, sticky=tk.W)
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1, sticky=tk.E)

        # Buttons
        add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        add_button.grid(row=4, column=0, columnspan=2)

        view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        view_button.grid(row=5, column=0, columnspan=2)

        search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        search_button.grid(row=6, column=0, columnspan=2)

        update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        update_button.grid(row=7, column=0, columnspan=2)

        delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        delete_button.grid(row=8, column=0, columnspan=2)

        # Text area for displaying contacts
        self.contact_display = tk.Text(master, height=10, width=50)
        self.contact_display.grid(row=9, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            new_contact = Contact(name, phone, email, address)
            self.contacts.append(new_contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def view_contacts(self):
        self.contact_display.delete(1.0, tk.END)
        if not self.contacts:
            self.contact_display.insert(tk.END, "No contacts available.")
            return

        for contact in self.contacts:
            self.contact_display.insert(tk.END, str(contact) + "\n")

    def search_contact(self):
        search_term = self.name_entry.get() or self.phone_entry.get()
        if not search_term:
            messagebox.showerror("Error", "Please enter a name or phone number to search.")
            return

        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        self.contact_display.delete(1.0, tk.END)
        if found_contacts:
            for contact in found_contacts:
                self.contact_display.insert(tk.END, str(contact) + "\n")
        else:
            self.contact_display.insert(tk.END, "No contacts found.")

    def update_contact(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Enter the name of the contact to update.")
            return

        new_phone = self.phone_entry.get()
        new_email = self.email_entry.get()
        new_address = self.address_entry.get()

        for contact in self.contacts:
            if contact.name == name:
                if new_phone: contact.phone = new_phone
                if new_email: contact.email = new_email
                if new_address: contact.address = new_address
                messagebox.showinfo("Success", f"Contact '{name}' updated successfully.")
                self.clear_entries()
                return

        messagebox.showerror("Error", f"Contact '{name}' not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Enter the name of the contact to delete.")
            return

        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
                self.clear_entries()
                self.view_contacts()
                return

        messagebox.showerror("Error", f"Contact '{name}' not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

root = tk.Tk()
gui = ContactBookGUI(root)
root.mainloop()


#Running the code!!!!
#done....