"""
Seminar 09
Product class
"""


class Product:
    """Represent information for a Product instance."""

    def __init__(self, name="", price=0.0):
        """Construct Product instance."""
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string for a Product instance."""
        return f"{self.name} ${self.price:.2f}"
