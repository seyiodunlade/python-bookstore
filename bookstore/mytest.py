from tkinter import *
from bookstore.backend import Database

database = Database()


class MyTest:

    def get_selected_row(self, event):
        try:
            global selected_book
            # self.selected_book
            index = self.list1.curselection()[0]
            selected_book = self.list1.get(index)
            print(self.list1.curselection())

            self.title_entry.delete(0, END)
            self.title_entry.insert(END, selected_book[1])

            self.author_entry.delete(0, END)
            self.author_entry.insert(END, selected_book[2])

            self.year_entry.delete(0, END)
            self.year_entry.insert(END, selected_book[3])

            self.isbn_entry.delete(0, END)
            self.isbn_entry.insert(END, selected_book[4])

        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search_entry(self.title_entry_value.get(), self.author_entry_value.get(),
                                         self.year_entry_value.get(), self.isbn_entry_value.get()):
            self.list1.insert(END, row)

    def add_entry_command(self):
        database.add_entry(self.title_entry_value.get(), self.author_entry_value.get(), self.year_entry_value.get(),
                           self.isbn_entry_value.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_entry_value.get(), self.author_entry_value.get(),
                                self.year_entry_value.get(), self.isbn_entry_value.get()))

    def delete_command(self):
        database.delete(selected_book[0])
        self.view_command()

    def update_command(self):
        database.update(selected_book[0], self.title_entry_value.get(), self.author_entry_value.get(),
                        self.year_entry_value.get(), self.isbn_entry_value.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_entry_value.get(), self.author_entry_value.get(),
                                self.year_entry_value.get(), self.isbn_entry_value.get()))

    def __init__(self):
        self.window = Tk()
        self.title_label = Label(self.window, text="Title")
        self.title_label.grid(row=0, column=0)

        self.author_label = Label(self.window, text="Author")
        self.author_label.grid(row=0, column=2)

        self.year_label = Label(self.window, text="Year")
        self.year_label.grid(row=1, column=0)

        self.isbn_label = Label(self.window, text="ISBN")
        self.isbn_label.grid(row=1, column=2)

        # Entry
        self.title_entry_value = StringVar()
        self.title_entry = Entry(self.window, textvariable=self.title_entry_value)
        self.title_entry.grid(row=0, column=1)

        self.author_entry_value = StringVar()
        self.author_entry = Entry(self.window, textvariable=self.author_entry_value)
        self.author_entry.grid(row=0, column=3)

        self.year_entry_value = StringVar()
        self.year_entry = Entry(self.window, textvariable=self.year_entry_value)
        self.year_entry.grid(row=1, column=1)

        self.isbn_entry_value = StringVar()
        self.isbn_entry = Entry(self.window, textvariable=self.isbn_entry_value)
        self.isbn_entry.grid(row=1, column=3)

        # Listbox
        self.list1 = Listbox(self.window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        #  scrollbar
        self.sb1 = Scrollbar(self.window)
        self.sb1.grid(row=2, column=2, rowspan=6)

        # Connecting List1 to scrollbar
        self.list1.configure(yscrollcommand=self.sb1.set)

        # Connecting scrollbar to List1
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        #  Buttons
        self.b1 = Button(self.window, text="View all", width=12, command=self.view_command)
        self.b1.grid(row=2, column=3)

        self.b2 = Button(self.window, text="Search entry", width=12, command=self.search_command)
        self.b2.grid(row=3, column=3)

        self.b3 = Button(self.window, text="Add entry", width=12, command=self.add_entry_command)
        self.b3.grid(row=4, column=3)

        self.b4 = Button(self.window, text="Update Selected", width=12, command=self.update_command)
        self.b4.grid(row=5, column=3)

        self.b5 = Button(self.window, text="Delete Selected", width=12, command=self.delete_command)
        self.b5.grid(row=6, column=3)

        self.b6 = Button(self.window, text="Close", width=12, command=self.window.destroy)
        self.b6.grid(row=7, column=3)


my_test = MyTest()
my_test.window.mainloop()
