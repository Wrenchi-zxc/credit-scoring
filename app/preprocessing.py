import numpy as np

def preprocessing(request: dict) -> dict:

    request["RevolvingUtilizationOfUnsecuredLines"] = min(2, request["RevolvingUtilizationOfUnsecuredLines"])
    request["DebtRatio"] = np.log1p(request["DebtRatio"])

    if request["MonthlyIncome"] is None:
        request["MonthlyIncome"] = np.nan
    if request["NumberOfDependents"] is None:
            request["NumberOfDependents"] = np.nan

    return request