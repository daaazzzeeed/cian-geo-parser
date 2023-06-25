from pydantic import BaseSettings

from parser.schemas import TransportationTypeEnum, DealTypeEnum


class Settings(BaseSettings):
    CIAN_BASE_URL: str = 'https://www.cian.ru/cat.php?engine_version=2&deal_type=sale'
    YANDEX_MAPS_GET_ROUTE_URL: str = 'https://yandex.ru/maps/213/moscow/?from=api-maps&mode=routes&' \
                                     'origin=jsapi_2_1_79&rtext={lat1}%2C{lon1}~{lat2}C{lon2}&rtt={transport_type}&' \
                                     'ruri=~&z=16.23'
    DEFAULT_TRANSPORTATION_TYPE: TransportationTypeEnum = TransportationTypeEnum.pedestrian
    DEFAULT_DEAL_TYPE: DealTypeEnum = DealTypeEnum.sale
