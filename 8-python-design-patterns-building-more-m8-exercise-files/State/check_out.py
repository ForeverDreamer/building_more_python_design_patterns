from abs_state import AbsState


class AtCheckOut(AbsState):

    def add_item(self):
        print("You can't add items at the check out counter.")

    def remove_item(self):
        print("You can't remove items at the check out counter.")

    def checkout(self):
        print("You're already at checkout.")

    def pay(self):
        print("You paid for %s items." % self._cart.size)
        self._cart.state = self._cart.paid_for

    def empty_cart(self):
        print("You can't empty items at the check out counter.")
