# Задание 1
# Создайте класс очереди для работы с символьными значениями
from tkinter import *
from tkinter import messagebox


class Queue:
    __queue_list = list()                   # Список # для хранения элементов queue
    __capacity = 0                          # максимальная емкость queue
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
            messagebox.showinfo('Задание 1. Очередь', 'Очередь не заполнена! Завершение процесса')
            exit(-1)
        x = self.__queue_list.pop(0)
        messagebox.showinfo('Задание 1. Очередь', f'Удаляем элемент: {x}')
        self.__queue_list.append(None)
        self.__count -= 1
        return x

    # Функция добавления элемента в queue
    def enqueue(self, value: any):
        # проверка на переполнение queue
        if self.isFull():
            messagebox.showinfo('Задание 1. Очередь', 'Переполнение очереди! Элемент в очередь не добавлен.')
        else:
            index = 0
            while self.__queue_list[index] == None and index != (self.__capacity - 1):
                index += 1
            messagebox.showinfo('Задание 1. Очередь', f'Добавляем элемент: {value}')
            self.__queue_list.pop(0)
            self.__queue_list.append(value)
            self.__count += 1

    # Функция для проверки, пуста ли queue или нет
    def isEmpty(self):
        return self.__count == 0

    # Функция проверки заполнения queue.
    def isFull(self):
        return self.__count == self.__capacity

    def show(self):
        return self.__queue_list


# if __name__ == '__main__':
#     # функция ввода длины очереди (начало работы)
#     def enter_queue_size():
#         global q
#         q = Queue(int(len_queue_entry.get()))
#
#
#     # функция кнопки проверки на пустоту
#     def click_isempty():
#         if q.isEmpty() == False:
#             messagebox.showinfo('Задание 1. Очередь', f'{q.isEmpty()} - Очередь не пуста')
#         else:
#             messagebox.showinfo('Задание 1. Очередь', f'{q.isEmpty()} - Очередь пуста')
#
#
#     # функция выводит сообщение о заполненности очереди
#     def click_isfull():
#         if q.isFull() == True:
#             messagebox.showinfo('Задание 1. Очередь', f'{q.isFull()} - Очередь заполнена')
#         else:
#             messagebox.showinfo('Задание 1. Очередь', f'{q.isFull()} - Очередь не заполнена')
#
#
#     # функция выводит сообщение со списком очереди
#     def click_show():
#         messagebox.showinfo('Задание 1. Очередь', f'Список очереди: {q.show()}')
#
#
#     # функция кнопки добавления элемента
#     def click_enqueue():
#         return q.enqueue(enqueue_label_entry.get())
#
#
#     # функция кнопки удаления элемента
#     def click_dequeue():
#         return q.dequeue()
#
#
#     # функция завершения работы
#     def click_exit():
#         messagebox.showinfo('Задание 1. Очередь', 'ЗАВЕРШЕНИЕ РАБОТЫ')
#         exit(-1)
#
#
#     # очистка полей ввода
#     def clear():
#         len_queue_entry.delete(0, END)
#         enqueue_label_entry.delete(0, END)
#
#
#     root = Tk()
#     root.title('Задание 1. Очередь')
#     root.geometry('700x500')
#
#     len_queue_label = Label(text='Введите длину очереди ', width=20, font=5)
#     enqueue_label = Label(text='Добавления в очередь ', width=20, font=5)
#
#     len_queue_label.grid(row=0, column=0)
#     enqueue_label.grid(row=1, column=0)
#
#     len_queue_entry = Entry()
#     enqueue_label_entry = Entry()
#
#     len_queue_entry.grid(row=0,column=1, padx=20, pady=5)
#     enqueue_label_entry.grid(row=1,column=1, padx=20, pady=5)
#
#     # вставка начальных данных
#     len_queue_entry.insert(0, '0')
#     enqueue_label_entry.insert(0, '0')
#
#     enter_queue_size_button = Button(text='Ввести длину очереди', background="#555", foreground="#ccc",
#                  padx="10", pady="8", width="20", font="5",  command=enter_queue_size)
#     enqueue_button = Button(text='Добавить в очередь', background="#555", foreground="#ccc",
#                  padx="10", pady="8", width="20", font="5",  command=click_enqueue)
#     dequeue_button = Button(text='Удалить из очереди', background="#555", foreground="#ccc",
#                  padx="10", pady="8", width="20", font="5",  command=click_dequeue)
#     clear_button = Button(text='Очистить данные', background="#555", foreground="#ccc",
#                  padx="20", pady="8", width="20", font="5", command=clear)
#
#     enter_queue_size_button.grid(row=0, column=2, padx=10, pady=5)
#     enqueue_button.grid(row=1, column=2, padx=10, pady=5)
#     dequeue_button.grid(row=2, column=2, padx=10, pady=5)
#     clear_button.grid(row=6, column=2, padx=10, pady=5)
#
#     btn_isempty = Button(text="IsEmpty\nПроверка очереди на пустоту", background="#555", foreground="#ccc",
#                  padx="20", pady="8", width="25", font="5", command=click_isempty)
#     btn_isfull = Button(text="IsFull\nпроверка очереди на заполнение", background="#555", foreground="#ccc",
#                  padx="20", pady="8", width="25", font="5", command=click_isfull)
#     btn_show = Button(text="Show\nВывести список очереди", background="#555", foreground="#ccc",
#                  padx="20", pady="8", width="25", font="5", command=click_show)
#     btn_exit = Button(text="Выход из программы", background="#555", foreground="#ccc",
#                  padx="20", pady="8", width="20", font="5", command=click_exit)
#     btn_isempty.grid(row=4, column=0, padx=10, pady=5)
#     btn_isfull.grid(row=5, column=0, padx=10, pady=5)
#     btn_show.grid(row=6, column=0, padx=10, pady=5)
#     btn_exit.grid(row=7, column=2, padx=10, pady=5)
#
#     root.mainloop()

