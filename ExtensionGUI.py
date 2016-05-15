# This file wil house the GUI design and overall System for version 2.0
# Coded by Zane Blalock of EssenceOfZen.org/
import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class MainFrame(Frame):
    def __init__(self,parent):
        self.title = "Extension Changer" # Default title
        self.size = "500x500" # Default size for the app
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initializeGUI()

    def initializeGUI(self):
        self.parent.title(self.title) # Set the title
        self.pack(fill=BOTH, expand=1)
        #self.parent.geometry(self.size)

        # Label that shows directory -----------------------------------------
        directory_frame = Frame(self)
        #Grid.columnconfigure(directory_frame, 0, weight=1)
        Grid.columnconfigure(directory_frame, 1, weight=3, )
        #Grid.columnconfigure(directory_frame, 2, weight=2)
        # directory_frame.grid(row=0, column=0, sticky=N+S+E+W)
        directory_frame.pack(fill=X)

        directory_label = Label(directory_frame, text="Directory",)
        # directory_label.grid(row=0, column=0)
        directory_label.pack(side=LEFT)

        directory_entry = Entry(directory_frame, width=50, background="white")
        # Grid.columnconfigure(directory_entry, 1, weight=3)
        # directory_entry.grid(row=0,column=1, padx=5, pady=5, sticky=N+S+E+W)
        directory_entry.pack(side=LEFT, padx=5, pady=5, expand=True, fill=BOTH)
        directory_entry.insert(0, "C:/Programming")

        directory_browse_button = Button(directory_frame, text="Browse")
        #Grid.columnconfigure(directory_browse_button, 1, weight=3)
        # directory_browse_button.grid(row=0,column=2, padx=5, pady=5, sticky=N+S+E+W)
        directory_browse_button.pack(side=RIGHT, padx=5, pady=5)

        #Body frames
        body_frame = Frame(self)
        body_frame.pack(fill=X)

        # Split Directories - Left for Directory, Right for files ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        directory_treeview = ttk.Treeview(body_frame, height=30)
        #directory_treeview["columns"]=("directory")
        #directory_treeview.column("directory", width=100)
        directory_treeview.column("#0", width=300, stretch=YES)
        directory_treeview.heading("#0", text="Directories")

        directory = directory_entry.get()
        print("Directory is: " + directory)

        directory_treeview.pack(side=LEFT, padx=5, pady=5, fill=BOTH, expand=True)

        # File View ~~~~~~~~~~~~~~~~~~~~~~~~~~
        files_treeview = ttk.Treeview(body_frame)
        files_treeview.column("#0", width=500, stretch=YES)
        files_treeview.heading("#0", text="Files")

        self.get_file_items(directory, files_treeview)
        files_treeview.pack(side=RIGHT, padx=5, pady=5, fill=BOTH, expand=True)

        # Target, Selection, and action buttons
        action_frame = Frame(self)
        action_frame.pack(fill=X)

        target_label = Label(action_frame, text="Target:")
        target_label.pack(side=LEFT, padx=5, pady=5)

        target = Combobox(action_frame)
        target["values"]= ("jpeg", "png") # todo: create function that pulls the extensions from file
        target.pack(side=LEFT, padx=5, pady=5)

        selection_label = Label(action_frame, text="Change to:")
        selection_label.pack(side=LEFT, padx=5, pady=5)

        selection = Combobox(action_frame)
        selection["values"] = ("jpeg", "png")
        selection.pack(side=LEFT, padx=5, pady=5)

        # Buttons
        execute_button = Button(action_frame, text="Change Extensions")
        execute_button.pack(side=RIGHT, padx=5, pady=5)

    def get_directory_items(self, directory, tree, parent):
        print("Attempting to grab directory")
        # Setup the root
        #node = tree.insert('', 'end', text="dir", values=[dir, "directory"])

    def get_file_items(self, directory, tree):
        direcory_items = os.listdir(directory)
        for item in direcory_items:
            # find a way to put the items in the files tree view
            tree.insert('', 'end', text=item)

def main():
    root = Tk()
    application = MainFrame(root)

    root.mainloop()

main()