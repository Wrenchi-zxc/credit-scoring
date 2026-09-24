from pydantic import BaseModel, Field, ConfigDict

class ScoringRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    RevolvingUtilizationOfUnsecuredLines: float
    age: int = Field(ge=18, lt=120)
    NumberOfTime30_59DaysPastDueNotWorse: int = Field(alias="NumberOfTime30-59DaysPastDueNotWorse")
    DebtRatio: float
    MonthlyIncome: float | None = None
    NumberOfOpenCreditLinesAndLoans: int
    NumberOfTimes90DaysLate: int
    NumberRealEstateLoansOrLines: int
    NumberOfTime60_89DaysPastDueNotWorse: int = Field(alias="NumberOfTime60-89DaysPastDueNotWorse")
    NumberOfDependents: float | None = None

class ScoringResponse(BaseModel):
    default_probability: float
    is_approved: bool