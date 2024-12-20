**Вариант №30**<br/>
**Задание №1**<br/>
Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу<br/>
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.<br/>
Эмулятор должен запускаться из реальной командной строки, а файл с<br/>
виртуальной файловой системой не нужно распаковывать у пользователя.<br/>
Эмулятор принимает образ виртуальной файловой системы в виде файла формата<br/>
tar. Эмулятор должен работать в режиме GUI.<br/>
***
Конфигурационный файл имеет формат xml и содержит:<br/>
• Имя пользователя для показа в приглашении к вводу.<br/>
• Путь к архиву виртуальной файловой системы.<br/>
Необходимо поддержать в эмуляторе команды `ls`, `cd` и `exit`, а также следующие команды:<br/>
1. `date`.<br/>
2. `cat`.<br/>
3. `clear`.<br/>
Все функции эмулятора должны быть покрыты тестами, а для каждой из<br/>
поддерживаемых команд необходимо написать 2 теста.<br/>
***
## 1. Общее описание<br/>
Shell Emulator — это эмулятор командной оболочки, который работает с виртуальной файловой системой, созданной из архива .tar. Этот проект реализует базовые функции командной оболочки, такие как
управление директориями, вывод содержимого файлов, вывод текущей даты и времени, очистка экрана и завершение работы.<br/>
Эмулятор предоставляет интерфейс командной строки с поддержкой следующих команд:<br/>
• `ls` — отображает список файлов и директорий в текущей директории.<br/>
• `cd` — смена текущей директории.<br/>
• `cat` — вывод содержимого файла.<br/>
• `date` — вывод текущей даты и времени.<br/>
• `clear` — очистка экрана.<br/>
• `exit` — завершение работы эмулятора.<br/>
## 2. Описание всех функций и настроек<br/>
**Основные классы:**<br/>
ShellEmulator — основной класс эмулятора, который управляет виртуальной файловой системой и обрабатывает команды.<br/>
ShellGUI — класс для графического интерфейса, который отображает командную строку и обрабатывает пользовательский ввод.<br/>
**Методы класса ShellEmulator:**<br/>
* __init__(self, config_path)<br/>
Инициализация эмулятора с указанием пути к конфигурационному файлу.<br/>
Загружает конфигурацию и виртуальную файловую систему из архива .tar.<br/>
* load_config(self, config_path)<br/>
Загружает конфигурацию из XML-файла, содержащего имя пользователя и путь к архиву .tar.<br/>
* load_virtual_fs(self)<br/>
Загружает виртуальную файловую систему из архива .tar.<br/>
* ls(self)<br/>
Выводит список файлов и директорий в текущей директории.<br/>
* cd(self, path)<br/>
Переход в указанную директорию.<br/>
* cat(self, filename)<br/>
Чтение и вывод содержимого файла.<br/>
* date(self)<br/>
Возвращает текущую дату и время в формате YYYY-MM-DD HH:MM:SS.<br/>
* clear(self)<br/>
Очищает экран.<br/>
* exit(self)<br/>
 Завершает работу эмулятора.<br/>

**Методы класса ShellGUI:** <br/>
* __init__(self, master, emulator)<br/>
Инициализирует графический интерфейс с использованием Tkinter.<br/>
* prompt(self)<br/>
Отображает командную строку с приглашением для ввода команды.<br/>
* execute_command(self, event)<br/>
Выполняет команду, введенную пользователем, и отображает результат.<br/>

## 3. Команды для сборки проекта<br/>
Скрипт использует стандартные библиотеки, поэтому дополнительных зависимостей не требуется.<br/>
TAR-файл, содержащий нужные файлы и директории для виртуальной файловой системы.<br/>
Файл config.xml с необходимыми параметрами.<br/>
## 4. Форматы данных <br/>
#### Конфигурационный файл (config.xml)<br/>
Пример:<br/>
```xml
<config>
    <username>user</username>
    <tar_path>virtual_fs.tar</tar_path>
</config>
```
`username` — имя пользователя для отображения в приглашении командной строки.<br/>
`tar_path` — путь к tar-архиву с файловой системой.<br/>
#### Файловая система (tar-архив)<br/>
Файлы и директории должны быть в tar-архиве, который эмулятор загружает при запуске.
#### Структура проекта:<br/>
`config.xml` — конфигурационный файл.<br/>
`emulator.py` — основной файл с эмулятором.<br/>
`test_emulator.py` — файл с юнит-тестами.<br/>
#### Запуск проекта:
```python
python emulator.py config.xml
```
#### Пример работы эмулятора:<br/>
![image](https://github.com/user-attachments/assets/835fe67a-495e-41e1-b4ad-817f6640d50f)
## 5. Результаты тестов<br/>
C:\Users\Taisi\PycharmProjects\Config_Dz\.venv\Scripts\python.exe "D:/PyCharm Community Edition 2024.3/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py" --path C:\Users\Taisi\PycharmProjects\Config_Dz\shell_emulator\test_emulator.py 
Testing started at 12:24 ...
Launching unittests with arguments python -m unittest C:\Users\Taisi\PycharmProjects\Config_Dz\shell_emulator\test_emulator.py in C:\Users\Taisi\PycharmProjects\Config_Dz\shell_emulator

Ran 11 tests in 0.075s

OK

Process finished with exit code 0
![image](https://github.com/user-attachments/assets/ff51f8fc-7a20-46f7-917f-065b2481ed2d)


