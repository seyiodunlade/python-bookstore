from tkinter import *
from bookstore.backend import Database

database = Database()


def get_selected_row(event):
    try:
        global selected_book
        index = list1.curselection()[0]
        selected_book = list1.get(index)
        print(list1.curselection())

        title_entry.delete(0, END)
        title_entry.insert(END, selected_book[1])

        author_entry.delete(0, END)
        author_entry.insert(END, selected_book[2])

        year_entry.delete(0, END)
        year_entry.insert(END, selected_book[3])

        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_book[4])

    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in database.search_entry(title_entry_value.get(), author_entry_value.get(), year_entry_value.get(),
                                     isbn_entry_value.get()):
        list1.insert(END, row)


def add_entry_command():
    database.add_entry(title_entry_value.get(), author_entry_value.get(), year_entry_value.get(),
                       isbn_entry_value.get())
    list1.delete(0, END)
    list1.insert(END, (title_entry_value.get(), author_entry_value.get(), year_entry_value.get(),
                       isbn_entry_value.get()))


def delete_command():
    database.delete(selected_book[0])
    view_command()


def update_command():
    database.update(selected_book[0], title_entry_value.get(), author_entry_value.get(), year_entry_value.get(),
                    isbn_entry_value.get())
    list1.delete(0, END)
    list1.insert(END, (title_entry_value.get(), author_entry_value.get(), year_entry_value.get(),
                       isbn_entry_value.get()))


window = Tk()

title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)

# Entry
title_entry_value = StringVar()
title_entry = Entry(window, textvariable=title_entry_value)
title_entry.grid(row=0, column=1)

author_entry_value = StringVar()
author_entry = Entry(window, textvariable=author_entry_value)
author_entry.grid(row=0, column=3)

year_entry_value = StringVar()
year_entry = Entry(window, textvariable=year_entry_value)
year_entry.grid(row=1, column=1)

isbn_entry_value = StringVar()
isbn_entry = Entry(window, textvariable=isbn_entry_value)
isbn_entry.grid(row=1, column=3)

# Listbox
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#  scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# Connecting List1 to scrollbar
list1.configure(yscrollcommand=sb1.set)

# Connecting scrollbar to List1
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

#  Buttons
b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)


b3 = Button(window, text="Add entry", width=12, command=add_entry_command)
b3.grid(row=4, column=3)


b4 = Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.wm_title("BookInfo")

window.mainloop()
