import json
import datetime

# Функция для чтения заметок из файла
def read_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

# Функция для добавления новой заметки
def add_note():
    notes = read_notes()
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "date": date
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена!")

# Функция для вывода всех заметок
def display_notes():
    notes = read_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата: {note['date']}")
        print()

# Функция для редактирования заметки по ID
def edit_note():
    notes = read_notes()
    note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note['title'] = title
            note['body'] = body
            note['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована!")
            return
    print(f"Заметка с ID {note_id} не найдена.")

# Функция для удаления заметки по ID
def delete_note():
    notes = read_notes()
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            return
    print(f"Заметка с ID {note_id} не найдена.")

# Главная функция пользовательского интерфейса
def main():
    while True:
        print("Выберите действие:")
        print("1. Добавить заметку")
        print("2. Вывести все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Введите номер действия: ")
        
        if choice == '1':
            add_note()
        elif choice == '2':
            display_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()