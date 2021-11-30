class Child:
    def __init__(self, food_cost, *toys_cost):
        self.food_cost = food_cost  # money required per day // 30 days in a month
        self.toys_cost = sum(toys_cost)
        self.cost = self.get_expense()

    def get_expense(self):
        return self.toys_cost + self.food_cost

    def get_monthly_expense(self):
        return self.cost * 30

