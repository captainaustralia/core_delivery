from rest_framework.exceptions import APIException


class AlreadyDeliveryException(APIException):
    status_code = 400
    default_detail = "Already deliveryman!"
