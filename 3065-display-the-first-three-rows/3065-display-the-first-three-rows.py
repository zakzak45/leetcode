import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
     df = pd.DataFrame(employees)

# Get the first three rows
     first_three_rows = df.head(3)

     return first_three_rows