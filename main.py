from datetime import datetime


tasks = []
num_id = 0


def find_task(phrase):
    if tasks:
        for task in tasks:
            if phrase in task['title']:
                return task
        else:
            print('Такой задачи нет. Попробуйте снова')
            find_task(phrase)


def show_tasks():
    """Выводит в консоль задачи."""
    if tasks:
        for task in tasks:
            print(task)
    else:
        print('У вас нет задач')


def add_task():
    """Добавляет новую задачу в список задач."""
    num_id += 1
    title = ''
    print('Добавим новую задачу!')
    while title.strip() == '':
        title = input('Название задачи: ')
    description = input('Описание задачи: ')
    priority = int(input('Приоритет задачи. 1 — высокий, 2 — средний, 3 — низкий: '))
    time_stamp = datetime.now()
    due_date = datetime.strptime(
        input('Дата и время дедлайна в формате dd.mm.yyyy hh:mm: '), '%d.%m.%Y %H:%M'
    )
    tasks.append({
        'id': num_id,
        'название_задачи': title,
        'описание': description,
        'приоритет': priority,
        'время_создания': time_stamp,
        'дедлайн': due_date,
        'статус_выполнения': 'В работе'
    })


CHANGED_DATA = {
    1: task['title'] = input('Название задачи: '),
    2: task['description'] = input('Описание задачи: '),
    3: task['priority'] = int(input(
        'Приоритет задачи. 1 — высокий, 2 — средний, 3 — низкий: '
    )),
    4: task['due_time'] = datetime.strptime(input(
        'Дата и время дедлайна в формате dd.mm.yyyy hh:mm'), '%d.%m.%Y %H:%M'
    )
}


def edit_task():
    """Изменяет название, описание, приоритет или срок дедлайна задачи."""
    phrase = input(
        'Напишите уникальный набор символов или слов задачи, которую хотите изменить'
    )
    task = find_task(phrase)
    
    while True:
        print('Параметры задачи для изменения')
        print()
        print('1. Название задачи')
        print('2. Описание задачи')
        print('3. Приоритет задачи')
        print('4. Дедлайн')
        print('5. Завершить изменение задачи' )
        
        number_command = int(input('Выберите действие (1-5)'))

        if number_command in CHANGED_DATA:
            if number_command == 1:
                while task['title'].strip() == '':
                    CHANGED_DATA[number_command]
            else:
                CHANGED_DATA[number_command]
            print('Успешно изменено')
        elif number_command == 5:
            print('Изменение задачи завершено')
            break
        else:
            print('Неверный ввод, попробуйте снова')
            

def delete_task():
    phrase = input(
        'Напишите уникальный набор символов или слов задачи, которую хотите удалить'
    )
    task = find_task(phrase)
    for t in range(len(tasks)):
        if task['id'] == tasks[t]['id']:
            del tasks[t]


def complete_task():
    phrase = input(
        'Напишите уникальный набор символов или слов задачи, статус которой хотите изменить'
    )
    task = find_task(phrase)
    task['статус_выполнения'] = 'Выполнена'


COMMANDS = {
     1: show_tasks(),
     2: add_task(),
     3: edit_task(),
     4: delete_task(),
     5: complete_task()
}


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
        
        number_command = int(input('Выберите действие (1-6)'))

        if number_command in COMMANDS:
            COMMANDS[number_command]
        elif number_command == 6:
            print('Завершение работы')
            break
        else:
            print('Неверный ввод, попробуйте снова')


if __name__ == '__main__':
    main()
