import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:

    selected_student = students[students['student_id'] == 101][['name', 'age']]
    
    return selected_student