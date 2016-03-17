from tkinter import *
import tkinter

class Window(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.SUM_All = 0
        self.places = []
        self.cal = False
        self.hall = Frame(self, width=500, height=300, )
        self.lbl = Label(self, text="Hall №1", font="Arial 12")
        self.lbl.pack()
        self.lbl_sum = Label(self.hall, text=self.SUM_All, font="Arial 12")
        self.lbl_sum.grid(row=2, column=23, rowspan=10)
        self.create_hall()
        self.Menu_hall()

    def Num_row(self, j, i):
        num_row = Label(self.hall, text=j)
        num_row.grid(row=j+1, column=i)

    def buy_tic(self, event):
        self.SUM_All = 0
        self.lbl_sum.destroy()

    def Menu_hall(self):
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
            if bg_color == "red":
                self.SUM_All += 50
            elif bg_color == "blue":
                self.SUM_All += 45
            event.widget["background"] = "grey"
        elif bg_color == "grey" and self.SUM_All != 0:
            if row <= 3:
                self.SUM_All -= 45
                event.widget["background"] = "blue"
            else:
                self.SUM_All -= 50
                event.widget["background"] = "red"
        self.lbl_sum.destroy()
        self.lbl_sum = Label(self.hall, text=self.SUM_All, font="Arial 12")
        self.lbl_sum.grid(row=4, column=23, rowspan=10)

    def create_hall(self):
        self.hall.pack()
        screen = Frame(self.hall, width=500, height=20, bg="yellow")
        screen.grid(row=0, column=2, columnspan=20)
        named = Label(self.hall, text="Screen")
        named.grid(row=1, column=2, columnspan=20)

        for j in range(1, 11):
            self.Num_row(j, 1)
            for i in range(1, 21):
                if j >= 3:
                    color = "red"
                else:
                    color = "blue"
                but = Button(self.hall, text=i,
                             bg=color)
                but.bind("<Button-1>", lambda event, row=j+1, column=i+1: self.reservation(event, row, column))
                but.grid(row=j+1, column=i+1)
            self.Num_row(j, 22)

if __name__ == '__main__':
    window_obj = Window()
    window_obj.mainloop()