# Задание 2
# Создайте класс очереди с приоритетами для работы с символьными значениями.


class QueuePriority:
    __queue_list = list()                   # Список # для хранения элементов queue
    __priority_list = list()                # Список приоритетов
    __capacity = 0                          # максимальная емкость queue
    __count = 0                             # текущий размер queue

    # Инициализировать queue
    def __init__(self, size: int):
        self.__capacity = size     # максимальная емкость queue
        self.__queue_list = [None] * size
        self.__priority_list = [0] * size

    def get_capacity(self):
        return self.__capacity

    # Функция элемента с приоритетом из очереди
    def pull_highest_priority_element(self):
        # проверка на опустошение queue
        if self.isEmpty():
            messagebox.showinfo('Задание 2. Очередь с приоритетом',
                                'Очередь не заполнена! Завершение процесса')
            exit(-1)
        max_priority = max(self.__priority_list)
        x = self.__priority_list.index(max_priority)
        messagebox.showinfo('Задание 2. Очередь с приоритетом',
                            f'Удаляем элемент: {self.__queue_list[x]} '
                            f'с приоритетом {self.__priority_list[x]}')
        self.__queue_list.pop(x)
        self.__priority_list.pop(x)
        self.__queue_list.append(None)
        self.__priority_list.append(0)
        self.__count -= 1

    # Функция добавления элемента с приоритетом в queue
    def insert_with_priority(self, value: any, priority: int):
        # проверка на переполнение queue
        if self.isFull():
            messagebox.showinfo('Задание 2. Очередь с приоритетом',
                                'Переполнение очереди! Элемент в очередь не добавлен.')
        else:
            index = 0
            while self.__queue_list[index] == None and index != (self.__capacity - 1):
                index += 1

            messagebox.showinfo('Задание 2. Очередь с приоритетом',
                                f'Добавляем элемент: {value} '
                                f'с приоритетом {priority}')
            index_none = self.__queue_list.index(None)
            self.__queue_list.pop(index_none)
            self.__queue_list.append(value)
            self.__priority_list.pop(index_none)
            self.__priority_list.append(priority)
            self.__count += 1

    # получаем элемент с максимальным приоритетом
    def peek(self):
        max_priority = max(self.__priority_list)
        x = self.__priority_list.index(max_priority)
        messagebox.showinfo('Задание 2. Очередь с приоритетом',
                            f'Элемент с максимальным приоритетом: {self.__queue_list[x]} '
                            f'с приоритетом: {self.__priority_list[x]}')
        return self.__queue_list[x]

    # Функция для проверки, пуста ли queue или нет
    def isEmpty(self):
        return self.__count == 0

    # Функция проверки заполнения queue.
    def isFull(self):
        return self.__count == self.__capacity

    def show(self):
        return self.__queue_list

    def show_priority(self):
        return self.__priority_list


