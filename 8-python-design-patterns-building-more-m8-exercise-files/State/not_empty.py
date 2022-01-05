from abs_state import AbsState


class NotEmpty(AbsState):

    def add_item(self):
        self._cart.size += 1
        print('You now have %s items in your cart.' % self._cart.size)

    def remove_item(self):
        self._cart.size -= 1
        if self._cart.size > 0:
            print('You now have %s items in your cart.' % self._cart.size)
        else:
            print('Your cart is empty again.')
            self._cart.state = self._cart.empty

    def checkout(self):
        print("Done shopping. Let's check out!")
        self._cart.state = self._cart.check_out

    def pay(self):
        print("You have to go to checkout to pay!")

    def empty_cart(self):
        self._cart.size = 0
        self._cart.state = self._cart.empty
        print("Your cart is empty again.")
