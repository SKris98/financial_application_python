class ExpensesManager:
    def __init__(self):
        self.expenses = [0 for i in range(7)]

    def saveExpense(self, moneyBeforeSalary: float, expense: float, day: int) -> float:
        moneyBeforeSalary = moneyBeforeSalary - expense
        self.expenses[day - 1] += expense
        print("Значение сохранено! Ваш текущий баланс в рублях:", moneyBeforeSalary)

        if moneyBeforeSalary < 1000:
            print("На Вашем счету осталось совсем немного. Стоит начать экономить!")
        return moneyBeforeSalary

    def printAllExpenses(self):
        i = 0
        for i in range(len(self.expenses)):
            print("День", (i + 1), ". Потрачено", self.expenses[i], " рублей")

    def findMaxExpense(self) -> float:
        maxExpense = 0
        for i in range(len(self.expenses)):
            if self.expenses[i] > maxExpense:
                maxExpense = self.expenses[i]
        return maxExpense
