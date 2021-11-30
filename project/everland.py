class Everland:
    def __init__(self):
        self.rooms = list()

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        consumptions = 0
        for room in self.rooms:
            consumptions += (room.expenses + room.room_cost)
        return f"Monthly consumptions: {consumptions:.2f}$."

    def pay(self):
        output = []
        for room in self.rooms:
            total_cost = room.expenses + room.room_cost
            if room.budget >= total_cost:
                room.budget -= total_cost
                output.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                return f"{room.family_name} does not have enough budget and must leave the hotel."
        return '\n'.join(output)

    def status(self):
        output = list()
        output.append(f"Total population: {sum([r.members_count for r in self.rooms])}")

        for room in self.rooms:
            output.append(
                f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if hasattr(room, "children"):
                counter = 0
                for child in room.children:
                    counter += 1
                    output.append(f"--- Child {counter} monthly cost: {child.get_monthly_expense():.2f}$")

            output.append(f"--- Appliances monthly cost: {sum([a.get_monthly_expense() for a in room.appliances]):.2f}$")

        return '\n'.join(output)
