# Задание 1
# Создайте класс очереди для работы с символьными значениями
from tkinter import *
from tkinter import messagebox


class Queue:
    __queue_list = list()                   # Список # для хранения элементов queue
    __capacity = 0                          # максимальная емкость queue
    __front = 0                             # front указывает на передний элемент в queue
    __rear = -1                             # сзади указывает на последний элемент в queue
    __count = 0                             # текущий размер queue

    # Инициализировать queue
    def __init__(self, size: int):
        self.__capacity = size     # максимальная емкость queue
        self.__queue_list = [None] * size

    def get_capacity(self):
        return self.__capacity

    # Функция удаления переднего элемента из очереди
    def dequeue(self):
        # проверка на опустошение queue
        if self.isEmpty():
            # print('Очередь не заполнена! Завершение процесса')
            messagebox.showinfo('Задание 1. Очередь', 'Очередь не заполнена! Завершение процесса')
            exit(-1)
        x = self.__queue_list[self.__front]
        messagebox.showinfo('Задание 1. Очередь', f'Удаляем элемент: {x}')
        # print('Удаляем элемент: ', x)
        self.__front = (self.__front + 1) % self.__capacity
        self.__count = self.__count - 1
        return x

    # Функция добавления элемента в queue
    def enqueue(self, value: any):
        # проверка на переполнение queue
        if self.isFull():
            # print('Переполнение очереди! Элемент в очередь не добавлен.')
            messagebox.showinfo('Задание 1. Очередь', 'Переполнение очереди! Элемент в очередь не добавлен.')
        else:
            # print('Добавляем элемент: ', value)
            messagebox.showinfo('Задание 1. Очередь', f'Добавляем элемент: {value}')
            self.__rear = (self.__rear + 1) % self.__capacity
            self.__queue_list[self.__rear] = value
            self.__count = self.__count + 1

    # Функция возврата размера queue
    def size(self):
        return self.__count

    # Функция для проверки, пуста ли queue или нет
    def isEmpty(self):
        return self.size() == 0

    # Функция проверки заполнения queue.
    def isFull(self):
        return self.size() == self.__capacity

    def show(self):
        return self.__queue_list


# функция ввода длины очереди (начало работы)
def enter_queue_size():
    global q
    q = Queue(int(len_queue_entry.get()))


# функция кнопки проверки на пустоту
def click_isempty():
    if q.isEmpty() == False:
        messagebox.showinfo('Задание 1. Очередь', f'{q.isEmpty()} - Очередь не пуста')
    else:
        messagebox.showinfo('Задание 1. Очередь', f'{q.isEmpty()} - Очередь пуста')


# функция выводит сообщение о заполненности очереди
def click_isfull():
    if q.isFull() == True:
        messagebox.showinfo('Задание 1. Очередь', f'{q.isFull()} - Очередь заполнена')
    else:
        messagebox.showinfo('Задание 1. Очередь', f'{q.isFull()} - Очередь не заполнена')


# функция выводит сообщение со списком очереди
def click_show():
    messagebox.showinfo('Задание 1. Очередь', f'Список очереди: {q.show()}')


# функция кнопки добавления элемента
def click_enqueue():
    return q.enqueue(enqueue_label_entry.get())


# функция кнопки удаления элемента
def click_dequeue():
    return q.dequeue()


# функция завершения работы
def click_exit():
    messagebox.showinfo('Задание 1. Очередь', 'ЗАВЕРШЕНИЕ РАБОТЫ')
    exit(-1)


# очистка полей ввода
def clear():
    len_queue_entry.delete(0, END)
    enqueue_label_entry.delete(0, END)


root = Tk()
root.title('Задание 1. Очередь')
root.geometry('700x500')

len_queue_label = Label(text='Введите длину очереди ', width=20, font=5)
enqueue_label = Label(text='Добавления в очередь ', width=20, font=5)

len_queue_label.grid(row=0, column=0)
enqueue_label.grid(row=1, column=0)

len_queue_entry = Entry()
enqueue_label_entry = Entry()

len_queue_entry.grid(row=0,column=1, padx=20, pady=5)
enqueue_label_entry.grid(row=1,column=1, padx=20, pady=5)

# вставка начальных данных
len_queue_entry.insert(0, '0')
enqueue_label_entry.insert(0, '0')

enter_queue_size_button = Button(text='Ввести длину очереди', background="#555", foreground="#ccc",
             padx="10", pady="8", width="20", font="5",  command=enter_queue_size)
enqueue_button = Button(text='Добавить в очередь', background="#555", foreground="#ccc",
             padx="10", pady="8", width="20", font="5",  command=click_enqueue)
dequeue_button = Button(text='Удалить из очереди', background="#555", foreground="#ccc",
             padx="10", pady="8", width="20", font="5",  command=click_dequeue)
clear_button = Button(text='Очистить данные', background="#555", foreground="#ccc",
             padx="20", pady="8", width="20", font="5", command=clear)

enter_queue_size_button.grid(row=0, column=2, padx=10, pady=5)
enqueue_button.grid(row=1, column=2, padx=10, pady=5)
dequeue_button.grid(row=2, column=2, padx=10, pady=5)
clear_button.grid(row=6, column=2, padx=10, pady=5)

btn_isempty = Button(text="IsEmpty\nПроверка очереди на пустоту", background="#555", foreground="#ccc",
             padx="20", pady="8", width="25", font="5", command=click_isempty)
btn_isfull = Button(text="IsFull\nпроверка очереди на заполнение", background="#555", foreground="#ccc",
             padx="20", pady="8", width="25", font="5", command=click_isfull)
btn_show = Button(text="Show\nВывести список очереди", background="#555", foreground="#ccc",
             padx="20", pady="8", width="25", font="5", command=click_show)
btn_exit = Button(text="Выход из программы", background="#555", foreground="#ccc",
             padx="20", pady="8", width="20", font="5", command=click_exit)
btn_isempty.grid(row=4, column=0, padx=10, pady=5)
btn_isfull.grid(row=5, column=0, padx=10, pady=5)
btn_show.grid(row=6, column=0, padx=10, pady=5)
btn_exit.grid(row=7, column=2, padx=10, pady=5)

root.mainloop()


