def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid command."

    return wrapper


def handle_hello():
    return "How can I help you?"


@input_error
def handle_add(name, phone, contacts):
    contacts[name] = phone
    return "Contact added successfully."


@input_error
def handle_change(name, phone, contacts):
    contacts[name] = phone
    return "Phone number changed successfully."


@input_error
def handle_phone(name, contacts):
    return contacts[name]


def handle_show_all(contacts):
    if not contacts:
        return "No contacts found."
    output = ""
    for name, phone in contacts.items():
        output += f"{name}: {phone}\n"
    return output.strip()


def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").lower()
        if command == "hello":
            response = handle_hello()
        elif command.startswith("add"):
            _, name, phone = command.split()
            response = handle_add(name, phone, contacts)
        elif command.startswith("change"):
            _, name, phone = command.split()
            response = handle_change(name, phone, contacts)
        elif command.startswith("phone"):
            _, name = command.split()
            response = handle_phone(name, contacts)
        elif command == "show all":
            response = handle_show_all(contacts)
        elif command in ["good bye", "close", "exit"]:
            response = "Good bye!"
            break
        else:
            response = "Invalid command."
        print(response)


if __name__ == "__main__":
    main()
