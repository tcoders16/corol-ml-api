from pydantic import BaseModel

class StrengthInput(BaseModel):
    Cement: float
    Slag: float
    FlyAsh: float
    Water: float
    Superplasticizer: float
    CoarseAggregate: float
    FineAggregate: float
    Age: float