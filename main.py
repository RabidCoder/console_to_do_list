from datetime import datetime


tasks = []
num_id = 0


def show_tasks():
    """Выводит в консоль задачи."""
    if tasks:
        for task in tasks:
            print(task)
    else:
        print('У вас нет задач')


def add_task():
    """Добавляет новую задачу в список задач."""
    print('Добавим новую задачу!')
    title = input('Введите название задачи. Поле не может быть пустым.')
    description = input('Можем добавить описание задачи, но это необязательно)')
    priority = int(input('Необходимо установить приоритет задачи. 1 — высокий, 2 — средний, 3 — низкий. Обязательное поле.'))
    time_stamp = datetime.now()
    due_date = datetime.strptime(input('Введите дату и время дедлайна в формате dd.mm.yyyy hh:mm'), '%d.%m.%Y %H:%M')
    num_id += 1
    tasks.append({'id': num_id, 'title': title, 'description': description, 'priority': priority, 'time_stamp': time_stamp, 'due_time': due_date})


def edit_task():
    """Изменяет название, описание, приоритет или срок дедлайна задачи."""
    pass


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
    """Основная логика программы."""
    while True:
        print('To-Do List')
        print()
        print('Возможные действия')
        print()
        print('1. Показать задачи')
        print('2. Добавить задачу')
        print('3. Изменить задачу')
        print('4. Удалить задачу')
        print('5. Отметить задачу как выполненную')
        print('6. Выйти')
        print()
        
        num = int(input('Выберите действие (1-6)'))

        if num == 1:
            show_tasks()
        elif num == 2:
            add_task()
        elif num == 3:
            edit_task()
        elif num == 4:
            delete_task()
        elif num == 5:
            complete_task()
        elif num == 6:
            print('Завершение работы')
            break
        else:
            print('Неверный ввод, попробуйте снова')


if __name__ == '__main__':
    main()
