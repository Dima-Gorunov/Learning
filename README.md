## Когда вы изменили код и хотите отправить изменения на удаленный репозиторий:

- git add . (или git add \<file>): Добавить измененные файлы в индекс.

- git commit -m "Ваше сообщение": Создать коммит с описанием ваших изменений.

- git push origin \<branch-name\>: Отправить ваши коммиты на удаленный репозиторий.

## Когда вы хотите скачать (получить) код с удаленного репозитория:

- git pull origin \<branch-name>: Получить и объединить изменения с удаленного репозитория в вашей текущей ветке.

Это самые основные действия для работы с Git в простых сценариях. Не забудьте заменить \<branch-name> на имя ветки, с которой вы работаете (обычно это "main" или "master").

## Структура названий коммитов: типы и примеры

Когда дело касается названия коммитов, хорошая практика - это следовать определенным соглашениям, таким как Conventional Commits, чтобы обеспечить структуру и понимание ваших коммитов. Вот несколько примеров названий коммитов в соответствии с этим подходом:

- feat: Добавлена новая функция или возможность.
Пример: feat: Добавлена поддержка множественных файлов

- fix: Исправлена ошибка или проблема.
Пример: fix: Исправлена ошибка неверной сортировки

- refactor: Произведен рефакторинг кода без изменения функциональности.
Пример: refactor: Улучшена структура хранения данных

- chore: Изменения, не влияющие на код (обновление зависимостей, настройки и т.д.).
Пример: chore: Обновлена версия библиотеки requests

- docs: Изменения в документации.
Пример: docs: Добавлено описание методов API

- style: Изменения в форматировании кода (пробелы, отступы и т.д.).
Пример: style: Улучшено выравнивание в коде

- test: Добавление, исправление или обновление тестов.
Пример: test: Добавлены тесты для проверки авторизации

- perf: Изменения, направленные на улучшение производительности.
Пример: perf: Оптимизирован алгоритм сортировки

- ci: Изменения в настройках непрерывной интеграции или автоматизации.
Пример: ci: Обновлены настройки деплоя на сервер

Применение соглашения Conventional Commits помогает создать четкую историю изменений, улучшает понимание коммитов и упрощает автоматизацию, например, при создании версий приложения.