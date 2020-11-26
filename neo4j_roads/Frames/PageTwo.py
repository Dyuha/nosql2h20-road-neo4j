from main import example
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Меню", font=controller.title_font).place(x=70,y=50)
        tk.Label(self, text="Выберите город", font=controller.title_font).place(x=20, y=150)

        def onListsButtonsClick(index):
            controller.show_frame("PageFive")
            print(index)

        tk.Button(self, text="Назад",
                  command=lambda: controller.show_frame("PageOne")).place(x=20, y=50)
        tk.Button(self, text="5",
                  command=lambda: onListsButtonsClick(5)).place(x=620, y=50)
        tk.Button(self, text="7",
                  command=lambda: onListsButtonsClick(7)).place(x=670, y=50)
        tk.Button(self, text="9",
                  command=lambda: onListsButtonsClick(9)).place(x=720, y=50)
        tk.Button(self, text="11",
                  command=lambda: controller.show_frame("PageEleven")).place(x=720, y=550)

        frameList = tk.Frame(self)
        frameList.place(x=0,y=0)
        frameList.pack(side="top",expand=1,fill="x")

        scrollbar = tk.Scrollbar(frameList)
        scrollbar.pack(side="right",fill="y")

        def onSelectCity(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            controller.frames["PageThree"].titleFrameLabel['text'] = value
            controller.frames["PageThree"].change_list_of_works_by_city()
            controller.show_frame("PageThree")
            print('You selected item %d: "%s"' % (index, value))

        self.mylist = tk.Listbox(frameList, yscrollcommand=scrollbar.set)
        self.mylist.bind('<<ListboxSelect>>',onSelectCity)

        #for line in example.get_cities():
            #self.mylist.insert(tk.END, str(line))

        self.mylist.pack(side="left", fill="both",expand = 1)
        scrollbar.config(command=self.mylist.yview)

    def change_list_of_cities(self):
        self.mylist.delete(0,tk.END)
        for line in example.get_cities():
            self.mylist.insert(tk.END, str(line))