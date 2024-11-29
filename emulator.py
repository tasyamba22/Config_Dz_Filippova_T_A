import os
import tarfile
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import xml.etree.ElementTree as ET


class ShellEmulator:
    # Эмулятор shell, работающий с виртуальной файловой системой.
    def __init__(self, config_path):
        self.load_config(config_path)
        self.current_dir = "/"
        self.virtual_fs = {}
        self.load_virtual_fs()

    def load_config(self, config_path):
        # Загружает конфигурацию из XML-файла.
        tree = ET.parse(config_path)
        root = tree.getroot()
        self.username = root.find('username').text
        self.tar_path = root.find('tar_path').text

    def load_virtual_fs(self):
        # Загружает виртуальную файловую систему из tar-архива.
        with tarfile.open(self.tar_path, 'r') as tar:
            for member in tar.getmembers():
                normalized_path = member.name.lstrip("./")
                self.virtual_fs[member.name] = {
                    "is_file": member.isfile(),
                    "content": tar.extractfile(member).read() if member.isfile() else None,
                }


    def ls(self):
        # Список файлов и папок в текущей директории.
        items = []
        prefix =  self.current_dir.strip("/") + "/" if self.current_dir != "/" else ""
        for path in self.virtual_fs.keys():
            if path.startswith(prefix) and path != prefix:
                relative_path = path[len(prefix):].split("/")[0]
                if relative_path not in items:
                    items.append(relative_path)

        return "\n".join(sorted(items)) if items else "No files or directories found."


    def cd(self, path):
       # Переход в указанную директорию.
        if not path:  # Если аргумент пустой, переход в корень
            self.current_dir = "/"
            return ""
        if path == "..":  # Переход на уровень вверх
            self.current_dir = "/".join(self.current_dir.strip("/").split("/")[:-1]) or "/"
        elif path == "/":  # Переход в корень
            self.current_dir = "/"
        else:
            new_path = os.path.normpath(os.path.join(self.current_dir, path)).replace("\\", "/")
            new_path = new_path.strip("/")  # Удалить лишние /
            # Проверка существования директории
            if new_path in self.virtual_fs and not self.virtual_fs[new_path]["is_file"]:
                self.current_dir = "/" + new_path
            else:
                return f"cd: no such file or directory: {path}"
        return ""

    def cat(self, filename):
        # Читает и выводит содержимое файла.
        file_path = os.path.normpath(os.path.join(self.current_dir, filename)).replace("\\", "/")
        file_path = file_path.lstrip("./")  # Убираем "./", если есть
        if file_path in self.virtual_fs and self.virtual_fs[file_path]["is_file"]:
            # Нормализация содержимого для удаления лишних символов переноса строк
            return self.virtual_fs[file_path]["content"].decode().strip()
        return f"cat: {filename}: No such file or directory"

    def date(self):
        # Вывод текущей даты и времени.
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def clear(self):
        # Очищает экран.
        return "CLEAR"

    def exit(self):
        # Завершение работы эмулятора.
        return "EXIT"


class ShellGUI:
    # Графический интерфейс эмулятора.
    def __init__(self, master, emulator):
        self.master = master
        self.emulator = emulator

        self.master.title("Shell Emulator")
        self.text = ScrolledText(master, wrap='word', font=('Consolas', 12))
        self.text.pack(fill='both', expand=True)
        self.text.bind("<Return>", self.execute_command)
        self.prompt()

    def prompt(self):
        # Отображение приглашения для ввода команды.
        self.text.insert('end', f"{self.emulator.username}@shell:{self.emulator.current_dir}$ ")
        self.text.mark_set("insert", "end")
        self.text.see("end")

    def execute_command(self, event):
        # Выполнение команды, введенной пользователем.

        start_index = self.text.index("end-2c linestart")
        command_line = self.text.get(start_index, "end-1c").strip()

        prompt = f"{self.emulator.username}@shell:{self.emulator.current_dir}$ "
        if command_line.startswith(prompt):
            command = command_line[len(prompt):].strip()
        else:
            command = command_line.strip()

        if not command:
            return

        cmd, *args = command.split()
        output = ""

        if cmd == "ls":
            output = self.emulator.ls()
        elif cmd == "cd":
            output = self.emulator.cd(" ".join(args))
        elif cmd == "cat":
            output = self.emulator.cat(" ".join(args))
        elif cmd == "date":
            output = self.emulator.date()
        elif cmd == "clear":
            self.text.delete("1.0", "end")
            self.prompt()
            return
        elif cmd == "exit":
            self.master.destroy()
            return
        else:
            output = f"{cmd}: command not found"

        if output:
            self.text.insert("end", "\n" + output)
        self.text.insert("end", "\n")
        self.prompt()


def main():
    # Главная функция для запуска эмулятора.

    import sys
    if len(sys.argv) != 2:
        print("Usage: python emulator.py <config.xml>")
        sys.exit(1)

    config_path = sys.argv[1]
    emulator = ShellEmulator(config_path)

    root = tk.Tk()
    app = ShellGUI(root, emulator)
    root.mainloop()


if __name__ == "__main__":
    main()
