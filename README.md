Вариант №30<br/>
Задание №1<br/>
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
Необходимо поддержать в эмуляторе команды ls, cd и exit, а также<br/>
следующие команды:<br/>
1. date.<br/>
2. cat.<br/>
3. clear.<br/>

Все функции эмулятора должны быть покрыты тестами, а для каждой из<br/>
поддерживаемых команд необходимо написать 2 теста.<br/>
***
