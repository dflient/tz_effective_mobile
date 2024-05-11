import csv
from typing import List, Dict

class RecordManager:
    def __init__(self):
        self.records: List[Dict[str, str]] = self.load_records()

    def show_balance(self) -> None:
        """Выводит текущий баланс, поступления и расходы"""
        total_income = sum(float(record['amount']) for record in self.records if record['category'] == 'доход')
        total_expense = sum(float(record['amount']) for record in self.records if record['category'] == 'расход')
        print(f"Текущий баланс: {total_income - total_expense}")
        print(f"Общий доход: {total_income}")
        print(f"Общий расход: {total_expense}")

    def add_record(self) -> None:
        """Добавляет новую запись поступлений/расходов"""
        date: str = input("Введите дату (ГГГГ-ММ-ДД): ")
        category: str = input("Введите категорию (доход/расход): ")
        amount: float = float(input("Введите сумму: "))
        description: str = input("Введите описание: ")
        self.records.append({'date': date, 'category': category, 'amount': amount, 'description': description})
        self.save_records()

    def edit_record(self) -> None:
        """Вносит корректировки в существующую запись"""
        index: int = int(input("Введите индекс записи для редактирования: "))
        if index < 0 or index >= len(self.records):
            print("Недопустимый индекс")
            return
        record = self.records[index]
        print("Текущая запись:")
        print(record)
        record['date'] = input("Введите новую дату (ГГГГ-ММ-ДД): ")
        record['category'] = input("Введите новую категорию (доход/расход): ")
        record['amount'] = float(input("Введите новую сумму: "))
        record['description'] = input("Введите новое описание: ")
        self.save_records()

    def search_records(self) -> None:
        """Выполняет поиск записи по категории/дате/сумме"""
        search_criteria = input("Введите критерий поиска (категория/сумма/дата): ")
        if search_criteria == 'категория':
            category = input("Введите категорию для поиска (доход/расход): ")
            results = [record for record in self.records if record['category'] == category]
        elif search_criteria == 'сумма':
            amount = float(input("Введите сумму для поиска: "))
            results = [record for record in self.records if float(record['amount']) == amount]
        elif search_criteria == 'дата':
            date = input("Введите дату для поиска (ГГГГ-ММ-ДД): ")
            results = [record for record in self.records if record['date'] == date]
        else:
            print("Неверный критерий поиска. Пожалуйста, попробуйте снова.")
            return
        print("Результаты поиска:")
        for result in results:
            print(result)

    def save_records(self) -> None:
        """Сохраняет данные в CSV файл"""
        with open('records.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(self.records)

    def load_records(self) -> List[Dict[str, str]]:
        """Загружает данные из CSV файла"""
        try:
            with open('records.csv', 'r') as file:
                reader = csv.DictReader(file)
                records = [record for record in reader]
        except FileNotFoundError:
            records = []
        return records

    def run(self) -> None:
        """Основной метод, выполняющий логику работы программы"""
        while True:
            print("\n1. Показать баланс\n2. Добавить запись\n3. Редактировать запись\n4. Поиск записей\n5. Выход")
            choice = input("Введите ваш выбор: ")
            if choice == '1':
                self.show_balance()
            elif choice == '2':
                self.add_record()
            elif choice == '3':
                self.edit_record()
            elif choice == '4':
                self.search_records()
            elif choice == '5':
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")
        print("Завершение работы...")
        self.save_records()

if __name__ == "__main__":
    record_manager = RecordManager()
    record_manager.run()