# q_p = QueuePriority(5)
# q_p.insert_with_priority('g', 2)
# q_p.insert_with_priority(1, 10)
# print(q_p.show())
# q_p.pull_highest_priority_element()
# print(q_p.show())


if __name__ == '__main__':
    # функция ввода длины очереди (начало работы)
    def enter_queue_size():
        global q_priority
        q_priority = QueuePriority(int(len_queue_entry.get()))


    # функция кнопки проверки на пустоту
    def click_isempty():
        if q_priority.isEmpty() == False:
            messagebox.showinfo('Задание 2. Очередь с приоритетом', f'{q_priority.isEmpty()} - Очередь не пуста')
        else:
            messagebox.showinfo('Задание 2. Очередь с приоритетом', f'{q_priority.isEmpty()} - Очередь пуста')


    # функция выводит сообщение о заполненности очереди
    def click_isfull():
        if q_priority.isFull() == True:
            messagebox.showinfo('Задание 2. Очередь с приоритетом', f'{q_priority.isFull()} - Очередь заполнена')
        else:
            messagebox.showinfo('Задание 2. Очередь с приоритетом', f'{q_priority.isFull()} - Очередь не заполнена')


    # функция выводит сообщение со списком очереди
    def click_show():
        messagebox.showinfo('Задание 2. Очередь с приоритетом', f'Список очереди: {q_priority.show()}')


    # функция кнопки добавления элемента
    def click_enqueue():
        return q_priority.insert_with_priority(enqueue_label_entry.get(),
                                               int(priority_label_entry.get()))


    # функция кнопки удаления элемента
    def click_dequeue():
        return q_priority.pull_highest_priority_element()


    # функция кнопки получения элемента с максимальным приоритетом
    def click_peek():
        q_priority.peek()


    # функция завершения работы
    def click_exit():
        messagebox.showinfo('Задание 2. Очередь с приоритетом', 'ЗАВЕРШЕНИЕ РАБОТЫ')
        exit(-1)


    # очистка полей ввода
    def clear():
        len_queue_entry.delete(0, END)
        enqueue_label_entry.delete(0, END)
        priority_label_entry.delete(0, END)


    root = Tk()
    root.title('Задание 2. Очередь с приоритетом')
    root.geometry('700x500')

    len_queue_label = Label(text='Введите длину очереди ', width=30, font=5)
    enqueue_label = Label(text='Добавления в очередь элемент ', width=30, font=5)
    priority_label = Label(text='Добавления в очередь приоритет', width=30, font=5)

    len_queue_label.grid(row=0, column=0)
    enqueue_label.grid(row=1, column=0)
    priority_label.grid(row=2, column=0)

    len_queue_entry = Entry()
    enqueue_label_entry = Entry()
    priority_label_entry = Entry()

    len_queue_entry.grid(row=0,column=1, padx=20, pady=5)
    enqueue_label_entry.grid(row=1,column=1, padx=20, pady=5)
    priority_label_entry.grid(row=2,column=1, padx=20, pady=5)

    # вставка начальных данных
    len_queue_entry.insert(0, '0')
    enqueue_label_entry.insert(0, '0')
    priority_label_entry.insert(0, 0)

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
    btn_peek = Button(text="Peek\nЭлемент с max приоритетом", background="#555", foreground="#ccc",
                 padx="20", pady="8", width="25", font="5", command=click_peek)
    btn_exit = Button(text="Выход из программы", background="#555", foreground="#ccc",
                 padx="20", pady="8", width="20", font="5", command=click_exit)
    btn_isempty.grid(row=4, column=0, padx=10, pady=5)
    btn_isfull.grid(row=5, column=0, padx=10, pady=5)
    btn_show.grid(row=6, column=0, padx=10, pady=5)
    btn_peek.grid(row=7, column=0, padx=10, pady=5)
    btn_exit.grid(row=7, column=2, padx=10, pady=5)

    root.mainloop()
