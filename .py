from tkinter import *
from tkinter import messagebox as mb
import PostgreSQL

class Main:
    def __init__(self):
        self.MainWindow()

    def MainWindow(self):
        root.title('Головна')
        Button(root,text ="USER", width = 20, height = 3, command = self.UserWindow).grid(row=0, column=0)
        Button(root,text ="CRUD", width = 20, height = 3, command = self.CRUD).grid(row=1, column=0)


    def UserWindow(self):
        def searcbysubject():
            mb.showinfo("Пошук",f"Обрано пошук за {self.Search.get()} \nрезультати пошуку - {PostgreSQL.showFromDb('discipline' , self.Search.get())}")

        def searchbyteacher():
            mb.showinfo("Пошук", f"Обрано пошук за {self.Search.get()}\nрезультатипошуку - {PostgreSQL.showFromDb('courses' , self.Search.get())}")

        def searchbytask():mb.showinfo("Пошук", f"Обрано пошук за {self.Search.get()}\nрезультатипошуку - {PostgreSQL.showFromDb('tasks' , self.Search.get())}")

        userW = Toplevel(root)
        userW.title("USER")
        Label(userW,text="Пошук за :").grid(row=2,column=8)
        Button(userW,text="Предмет",width = 20, height = 3, command = searcbysubject).grid(row=3,column=0)
        Button(userW, text="Курс викладача", width=20, height=3, command=searchbyteacher).grid(row=4, column=0)
        Button(userW, text="Завдання", width=20, height=3, command=searchbytask).grid(row=5, column=0)
        Label(userW, text = "Введіть значення для пошуку:").grid(row=0,column=0)
        self.Search = Entry(userW,width=40)
        self.Search.grid(row=1,column=8)

    def CRUD(self):
        def UpdateBD():
            mb.showinfo("BD",f"{PostgreSQL.showDb('tasks')}\n{PostgreSQL.showDb('discipline')}\n{PostgreSQL.showDb('courses')}\n")

        def ChangeBD():
            Change = Toplevel(root)
            Change.title("Change BD")
            Label(Change,text="Поміняти значення в Базі даних").grid(row=0,column=0)
            Label(Change, text="Ввести id").grid(row=1, column=0)
            id=Entry(Change,width=40)
            id.grid(row=2,column=0)
            Label(Change, text="Старе значення в базі даних").grid(row=3, column=0)

            oldV=Entry(Change,width=40)
            oldV.grid(row=4,column=0)
            Label(Change, text="Нове значення").grid(row=5, column=0)

            newV=Entry(Change,width=40)
            newV.grid(row=6,column=0)
            Label(Change, text="Колонка, яку хочете змінити").grid(row=7, column=0)

            ccg=Entry(Change,width=40)
            ccg.grid(row=8,column=0)
            Button(Change,text="Змінити",command=lambda:PostgreSQL.updateDb(id.get(),str(oldV.get()),str(newV.get()),ccg.get())).grid(row=9,column=0)

            def DeleteBD():
                Change=Toplevel(root)
                Change.title("Delete BD")
                Label(Change,text="Видалити значення в БД").grid(row=0,column=0)
                Label(Change,text="Ввести id")
                id.grid(row=2,column=0)
                Label(Change,text="Таблиця").grid(row=3,column=0)
                table=Entry(Change,width=40)
                table.grid(row=4,column=0)
                Button(Change,text="ВИдалити",command=lambda:PostgreSQL.deleteFromDb(id.get(),table.get())).grid(row=7,column=0)

            def CreateBD():
                Change=Toplevel(root)
                Change.title("CreateBD")
                Label(Change,text="Створити запис").grid(row=0,column=0)
                Label(Change,text="Таблиця").grid(row=1,column=0)
                table=Entry(Change,width=40)
                table.grid(row=2,column=0)
                Label(Change,text="c").grid(row=3,column=0)
                val=Entry(Change,width=40)
                val.grid(row=4,column=0)
                Button(Change,text="Створити",command= lambda: PostgreSQL.insert2Db(table.get(),','.join(str(val.get())))).grid(row=7,column=0)

            def Export():
                Change=Toplevel(root)
                Change.title("Export")
                Label(Change,text="Export").grid(row=0,column=0)
                Label(Change,text="Таблиця").grid(row=1,column=0)
                table = Entry(Change,width=40)
                table.grid(row=2,column=0)
                Label(Change,text="б").grid(row=3,column=0)
                oldV=Entry(Change,width=40)
                oldV.grid(row=4,column=0)
                Label(Change,text="б").grid(row=5,column=0)
                newV=Entry(Change,width=40)
                newV.grid(row=6,column=0)
                Button(Change,text="Export",command=lambda:PostgreSQL.pos2liteFunc(table.get())).grid(row=7,column=0)

            def Import():
                Change=Toplevel(root)
                Change.title("Import")
                Label(Change,text="Import").grid(row=0,column=0)
                Label(Change,text="a").grid(row=1,column=0)
                table = Entry(Change, width=40)
                table.grid(row=2, column=0)
                Label(Change, text="a").grid(row=3, column=0)
                oldV = Entry(Change, width=40)
                oldV.grid(row=4, column=0)
                Label(Change, text="a").grid(row=5, column=0)
                newV = Entry(Change, width=40)
                newV.grid(row=6, column=0)
                Button(Change, text="Export", command=lambda: PostgreSQL.pos2liteFunc(table.get())).grid(row=7,column=0)

            crud=Toplevel(root)
            crud.title("USER")
            Button(crud,text="Показати Базу Даних", width=20, height=3, command=UpdateBD).grid(row=0,column=0)
            Button(crud, text="Змінити Базу Даних", width=20, height=3, command=ChangeBD).grid(row=1, column=0)
            Button(crud, text="Створити Базу Даних", width=20, height=3, command=CreateBD).grid(row=2, column=0)
            Button(crud, text="Видалити Базу Даних", width=20, height=3, command=DeleteBD).grid(row=3, column=0)
            Button(crud, text="Експорт БД", width=20, height=3, command=Export).grid(row=4, column=0)
            Button(crud, text="Імпорт БД", width=20, height=3, command=Import).grid(row=5, column=0)

if __name__ == "__main__":
    root = Tk()
    root.title("Головне меню")
    start = Main()
    root.mainloop()

