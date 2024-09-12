from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'