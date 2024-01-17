"""
Python program which will track your notes:
    1. Function to display the list of notes
    2. Function to add a note to the list of notes with date and time
    3. Function to remove a note from the list of notes
    4. Function to edit a note based by index
    5. Function to save the list of notes as a excel file 
    6. Function to load the list of notes from a excel file
    7. Program controls
"""
import datetime
import csv
import os


def display_note_list(note_list):
    '''Display the list of notes'''

    if not note_list:
        print("List of notes are empty!")
    else:
        print("Your list of notes:")
        for note in note_list:
            print("________________")
            print(f"ID: {note['id']}"
                  f"\nCreation Date: {note['reg_date']}"
                  f"\nUpdate Date: {note['edit_date']}"
                  f"\nUser: {note['user']}"
                  f"\nNote: {note['note']}"
                  f"\nDue Date: {note['due_date']}"
                  f"\nDue Time: {note['due_time']}")
            print("________________")


def add_note(note_list, full_date, note, due_date, due_time):
    '''Add a note to the list'''

    note_list.append({
        'id': len(note_list) + 1,
        'reg_date': full_date,
        'edit_date': "",
        'user': os.getlogin(),
        'note': note,
        'due_date': due_date,
        'due_time': due_time,
    })
    print(f"Note with id number {note_list[-1]['id']} added to the list of notes "
          f"with due date {due_date} and due time {due_time}.")


def remove_note(note_list, full_date):
    '''Remove a note based by note ID number'''

    if not note_list:
        print("Cannot remove. List of notes are empty!")
    else:
        print("Your list of notes:")
        for note in note_list:
            print(f"ID: {note['id']}. {note['note']}.")

        print("Choose a note you want to edit. Type ID number (1 - ", end="")
        print(f"{len(note_list)}):", end=" ")
        note_id = int(str.strip(input()))

        if 1 <= note_id <= len(note_list):
            note_id -= 1
            note_list.remove(note_list[note_id])

            print(f"Note with ID number - {note_id + 1} "
                  f"has been removed from the list on {full_date}.")
        else:
            print("Invalid note ID number. Enter a valid number")


def edit_note(note_list, full_date):
    '''Edit a note based by note ID number'''

    if not note_list:
        print("Cannot edit. List of notes are empty!")
    else:
        print("Your list of notes:")
        for note in note_list:
            print(f"ID: {note['id']}. {note['note']}.")

        print("Choose a note you want to edit. Type ID number (1 - ", end="")
        print(f"{len(note_list)}):", end=" ")
        note_id = int(str.strip(input()))

        if 1 <= note_id <= len(note_list):
            note_id -= 1
            print(f"Your note: {note_list[note_id]['note']}")
            note = str.strip(input("Edit the note: "))

            print(f"Due date: {note_list[note_id]['due_date']} ->", end=" ")
            due_date = str.strip(input()) or note_list[note_id]['due_date']

            print(f"Due time: {note_list[note_id]['due_time']} ->",  end=" ")
            due_time = str.strip(input()) or note_list[note_id]['due_time']
            edit_date = full_date

            note_list[note_id]['note'] = note
            note_list[note_id]['due_date'] = due_date
            note_list[note_id]['due_time'] = due_time
            note_list[note_id]['edit_date'] = edit_date

            print(f"Note with ID number - {note_list[note_id]['id']} "
                  f"has been updated in the list on {note_list[note_id]['edit_date']}.")
        else:
            print("Invalid note ID number. Enter a valid number")


def save_to_csv(note_list, filename='notes_db.csv'):
    '''Save notes to the csv file'''

    header = list(note_list[0].keys())

    with open(filename, 'w', encoding='UTF8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(note_list)


def load_from_csv(filename='notes_db.csv'):
    '''Read data from csv to the list'''

    note_list = []

    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTF8') as file:
            csv_reader = csv.reader(file)
            for line_no, line in enumerate(csv_reader, 1):
                if line_no == 1:
                    header = line
                else:
                    note_list.append(dict(zip(header, line)))
    return note_list


def main():
    '''Controller of the program'''

    note_list = load_from_csv()

    while True:
        now = datetime.datetime.now()
        full_date = now.strftime("%Y-%m-%d %H:%M:%S")
        now_date = now.strftime("%Y-%m-%d")
        now_time = now.strftime("%H:%M")

        print("\n1. Display list of notes")
        print("2. Add a note")
        print("3. Remove a note")
        print("4. Edit note in the list")
        print("5. Exit the program")

        choice = str.strip(input("Enter your choose (From 1-5): "))

        if choice == "1":
            display_note_list(note_list)
        elif choice == "2":
            note = input("Enter the note: ")
            due_date = input(
                f"Enter the due date (ex. {now_date}): ") or now_date
            due_time = input(
                f"Enter the due time (ex. {now_time}): ") or now_time
            add_note(note_list, full_date, note, due_date, due_time)
        elif choice == "3":
            remove_note(note_list, full_date)
        elif choice == "4":
            edit_note(note_list, full_date)
        elif choice == "5":
            save_to_csv(note_list)
            print("List of notes saved to 'csv' file. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
