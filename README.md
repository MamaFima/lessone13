```markdown
# Парсеры на Python для работы с Википедией

В данном репозитории представлены два проекта на основе библиотеки `selenium`, которые позволяют взаимодействовать с Википедией через автоматизированные браузерные сессии. Эти скрипты предоставляют возможности для поиска статей, чтения параграфов и перехода по связанным ссылкам.

## Описание проектов

### 1. **Интерактивный парсер статей Википедии**
Этот проект предназначен для поиска статей в Википедии, чтения их содержания и перехода к связанным статьям. Особенности:
- Пользователь вводит запрос для поиска информации.
- Скрипт находит статью по указанному запросу и открывает её.
- Возможность:
  - Просматривать параграфы текущей статьи.
  - Переходить к случайным связанным статьям.
- Реализована проверка наличия связанных ссылок через элементы на странице.
- Используется библиотека `selenium` для управления браузером.

### 2. **Расширенный парсер с обработкой связанных статей**
Этот проект включает более сложную обработку связанных ссылок и предоставляет гибкие возможности:
- Поиск и открытие статей, связанных с заданным запросом.
- Чтение текста параграфов из статьи.
- Обработка раздела «См. также» для нахождения релевантных связанных ссылок.
- При отсутствии раздела «См. также» скрипт ищет все доступные ссылки на странице.
- Реализован безопасный выход из программы и обработка ошибок.

## Используемые технологии
- **Python 3.x**
- **Selenium**: управление браузером и автоматизация взаимодействия с веб-страницами.
- **Google Chrome**: браузер по умолчанию для выполнения парсинга.
- **WebDriver для Chrome**: обеспечивает интерфейс между `selenium` и браузером.


## Примечания
- Скрипты требуют установленного браузера Chrome и совместимого драйвера ChromeDriver.
- Рекомендуется запускать в виртуальном окружении Python.
- Возможны блокировки запросов при слишком частом обращении к Википедии.

## Вклад в проект
Если у вас есть предложения или улучшения, отправляйте запросы на добавление (pull requests) или создавайте задачи (issues).

## Лицензия
Проект распространяется под лицензией MIT. Подробности см. в файле `LICENSE`.



 
