from tkinter import *

# global_vars
names = ["Kelly", "Dan", "John", "Reno", "Brian", "Mario", "Smitty", "Eric", "Josh", "Jacob", "Bethany"]


class View:
    def __init__(self, master):
        self.selected = ""

        self.title_names = Label(master, text="Names")
        self.title_names.grid(row=0, column=0)

        self.names = Listbox(master)
        self.names.grid(row=1, rowspan=4, column=0)

        self.want = Button(master, text="-->", command=self.add)
        self.want.grid(row=1, column=1)

        self.spoke = Button(master, text="<--", command=self.remove)
        self.spoke.grid(row=2, column=1)

        self.clr = Button(master, text="CLR", command=self.clear)
        self.clr.grid(row=3, column=1)

        self.spoke = Label(master, text="Speaker's List")
        self.spoke.grid(row=0, column=2)

        self.list = Listbox(master)
        self.list.grid(row=1, rowspan=4, column=2)

        self.names.bind('<<ListboxSelect>>', self.onselect)

        self.fill_list()

    def onselect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        self.selected = w.get(index)

    def fill_list(self):
        # You should make this take a file, and populate the list using the names in the file
        # Love, Reno

        # Agreed

        for item in names:
            self.names.insert(END, item)

    def add(self):
        self.list.insert(END, self.selected)
        pass

    def remove(self):
        self.list.delete(0, 0)

    def clear(self):
        self.list.delete(0, END)

root = Tk()

app = View(root)

root.mainloop()
