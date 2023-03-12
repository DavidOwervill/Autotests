from pydantic import BaseModel, validator
from API_test_v2.src.enums.sample_api_characters_enum import SampleApiEnums


class SampleApiCharacterSchema(BaseModel):
    id: int
    name: str
    status: SampleApiEnums
    species: str
    type: str
    gender: str
    origin: str
    image: str

    @validator("id")
    def get_validate_id(cls, id):
        if id > 0:
            return id
        else:
            raise ValueError("Id меньше нуля")
