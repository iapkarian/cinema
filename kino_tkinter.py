from tkinter import *
from tkinter import ttk
from db import Ticket
from datetime import *

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title('parent')
        self.master.geometry('550x400+300+225')
        self.create_menu()
        self.master.mainloop()



    def create_film(self):
        Films(self.master)

    def create_menu(self):
        notebook = ttk.Notebook(root)
        today = datetime.today()
        lbl = Label(self.master, text='MOST-CINEMA', font='Arial 20')
        lbl.pack()
        films = ttk.Combobox()
        films['values'] = ('Film 1', )
        films.pack()
        but = Button(self.master, text='Create film', command=self.create_film)
        but.pack()
        but1 = Button(self.master,
                      text='Hall №1',
                      command=self.open_first_win)
        but1.pack()
        but2 = Button(self.master,
                      text='Hall №2',
                      command=self.open_second_win)
        but2.pack()
        notebook.add(Frame(width=400, height=300),
                     text=today.strftime('%a  %d.%m'))
        for i in range(1, 7):
            tomorrow = today.date() + timedelta(days=i)
            tomorrow = tomorrow.strftime('%a  %d.%m')
            notebook.add(Frame(width=800, height=300),
                         text=tomorrow,)
        notebook.bind_all("<<NotebookTabChanged>>",) #self.master.tabChangedEvent)

        notebook.pack()

    def tabChanged(self):
        pass

    def open_first_win(self):
        FirstHall(self.master)

    def open_second_win(self):
        SecondHall(self.master)

class Films:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.slave.title('Create/delete film')
        self.slave.geometry('500x300')
        self.new_film()

    def new_film(self):
        lbl1 = Label(self.slave, text='Create new film:', font='Arial 18')
        lbl2 = Label(self.slave, text='Name:', font='Arial 12')
        lbl3 = Label(self.slave, text='Duration:', font='Arial 12')
        ent1 = Entry(self.slave, width=20, bd=3,)
        ent2 = Entry(self.slave, width=20, bd=3)
        but_create = Button(self.slave, text='Create', font='Arial 12')

        lbl1.grid(row=1, column=15)
        lbl2.grid(row=2, column=2)
        lbl3.grid(row=2, column=20)
        ent1.grid(row=3, column=2)
        ent2.grid(row=3, column=20)
        but_create.grid(row=5, column=15)

        lbl4 = Label(self.slave, text='Delete film:', font='Arial 18')
        lst = Text(self.slave, height=7, width=15, font="Verdana 12", wrap=WORD)
        but_delete = Button(self.slave, text='Delete', font='Arial 12')

        lbl4.grid(row=9, column=15)
        lst.grid(row=10, column=2, columnspan=10)
        but_delete.grid(row=10, column=15)

class FirstHall:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.slave.title('Hall №1')
        self.SUM_All = 0
        self.places = []
        self.cal = False
        self.hall = Frame(self.slave, width=500, height=300, )
        self.lbl = Label(self.slave,
                         text="Hall №1",
                         font="Arial 12", )
        self.lbl.pack()
        self.lbl_sum = Label(self.hall, text=self.SUM_All, font="Arial 12")
        self.lbl_sum.grid(row=2, column=23, rowspan=10)
        self.create_hall()
        self.menu_hall()
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()

    def num_row(self, j, i):
        num_row = Label(self.hall, text=j)
        num_row.grid(row=j+1, column=i)

    def buy_tic(self, event):
        self.SUM_All = 0
        self.lbl_sum.destroy()

    def menu_hall(self):
        menu_hall = Frame(self.hall, width=100, height=300)
        menu_hall.grid(row=2, column=23, rowspan=10)
        lbl = Label(self.hall,
                    text="blue = 50 \n red = 100 \n grey = close",
                    font="Arial 12")
        lbl.grid(row=0, column=23, rowspan=10)
        but_buy = Button(self.hall, text="Buy!", font="Arial 12")
        but_buy.bind("<Button-1>", self.buy_tic)
        but_buy.grid(row=6, column=23, rowspan=10)

    def reservation(self, event, row, column):
        bg_color = event.widget["background"]
        if bg_color != "grey":
            ticket = Ticket(line=row-1, seat=column-1, )
            if bg_color == "red":
                ticket.price = 50
                ticket.type_seat = 'red'
                self.SUM_All += 50
            elif bg_color == "blue":
                ticket.price = 45
                ticket.type_seat = 'blue'
                self.SUM_All += 45
            event.widget["background"] = "grey"
            ticket.save()
        elif bg_color == "grey" and self.SUM_All != 0:
            if row <= 3:
                self.SUM_All -= 45
                event.widget["background"] = "blue"
            else:
                self.SUM_All -= 50
                event.widget["background"] = "red"
            Ticket.delete().where(Ticket.line == row-1, Ticket.seat == column-1).execute()
        self.lbl_sum.destroy()
        self.lbl_sum = Label(self.hall, text=self.SUM_All, font="Arial 12")
        self.lbl_sum.grid(row=4, column=23, rowspan=10)

    def create_hall(self):
        sell_ticket = []
        for j in range(1, 11):
            for i in range(1, 21):
                try:
                    Ticket.get(Ticket.line == j, Ticket.seat == i, )
                    sell_ticket.append((j, i))
                except Ticket.DoesNotExist:
                    pass
        self.hall.pack()
        screen = Frame(self.hall, width=500, height=20, bg="yellow")
        screen.grid(row=0, column=2, columnspan=20)
        named = Label(self.hall, text="Screen")
        named.grid(row=1, column=2, columnspan=20)

        for j in range(1, 11):
            self.num_row(j, 1)
            for i in range(1, 21):
                if (j, i) in sell_ticket:
                    color = 'grey'
                elif j >= 3:
                    color = "red"
                else:
                    color = "blue"
                but = Button(self.hall, text=i,
                             bg=color)
                but.bind("<Button-1>", lambda event, row=j+1, column=i+1: self.reservation(event, row, column))
                but.grid(row=j+1, column=i+1)
            self.num_row(j, 22)

class SecondHall:
    def __init__(self, master):
        self.slave2 = Toplevel(master)
        self.slave2.title('Hall №2')
        self.SUM_All = 0
        self.places = []
        self.cal = False
        self.hall = Frame(self.slave2, width=500, height=300, )
        self.lbl = Label(self.slave2,
                         text="Hall №2",
                         font="Arial 12")
        self.lbl.pack()
        self.lbl_sum = Label(self.hall, text=self.SUM_All, font="Arial 12")
        self.lbl_sum.grid(row=2, column=23, rowspan=10)
        # self.create_hall()
        # self.menu_hall()
        self.slave2.grab_set()
        self.slave2.focus_set()
        self.slave2.wait_window()

    # def create_hall(self):

root = Tk()
MainWindow(root)




