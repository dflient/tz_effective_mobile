# RecordManager 
 
RecordManager - это приложение, который позволяет управлять записями о доходах и расходах. С помощью этого класса вы можете добавлять новые записи, редактировать существующие, искать записи по различным критериям, а также просматривать текущий баланс. 
 
## Установка 
 
1. Склонируйте репозиторий на свой компьютер 
2. Убедитесь, что у вас установлен Python версии 3.x 
 
## Использование 
 
1. Запустите программу, выполнив  python main.py  
2. Следуйте инструкциям в консоли для выполнения различных действий: 
   - Введите  1  для просмотра текущего баланса 
   - Введите  2  для добавления новой записи 
   - Введите  3  для редактирования существующей записи 
   - Введите  4  для поиска записей 
   - Введите  5  для выхода из программы 
 
## Функции 
 
-  show_balance() : Отображает текущий баланс, общий доход и общий расход. 
-  add_record() : Добавляет новую запись о доходе или расходе. 
-  edit_record() : Редактирует существующую запись. 
-  search_records() : Выполняет поиск записей по категории, сумме или дате. 
-  save_records() : Сохраняет данные в CSV файл. 
-  load_records() : Загружает данные из CSV файла. 
-  run() : Основной метод, выполняющий логику работы программы. 