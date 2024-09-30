tasks = []


def show_tasks():
    if tasks:
        for name, status in tasks:
            print(name, status)
    else:
        print('У вас нет задач')


def add_task():
    print('Давай добавим новую задачу!')
    title = input('Введи название задачи. Поле не может быть пустым.')
    description = input('Можешь добавить описание задачи, но это необязательно)')
    status = int(input(
        '''Выбери цифру из перечня ниже для присвоения задаче статуса.
        1 - "новая" (задача только что создана и ещё не начата);
        2 - "в процессе" (задача в процессе выполнения);
        3 - "завершена" (задача выполнена);
        4 - "отменена" (задача была отменена и больше не актуальна)
    '''))
    priority = int(input('Установи приоритет задачи. 1 — высокий, 2 — средний, 3 — низкий. Обязательное поле.'))
    due_date = None # дата
    tasks.append({name: False})


def delete_task():
    task = input('Напишите уникальный набор символов или слов задачи, которую хотите удалить')
    for key in tasks:
        if task in key:
            tasks[key].pop()
            break
        else:
            print('Такой задачи нет')


def complete_task():
    task = input('Напишите уникальный набор символов или слов задачи, которую хотите удалить')
    for key in tasks:
        if task in key:
            tasks[key] = True
            break
        else:
            print('Такой задачи нет')


def main():
    while True:
        print('To-Do List')
        print('1. Показать все задачи')
        print('2. Добавить задачу')
        print('3. Удалить задачу')
        print('4. Отметить задачу как выполненную')
        print('5. Выйти')
        
        num = int(input('Выберите действие (1-5)'))

        if num == 1:
            show_tasks()
        elif num == 2:
            add_task()
        elif num == 3:
            delete_task()
        elif num == 4:
            complete_task()
        elif num == 5:
            print('Завершение работы')
            break
        else:
            print('Неверный ввод, попробуйте снова')


if __name__ == '__main__':
    main()