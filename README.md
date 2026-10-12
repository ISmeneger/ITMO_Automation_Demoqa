# ITMO — DemoQA Python UI Automation

Первый учебный проект по автоматизации UI-тестирования на **Python**, выполненный во время обучения тестированию ПО в **Университете ИТМО**. Содержит практические задания с занятий и самостоятельные домашние работы.

Объекты тестирования: [DemoQA](https://demoqa.com/) и раздел Add/Remove Elements учебного сайта [The Internet](https://the-internet.herokuapp.com/).

## Стек и структура

**Python · Pytest · Selenium WebDriver · Chrome · Page Object Model**

- `pages/` — модели страниц и локаторы;
- `components/` — общие действия с элементами и явные ожидания;
- `tests/` — UI-сценарии, включая домашние задания в `tests_hw/`;
- `checks/` — проверки вспомогательной логики без браузера;
- `examples/` — учебные примеры markers, skip и проверки формата даты;
- `conftest.py` — отдельный браузер для каждого UI-теста;
- `pytest.ini` — настройки сбора и markers;
- `requirements.txt` — прямые зависимости проекта.

Сохранены версии учебного стека: **Selenium 4.16.0, Pytest 7.4.4**. Сбор тестов и проверки helpers выполнены на Python 3.12. Примеры в `examples/` не входят в обычный UI-прогон.

## Сценарии

- навигация, заголовки страниц, viewport и элементы меню;
- ввод и очистка текста, атрибуты и CSS;
- заполнение Practice Form и проверки валидации;
- выбор значения в State;
- alert, confirm, prompt и отложенный alert;
- модальные окна, новые вкладки, accordion;
- slider и progress bar;
- добавление, редактирование, удаление и пагинация записей Web Tables;
- поиск по значениям шести столбцов;
- добавление и удаление элементов на The Internet.

Practice Form — учебная форма ввода данных, а не настоящая авторизация. Названия некоторых исходных файлов (`test_login_form.py`) сохранены для преемственности с курсом.

## Что изменено после обучения

- Исправлены отсутствующий импорт `Keys` и пробел в URL формы.
- Убрана вспомогательная HTTP-проверка, скрывавшая ошибки UI через `skip`.
- Заменены фиксированные паузы на ожидания элементов, alerts и результатов.
- Циклы ограничены; progress bar проверяется по достижению порога, slider имеет конечное число действий.
- Каждый тест получает отдельный браузер; страницы и вкладки не переносят состояние между тестами.
- Очистка `input` проверяется через `value`, прокрутка выполняется к указанному элементу.
- Исправлены CSS-имена, навигационная проверка и проверка удаления записи.
- Поиск проверяет реальные данные таблицы; исторический сценарий сортировки перенесён в `examples/`, поскольку текущий сайт больше не реализует сортировку.
- Примеры с `assert True` и учебные skip вынесены в `examples/`.
- Убраны ненужные зависимости анализа данных и бинарный `chromedriver.exe`; драйвер подбирается Selenium Manager.

## Запуск в Windows / PowerShell

Установите Python и Google Chrome. При первом запуске Selenium Manager может потребоваться доступ в интернет для получения совместимого драйвера.

```powershell
git clone https://github.com/ISmeneger/ITMO_Automation_Demoqa.git
cd ITMO_Automation_Demoqa
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Проверить сбор UI-тестов без запуска браузера:

```powershell
.\.venv\Scripts\python.exe -m pytest --collect-only -q
```

Весь UI-набор:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Один сценарий:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_clear.py -v
```

Проверки helpers без браузера:

```powershell
.\.venv\Scripts\python.exe -m pytest checks -v
```

Выбор по markers:

```powershell
.\.venv\Scripts\python.exe -m pytest -m smoke -v
.\.venv\Scripts\python.exe -m pytest -m regress -v
```

Markers назначены отдельным примерам реальных проверок; они не обозначают весь набор проекта.

Headless Chrome:

```powershell
$env:HEADLESS="1"
.\.venv\Scripts\python.exe -m pytest -v
Remove-Item Env:HEADLESS
```

На Linux/macOS используйте `.venv/bin/python` вместо `.\.venv\Scripts\python.exe`.

## Результаты проверки

Полный локальный запуск **13 октября 2026 года** на Windows, Python 3.12 и Chrome 154.0.8037.99:

```powershell
.\.venv\Scripts\python.exe -m pytest tests checks -v --tb=short -rx
```

| Набор | Всего | Passed | Xfailed |
|---|---:|---:|---:|
| UI-сценарии | 52 | 50 | 2 |
| Проверки helpers | 10 | 10 | 0 |
| **Итого** | **62** | **60** | **2** |

**0 failed, 0 errors**. Время прогона — **480,64 секунды** (около 8 минут). Это результат указанного локального запуска, а не гарантия будущих прогонов внешнего сайта.

Два сценария воспроизводят известные дефекты DemoQA:

- кнопка **Close** не закрывает окно после отправки Practice Form;
- последовательное удаление исходных записей **Web Tables** восстанавливает ранее удалённую запись.

Они отмечены **strict xfail**. При исправлении поведения сценарий получит **XPASS**, и прогон завершится ошибкой, чтобы напомнить обновить отметку. Проверка удаления допускает xfail только для специальной ошибки восстановления записи. Ошибки Selenium, таймауты и другие неожиданные ошибки остаются падениями. Подробности — в [KNOWN_ISSUES.md](KNOWN_ISSUES.md).

## Ограничения и диагностика

DemoQA — внешний учебный сайт: изменения DOM, текста, оформления и рекламные перекрытия могут влиять на сценарии. Локаторы адаптированы по актуальному сайту и проверены локальным прогоном.

Если footer перехватывает обычный клик по button/a, применяется активация через Enter. Это проверяет функциональный результат через клавиатуру; проблема доступности кнопки мышью описана отдельно.

Сортировка больше не реализована в текущей Web Tables. Исторический сценарий сохранён в `examples/webtables_sort_legacy.py`; активный набор проверяет поиск по данным таблицы.

При обычных UI-падениях в `artifacts/` сохраняются screenshot, HTML и URL. Эти файлы исключены из Git через `.gitignore`.

Более развитые проекты портфолио:

- [American Eagle — Java UI & API](https://github.com/ISmeneger/American_Eagle_java_automation)
- [American Eagle — Python UI & API](https://github.com/ISmeneger/American_Eagle_python_automation)

## Автор

[Илья Сидорычев / ISmeneger](https://github.com/ISmeneger)

Учебная работа ИТМО с последующим рефакторингом для портфолио.
