from typing import Annotated, Literal
from pydantic import BaseModel, ConfigDict, Field

NonNegativeInt = Annotated[int, Field(ge=0)]
NonNegativeFloat = Annotated[float, Field(ge=0)]
Age = Annotated[int, Field(ge=18, lt=120)]

class Health(BaseModel):
    status: Literal["ok"]



class ScoringRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    RevolvingUtilizationOfUnsecuredLines: NonNegativeFloat
    age: Age
    NumberOfTime30_59DaysPastDueNotWorse: NonNegativeInt = Field(
        alias="NumberOfTime30-59DaysPastDueNotWorse"
    )
    DebtRatio: NonNegativeFloat
    MonthlyIncome: NonNegativeFloat | None = None
    NumberOfOpenCreditLinesAndLoans: NonNegativeInt
    NumberOfTimes90DaysLate: NonNegativeInt
    NumberRealEstateLoansOrLines: NonNegativeInt
    NumberOfTime60_89DaysPastDueNotWorse: NonNegativeInt = Field(
        alias="NumberOfTime60-89DaysPastDueNotWorse"
    )
    NumberOfDependents: NonNegativeFloat | None = None

class ScoringResponse(BaseModel):
    default_probability: float
    is_approved: bool