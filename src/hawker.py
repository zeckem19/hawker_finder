from datetime import datetime
from typing import List

from pydantic import (
    BaseModel,
    AnyHttpUrl,
    constr,
    confloat,
)

class CreationMixin(BaseModel):
    creation_timestamp: datetime

class GeoJSON(BaseModel):
    type: str
    coordinates: List[confloat(ge=-180,le=180)]

class HawkerCentre(CreationMixin):
    name: constr(min_length=2, max_length= 100, strip_whitespace=True)
    photourl: AnyHttpUrl
    location: GeoJSON