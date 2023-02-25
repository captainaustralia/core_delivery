from djchoices.choices import DjangoChoices


class GenderType(DjangoChoices):
    UNDEFINED = (0, "UNDEFINED")
    MALE = (1, "MALE")
    FEMALE = (2, "FEMALE")


class TransportType(DjangoChoices):
    AUTO = (0, "AUTO")
    MOTO = (1, "MOTO")
    OTHER = (2, "OTHER")
