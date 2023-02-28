import factory

from core_delivery.users.models import DefaultUser


class DefaultUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Sequence(lambda n: "FirstName%d" % n)
    last_name = factory.Sequence(lambda n: "LastName%d" % n)
    phone = factory.Sequence(lambda n: "+7909457%03d" % n)
    password = "strongpassword"

    class Meta:
        model = DefaultUser
