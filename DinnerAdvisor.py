class DinnerAdvisor:
    @staticmethod
    def getAdvice(moneyBeforeSalary: float, daysBeforeSalary: int):
        if moneyBeforeSalary < 3000:
            print("Сегодня лучше поесть дома. Экономьте, и вы дотянете до зарплаты!")
        elif moneyBeforeSalary < 10000:
            if daysBeforeSalary < 10:
                print("Можете шиковать! Пора в Макдак!")
            else:
                print("Сегодня лучше поесть дома. Экономьте, и вы дотянете до зарплаты!")
        elif moneyBeforeSalary < 30000:
            if daysBeforeSalary < 10:
                print("Замечательно! Можно прикупить долларов и зайти поужинать в классное место. Так держать! :)")
            else:
                print("Можете шиковать! Пора в Макдак!")
        else:
            if daysBeforeSalary < 10:
                print("Отлично! Можно заказывать крабов!")
            else:
                print("Замечательно! Можно прикупить долларов и зайти поужинать в классное место. Так держать! :)")
