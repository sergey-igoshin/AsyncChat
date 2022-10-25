from subprocess import Popen, CREATE_NEW_CONSOLE
import time

# CLIENT = 2
SET_TIME_OUT = 0.2


def clients():
    num = int(input("Укажите кол-во клиентов от 2 до 9\n> "))
    try:
        if 0 < num <= 9:
            return num
        else:
            print('Неверный диапозон')
            clients()
    except Exception as e:
        print(e)
        clients()
    except KeyboardInterrupt:
        pass


def main():
    process_list = []
    CLIENT = clients()
    try:
        while True:
            print("Запустить программу (start) / Остановить программу (stop)")
            action = input("> ").lower()
            if action == 'stop':
                for p in process_list:
                    time.sleep(SET_TIME_OUT)
                    p.kill()
                process_list.clear()
                break
            elif action == 'start':
                process_list.append(Popen('python server.py'))
                time.sleep(SET_TIME_OUT)
                for _ in range(CLIENT):
                    process_list.append(Popen('python client.py', creationflags=CREATE_NEW_CONSOLE))
            else:
                print('Команда не распознана')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
