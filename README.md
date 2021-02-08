# tic-tac-toe-9000-tasks

### Как начать пользоваться этим проектом?
Ещё раз, последовательность действий, если вдруг у кого-то что-то не получилось.

0. Установите питон. https://www.python.org/downloads/windows/

    Для проверки в консоли можете написать
    
    ```bash
    python --version
    ```

1. Установите VSCode (или PyCharm, но VSCode мне нравится чуть больше для наших целей).

2. Установите Git (и Git Bash в Винде, они вроде вместе ставятся).

3. (только для винды). Установите в вашей IDE Git Bash как дефолтный терминал. 

    [VSCode](https://stackoverflow.com/questions/42606837/how-do-i-use-bash-on-windows-from-the-visual-studio-code-integrated-terminal) 

    [PyCharm](https://coderoad.ru/20573213/%D0%92%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-Git-bash-%D0%B2-PyCharm-%D0%BA%D0%B0%D0%BA-%D0%B2%D0%BD%D0%B5%D1%88%D0%BD%D0%B8%D0%B9-%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82-%D0%B8-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C-%D1%81-%D0%BD%D0%B8%D0%BC-%D0%B2-%D0%BE%D0%BA%D0%BD%D0%B5)

4. Клонируйте ваш репозиторий (вставьте ссылку на ваш репозиторий)!

    ```bash
    git clone https://github.com/VasyaPupkin/tic-tac-toe-9000-tasks.git
    ```

    Можете клонировать, указав папку, куда хотите клонировать. (~ - это домашняя директория вашего пользователя).

    ```bash
    git clone https://github.com/VasyaPupkin/tic-tac-toe-9000-tasks.git ~/my/favorite/folder
    ```

5. Откройте то, что склонировали как папку (или как проект) вашим редактором (IDE).

6. "Подключитесь" к оригинальному репозиторию, дабы иметь возможность брать оттуда задания.

    ```bash
    git remote add upstream https://github.com/DarkSquirrelComes/tic-tac-toe-9000-tasks.git
    ```

7. Небольшой гайд. 

    7.1.0 как создать ветку?
    
    ```bash
    git checkout -b my-branch
    ```

    7.1.1 как переключиться на ветку?
    
    ```bash
    git checkout my-branch
    ```

    7.2 Как выкачать свежее содержимое моей (Вадима Евгеньевича в смысле) ветки tasks?

    ```bash
    git checkout tasks
    git fetch upstream
    git rebase upstream/tasks
    ```

    7.3 Мне уже лень писать, вспомните/погуглите сами как работают команды...
    ```bash
    git status
    git add
    git commit
    git push
    ```
8. Добавьте меня как участника в настройках репозитория (гуглить add colaborator).

9. Когда внесёте в свой develop все свои изменения, сделайте pull-request в ваш же `main` и не забудьте добавить меня ревьюером! 

### Задание 1
Реализуйте все методы в https://github.com/DarkSquirrelComes/tic-tac-toe-9000-tasks/blob/main/game_engine/tic_tac_toe_game.py

Пример использования можете посмотреть в https://github.com/DarkSquirrelComes/tic-tac-toe-9000-tasks/blob/main/game_engine_test.py

Этот самый тест можно запустить или с помощью pytest
```bash
pytest test_game_engine.py
```
или просто выполнив функцию ```test_scenario()```.
