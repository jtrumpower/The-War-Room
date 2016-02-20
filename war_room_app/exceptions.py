from rest_framework.exceptions import APIException, ParseError

class ClashAPIUnavailable(APIException):
    status_code = 503
    default_detail = 'Could not connect to Clash API.'

class CouldntRetrieveClan(ParseError):
    status_code = 400
    default_detail = 'Clash Api Returned no results'