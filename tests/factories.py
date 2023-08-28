# Import necessary modules
from datetime import date
import factory
from factory.fuzzy import FuzzyDate
from service.models import Account

# Define the AccountFactory

class AccountFactory(factory.Factory):
    """Creates fake Accounts"""

    class Meta:
        model = Account

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    email = factory.Faker("email")
    address = factory.Faker("address")
    phone_number = factory.Faker("phone_number")
    date_joined = FuzzyDate(date(2008, 1, 1))

# Now you can use the AccountFactory to create fake Account instances for testing
