import pandas as pd 
student =pd.read_csv ('../data/raw/student.csv')
 # print(student.columns)
# print(student.info())
# print(student.isnull().sum())
# print(student.isnull())
# print(student.dtypes)
# print(student.describe)
# is_all_unique=student['Student ID'].is_unique
# print(is_all_unique)
# duplicate=student[student['Student ID'].duplicated()]
# print(duplicate)
# print(student['Student ID'].duplicated().sum())
# duplicate_id=student['Student ID'].value_counts()
# print(duplicate_id[duplicate_id>1])
# print(student.duplicated().sum())
# print(student[student['Student ID']=='EDO8757'])
# id_counts=student['Student ID'].value_counts()
# duplicate_ids=id_counts[id_counts>1]
# print(len(duplicate_ids))
# print(student['Balance Due'])
# print(student.dtypes)
# print(student['Fee Amount'])

# print(student['Fee Payment Status']  
# print(student['Deadline Date'])
# print(student['Country'].unique())
# print(student['Enrollment Status'].unique())
# print(student['Fee Currency'].unique())
# print(student['College'])
# print(student['Counsellor'])
# print(student['Fee Paid'])
