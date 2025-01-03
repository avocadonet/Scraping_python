# Сайт для поиска радиодеталей и компонентов  

Этот проект предназначен для удобного поиска радиодеталей и компонентов на сайтах [ChipDip](https://www.chipdip.ru) и [Elecomp](https://elecomp.ru). Он позволяет быстро находить информацию о товарах, включая их название, цену, количество на складе и ссылки на страницы товаров.

## Основные особенности  

- **Парсинг сайтов**: удобное извлечение данных о товарах с популярных ресурсов.  
- **Информация о товарах**: получение названия, цены, количества и ссылки на товар.  
- **Простота использования**: легкий доступ к информации через интуитивно понятный интерфейс.  

Проект идеально подходит для радиолюбителей и специалистов в области электроники, которые ищут нужные компоненты для своих проектов!

## Установка

### Для Linux

1. Склонируйте репозиторий:
```bash
   git clone git clone https://github.com/avocadonet/Scraping_python.git
   ```
2. Убедитесь, что Docker установлен и запущен. Если Docker не установлен, следуйте [официальному руководству по установке Docker](https://docs.docker.com/engine/install/).

3. Запустите проект с помощью скрипта `build.sh`, который содержит команды для работы с Docker:
```bash
   bash build.sh
   ```
4. После запуска, откройте браузер и перейдите по адресу: [http://localhost:5000/](http://localhost:5000/)

5. Ждите завершения запуска и сбора данных с сайтов.

### Для Windows

1. Склонируйте репозиторий:
```bash
   git clone git clone https://github.com/avocadonet/Scraping_python.git
   ```
2. Убедитесь, что Docker Desktop установлен и запущен. Если Docker не установлен, следуйте [официальному руководству по установке Docker Desktop](https://docs.docker.com/desktop/windows/install/).

3. Рыбота с Git Bash (если не установлено, установите [Git для Windows](https://git-scm.com/download/win)). Запустите команду:
```bash
   bash build.sh
   ```
4. После запуска, откройте браузер и перейдите по адресу: [http://localhost:5000/](http://localhost:5000/)

5. Ждите завершения запуска и сбора данных с сайтов.