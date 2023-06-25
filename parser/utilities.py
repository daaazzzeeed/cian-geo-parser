from schemas import GeoLocation, TransportationTypeEnum
from config import Settings


def build_route_url(point_from: GeoLocation,
                    point_to: GeoLocation,
                    transportation_type: TransportationTypeEnum,
                    ) -> str:
    return Settings.YANDEX_MAPS_GET_ROUTE_URL.format(lat1=point_from.lat,
                                                     lon1=point_from.lon,
                                                     lat2=point_to.lat,
                                                     lon2=point_to.lon,
                                                     transport_type=transportation_type,
                                                     )
