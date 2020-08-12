class CoffeeMachine:
    coffee_machine_state = "off"
    water = 0
    milk = 0
    coffee_beans = 0
    disposable_cups = 0
    money = 0

    # espresso
    water_for_one_espresso = 250
    coffee_beans_for_one_espresso = 16
    cost_for_one_espresso = 4

    # latte
    water_for_one_latte = 350
    milk_for_one_latte = 75
    coffee_beans_for_one_latte = 20
    cost_for_one_latte = 7

    # cappuccino
    water_for_one_cappuccino = 200
    milk_for_one_cappuccino = 100
    coffee_beans_for_one_cappuccino = 12
    cost_for_one_cappuccino = 6

    def __init__(self, coffee_machine_state="on", water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550):
        self.coffee_machine_state = coffee_machine_state
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def __str__(self):  # Only for debugging purposes
        return "CoffeeMachine {} {} {} {} {} {}".format(self.coffee_machine_state, self.water, self.milk,
                                                        self.coffee_beans, self.disposable_cups, self.money)

    @staticmethod
    def machine_action():  # read input from the user
        user_input = input()
        return user_input

    def fill_coffee_machine(self):

        print("Write how many ml of water do you want to add: ")
        water_to_add = int(CoffeeMachine.machine_action())
        self.water += water_to_add
        print("Write how many ml of milk do you want to add: ")
        milk_to_add = int(CoffeeMachine.machine_action())
        self.milk += milk_to_add
        print("Write how many grams of coffee beans do you want to add: ")
        coffee_beans_to_add = int(CoffeeMachine.machine_action())
        self.coffee_beans += coffee_beans_to_add
        print("Write how many disposable cups of coffee do you want to add:")
        disposable_cups_to_add = int(CoffeeMachine.machine_action())
        self.disposable_cups += disposable_cups_to_add
        print()

    def print_current_machine_supplies_level(self):
        print("The coffee machine has: ")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(self.money, "of money")
        print()

    def take_money(self):
        print("I gave you $%d" % self.money)
        self.money -= self.money
        print()

    def perform_buy(self):

        while True:
            print("What you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu")
            coffee_type = CoffeeMachine.machine_action()  # read input from the user

            if coffee_type == "1":
                if self.water >= CoffeeMachine.water_for_one_espresso:
                    self.water -= CoffeeMachine.water_for_one_espresso
                else:
                    print("Sorry, not enough water")
                    break
                if self.coffee_beans >= CoffeeMachine.coffee_beans_for_one_espresso:
                    self.coffee_beans -= CoffeeMachine.coffee_beans_for_one_espresso
                else:
                    print("Sorry, not enough coffee beans")
                    break

                self.money += CoffeeMachine.cost_for_one_espresso
                self.disposable_cups -= 1
                print("I have enough resources, making you a coffee!")
                print()
                break

            elif coffee_type == "2":
                if self.water >= CoffeeMachine.water_for_one_latte:
                    self.water -= CoffeeMachine.water_for_one_latte
                else:
                    print("Sorry, not enough water")
                    break
                if self.milk >= CoffeeMachine.milk_for_one_latte:
                    self.milk -= CoffeeMachine.milk_for_one_latte
                else:
                    print("Sorry, not enough milk")
                    break
                if self.coffee_beans >= CoffeeMachine.coffee_beans_for_one_latte:
                    self.coffee_beans -= CoffeeMachine.coffee_beans_for_one_latte
                else:
                    print("Sorry, not enough coffee beans")
                    break
                self.money += CoffeeMachine.cost_for_one_latte
                self.disposable_cups -= 1
                print("I have enough resources, making you a coffee!")
                break
            elif coffee_type == "3":
                if self.water >= CoffeeMachine.water_for_one_cappuccino:
                    self.water -= CoffeeMachine.water_for_one_cappuccino
                else:
                    print("Sorry, not enough water")
                    break
                if self.milk >= CoffeeMachine.milk_for_one_cappuccino:
                    self.milk -= CoffeeMachine.milk_for_one_cappuccino
                else:
                    print("Sorry, not enough milk")
                    break
                if self.coffee_beans >= CoffeeMachine.coffee_beans_for_one_cappuccino:
                    self.coffee_beans -= CoffeeMachine.coffee_beans_for_one_cappuccino
                else:
                    print("Sorry, not enough coffee beans")
                    break
                self.money += CoffeeMachine.cost_for_one_cappuccino
                self.disposable_cups -= 1
                print("I have enough resources, making you a coffee!")
                break
            elif coffee_type == "back":
                break


a = CoffeeMachine()

while True:
    if a.coffee_machine_state == "on":
        print("Write action (buy, fill, take, remaining, exit): ")
        user_choice = a.machine_action()
        if user_choice == "remaining":
            a.print_current_machine_supplies_level()
        elif user_choice == "buy":
            a.coffee_machine_state = "buy"
            a.perform_buy()
            a.coffee_machine_state = "on"
        elif user_choice == "take":
            a.take_money()
        elif user_choice == "fill":
            a.fill_coffee_machine()
        elif user_choice == "exit":
            a.coffee_machine_state = "off"
            break
