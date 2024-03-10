class Rental():
    def __init__(self):
        self.income = 0
        self.all_expenses = 0
        self.cashflow1 = 0
        self.invesments = 0
        self.roi = 0


    def income_input(self):
        self.income = float(input('Enter your rental income: '))
        print(f'Your rental income is {self.income}')
        return self.income

    def expenses(self):
        print('We need all your expenses per month: ')
        tax = float(input('Enter your property tax: '))
        insurance = float(input('Enter your insurance amount: '))
        utilities = float(input('Enter your utilities amount: '))
        hoa = float(input('Enter your HOA amount: '))
        repairs = float(input('Enter your repairs amount: '))
        vacancy = float(input('Enter your estimated vacancy amount: '))
        PM = float(input('Enter your property management amount: '))
        mortgage = float(input('Enter your monthly mortgage amount: '))

        self.all_expenses = tax + insurance + utilities + hoa + repairs + vacancy + PM + mortgage
        print(f'Your total expenses is: {self.all_expenses}')
        return self.all_expenses

    def cashflow(self):
        self.cashflow1 = self.income - self.all_expenses
        print(f'Cashflow: {self.cashflow1}')
        return self.cashflow1
    
    def total_invesments(self):
        print('We need all your invesments amount: ')
        down = float(input('Enter your down payment: '))
        closing_cost = float(input('Enter your closing cost: '))
        rehab = float(input('Enter your rehab budget: '))
        misc = float(input('Enter your misc other: '))

        self.invesments = down + closing_cost + rehab +misc
        print(f'Your total invesments is {self.invesments}')
        return self.invesments
    
    def print_roi(self):
        self.roi = self.cashflow1 * 12 / self.invesments * 100
        print(f'Your ROI is {self.roi}%')



def main():
    rental1 = Rental()
    rental1.income_input()
    rental1.expenses()
    rental1.cashflow()
    rental1.total_invesments()
    rental1.print_roi()

main()
    



            







