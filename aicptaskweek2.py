class OutingOrganizer:
    def __init__(self):
        self.min_seniors = 10
        self.max_seniors = 36
        self.min_carers = 2
        self.additional_carers_threshold = 24

        self.cost_table = {
            '12-16': {'coach': 150, 'meal': 14.00, 'ticket': 21.00},
            '17-26': {'coach': 190, 'meal': 13.50, 'ticket': 20.00},
            '27-39': {'coach': 225, 'meal': 13.00, 'ticket': 19.00}
        }

        self.num_seniors = 0
        self.num_carers = 0
        self.total_cost = 0
        self.cost_per_person = 0
        self.total_collected = 0
        self.people_on_outing = []

    def calculate_cost(self):
        if self.num_seniors < self.min_seniors or self.num_seniors > self.max_seniors:
            print("Error: Number of seniors should be between 10 and 36.")
            return

        if self.num_seniors > self.additional_carers_threshold:
            self.num_carers = self.min_carers + 1

        for range_, costs in self.cost_table.items():
            range_start, range_end = map(int, range_.split('-'))
            if range_start <= self.num_seniors <= range_end:
                self.total_cost = costs['coach'] + costs['meal'] * self.num_seniors + costs['ticket'] * self.num_seniors
                self.cost_per_person = self.total_cost / self.num_seniors
                break

    def record_people_on_outing(self):
        print("Enter the names and amounts paid by the people on the outing:")
        for _ in range(self.num_seniors + self.num_carers):
            name = input("Enter name: ")
            amount_paid = float(input("Enter amount paid: $"))
            self.people_on_outing.append((name, amount_paid))
            self.total_collected += amount_paid

    def print_people_on_outing(self):
        print("\nPeople on the outing:")
        for name, amount_paid in self.people_on_outing:
            print(f"{name}: ${amount_paid}")

    def calculate_profit_or_break_even(self):
        profit_or_loss = self.total_collected - self.total_cost
        if profit_or_loss >= 0:
            print(f"\nThe outing has made a profit of ${profit_or_loss:.2f}.")
        else:
            print(f"\nThe outing has broken even.")


def main():
    organizer = OutingOrganizer()

    # Task 1: Calculate cost
    organizer.num_seniors = int(input("Enter the number of senior citizens interested in the outing: "))
    organizer.calculate_cost()
    print(f"\nTotal cost of the outing: ${organizer.total_cost:.2f}")
    print(f"Cost per person: ${organizer.cost_per_person:.2f}")

    # Task 2: Record people on outing
    organizer.record_people_on_outing()
    organizer.print_people_on_outing()

    # Task 3: Calculate profit or break-even
    organizer.calculate_profit_or_break_even()


if __name__ == "__main__":
    main()
