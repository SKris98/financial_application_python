from Converter import Converter
from DinnerAdvisor import DinnerAdvisor
from ExpensesManager import ExpensesManager


class Main:
    def __init__(self):
        self.moneyBeforeSalary = float(input("Сколько денег у вас осталось до зарплаты?\n"))
        self.daysBeforeSalary = float(input("Сколько дней до зарплаты?\n"))
        self.converter = Converter(78.5, 88.7, 0.75)
        self.dinnerAdvisor = DinnerAdvisor()
        self.expensesManager = ExpensesManager()

    @staticmethod
    def printMenu():
        print("Что вы хотите сделать?")
        print("1 - Конвертировать валюту")
        print("2 - Получить совет")
        print("3 - Ввести трату")
        print("4 - Показать траты за неделю")
        print("5 - Показать самую большую сумму расходов за неделю")
        print("0 - Выход")

    def main(self):
        while True:
            main.printMenu()
            command = int(input())
            if command == 1:
                print("Ваши сбережения:", self.moneyBeforeSalary, "RUB")
                currency = int(input("В какую валюту хотите конвертировать? "
                                     "Доступные варианты: 1 - USD, 2 - EUR, 3 - JPY.\n"))
                self.converter.convert(self.moneyBeforeSalary, currency)
            elif command == 2:
                self.dinnerAdvisor.getAdvice(self.moneyBeforeSalary, self.daysBeforeSalary)
            elif command == 3:
                day = int(input("За какой день вы хотите ввести трату: 1-ПН, 2-ВТ, 3-СР, 4-ЧТ, 5-ПТ, 6-СБ, 7-ВС?\n"))
                expense = float(input("Введите размер траты:\n"))
                self.moneyBeforeSalary = self.expensesManager.saveExpense(self.moneyBeforeSalary, expense, day)
            elif command == 4:
                self.expensesManager.printAllExpenses()
            elif command == 5:
                print("Самая большая сумма расходов на этой неделе составила", self.expensesManager.findMaxExpense(),
                      "руб.")
            elif command == 0:
                print("Выход")
                return
            else:
                print("Извините, но такой команды сейчас нет.")


main = Main()
main.main()
