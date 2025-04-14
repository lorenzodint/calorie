from pydantic import BaseModel, Field, field_validator
from typing import List, Optional


class Cibo(BaseModel):
    cibo: Optional[str] = Field(None, description="Cibo che è stato fornito")
    calorie: Optional[str] = Field(
        None, description="Il valore in calorie del cibo che è stato fornito")
    consigli: Optional[str] = Field(
        None, description="Consigli sull'assunzione del cibo che è stato fornito")
    info: Optional[str] = Field(
        None, description="Informazioni aggiuntive sul cibo fornito")
    rischi: Optional[str] = Field(
        None, description="Rischi sull'eccessiva assunzione del cibo fornito o altro")

    model_config = {
        "json_schema_extra": {
            "additionalProperties": False  # Blocca campi non definiti
        }
    }
