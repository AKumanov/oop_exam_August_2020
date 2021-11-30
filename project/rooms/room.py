class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = list()
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        """ each element of args is a list of either child or appliance """
        expenses = 0
        for list_el in args:
            for obj in list_el:
                expenses += obj.get_monthly_expense()
        self.expenses = expenses
