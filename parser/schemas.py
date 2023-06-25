from pydantic import BaseModel
from enum import Enum


class DealTypeEnum(str, Enum):
    sale = 'sale'
    rent = 'rent'


class TransportationTypeEnum(str, Enum):
    pedestrian = 'pd'
    public_transport = 'mt'
    car = 'auto'
    bicycle = 'bc'
    scooter = 'sc'
    taxi = 'taxi'


class GeoLocation(BaseModel):
    lat: float
    lon: float
