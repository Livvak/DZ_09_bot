from pprint import pprint

data = dict()
data = {
    "kkk": "575678567",
    "lll": "67845643789",
    "mmm": "657965798"
}
def check_empty_cmd(cmd: str) -> bool:
    if not cmd:
        # Проверяем наличие команды
        print("Empty line")
        return True

def check_cmd(cmd: str) -> bool:
    cmd_list = ["hello", "add", "change", "phone", "show all", "good bye", "close", "exit"]
    for command in cmd_list:
        # Проверка соответствия команды
        if command in cmd:
            flag = True
            break
            # return func(cmd)
        else:
            flag = False
    if flag == False:
        print(f"You need use only this commands {', '.join(cmd_list)}")
    return flag

def check_len_command(cmd: str) -> bool:
    # Перевірка довжини команди
    if "add" in cmd or "change" in cmd:
        count = cmd.split()
        if len(count) != 3:
            print("Формат команди: add/change name phone_number ")
            return True
    elif "hello" in cmd or "close" in cmd or "exit" in cmd:
        count = cmd.split()
        if len(count) != 1:
            print("Формат команди: hello or close or exit")
            return True
    elif "show all" in cmd or "good bye" in cmd or "phone" in cmd:
        count = cmd.split()
        if len(count) != 2:
            print("Формат команди: show all or good bye or phone number")
            return True

def check_type(cmd: str) -> bool:
    # Проверяем тип данных в add change

    if "add" in cmd or "change" in cmd:
        name = cmd.split()[1]
        phone = cmd.split()[2]
        if not name.isalpha():
            print("В імені повинні бути лише літери")
            return True
        if not phone.isdigit():
            print("В номері повинні бути лише цифри")
            return True
        # Проверяем тип данных в phone

    if "phone" in cmd:
        phone = cmd.split()[1]
        if not phone.isalpha():
            print("В імені повинні бути лише літери")
            return True

def input_error(func):
    def inner(cmd):
        cmd = cmd.lower()
        if check_empty_cmd(cmd):
            return True
        flag = check_cmd(cmd)
        if flag == False:
            return True
            # return func(cmd)
        if check_len_command(cmd):
            return True

        if check_type(cmd):
            return True

        if flag == True:
            return func(cmd)

    return inner


@input_error
def check_command(cmd: str) -> bool:
    # cmd = cmd.lower()
    # cmd_list = ["hello", "add", "change", "phone", "show all", "good bye", "close", "exit"]
    if cmd == 'hello':
        print("How can I help you?")
    elif cmd == "good bye" or cmd == "close" or cmd == "exit":
        print("Good bye!")
        return False
    elif "add" in cmd or "change" in cmd:
        name = cmd.split()[1]
        phone = cmd.split()[-1]
        data[name] = phone
    elif "phone" in cmd:
        name = cmd.split()[1]
        print(data[name])
    elif "show all" == cmd:
        pprint(data)
    return True


def main():
    while True:
        cmd = input("Введите комманду: ")
        if check_command(cmd) == False:
            break


if __name__ == "__main__":
    main()
