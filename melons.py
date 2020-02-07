"""Classes for melon orders."""


class AbstractMelonOrder():
    def __init__(self, species, qty, country_code, order_type, tax):

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melons":
            base_price = 7.5

        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price

        if self.country_code != 'USA' and self.qty < 10:
            return total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, 'USA', 'domestic', 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, country_code, 'international', 0.17)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super().__init__(species, qty, 'USA', 'government', 0)

    def mark_inspection(self, passed):
        """"""
        if passed:
            self.passed_inspection = True
        else:
            self.passed_inspection = False
