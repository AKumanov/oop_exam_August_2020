class Appliance:
    def __init__(self, cost: float):
        self.cost = cost  # cost per day // 30 days in a month

    def get_monthly_expense(self):
        return self.cost * 30
