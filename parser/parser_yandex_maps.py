from schemas import GeoLocation, TransportationTypeEnum
from utilities import build_route_url


def get_commute_time_between(point_from: GeoLocation,
                             point_to: GeoLocation,
                             transportation_type: TransportationTypeEnum,
                             ) -> int:
    route_url = build_route_url(point_from, point_to, transportation_type)
    return 1
