# import pandas as pd 
# import numpy as np
# student =pd.read_csv ('../data/raw/student.csv')
#  # print(student.columns)
# # print(student.info())
# # print(student.isnull().sum())
# # print(student.isnull())
# # print(student.dtypes)
# # print(student.describe)
# # is_all_unique=student['Student ID'].is_unique
# # print(is_all_unique)
# # duplicate=student[student['Student ID'].duplicated()]
# # print(duplicate)
# # print(student['Student ID'].duplicated().sum())
# # duplicate_id=student['Student ID'].value_counts()
# # print(duplicate_id[duplicate_id>1])
# # print(student.duplicated().sum())
# # print(student[student['Student ID']=='EDO8757'])
# # id_counts=student['Student ID'].value_counts()
# # duplicate_ids=id_counts[id_counts>1]
# # print(len(duplicate_ids))
# # print(student['Balance Due'])
# # print(student.dtypes)
# # print(student['Fee Amount'])

# # print(student['Fee Payment Status']  
# # print(student['Deadline Date'])
# # print(student['Country'].unique())
# # print(student['Enrollment Status'].unique())
# # print(student['Fee Currency'].unique())
# # print(student['College'])
# # print(student['Counsellor'])
# # print(student['Fee Paid'])
# # print(student['First Name'].isnull().sum())
# student['First Name']=student['First Name'].str.strip().str.title()
# # print(student['First Name'])
# student['Last Name']=student['Last Name'].str.strip().str.title()
# student['College']=student['College'].str.split().str.join(" ").str.title()
# # print (student['College'])
# # print(student['College'].isnull().sum())
# # print(student['Counsellor'])
# # student['Counsellor']=student['Counsellor'].str.split().str.join(" ").str.title()

# # print(student['Counsellor'])
# # print(student.head(10))
# # print (student['Phone'])
# # print(student[student['Phone']=='Not Found'])
# # print(student['Phone'].isnull().sum())
# # print((student[student['Phone']=='Not Found']))
# # print((student['Phone'] == 'Not Found').sum())
# # print((student[student['Phone'].str.startswith('+')]))
# # print((student['Phone'].str.startswith('+', na=False)).sum())
# # print(student[['Country','Phone']].head(50))
# # print(
# # phone_list=('250', '233', '265', '255', '27', '264', '260', '254', '267', '263', '234', '251')
# # new_dict={'Rawanda':'250','Ghana':'233','Malawi':'265',
# # 'Tanzania':'255','South Africa':'27','Namibia':'264',
# #     'Zambia':'260','Kenya':'254','Botswana':'267','Zimbabwe':'263','Nigeria':'234','Ethiopia':'251','Rwanda':'250'}
# # student['Phone']=student['Phone'].replace('Not Found',np.nan)
# # student['Country']=student['Country'].map(new_dict)
# # student['Country']=student['Country'].isnull()
# # student['Phone']=student['Phone'].apply(lambda x:student['Phone'].add_prefix('+') if x.startswith(phone_list)else x)
# # def clean_phone(phone):
# #     
# #     if pd.isna(phone):
# #         return np.nan

# #   
# #     if phone == "Not Found":
# #         return np.nan

# #    
# #     phone = phone.replace(" ", "")

# #    
# #     if phone.startswith("+"):
# #         return phone

# #     
# #     if phone.startswith(phone_list):
# #         return "+" + phone

# #     
# #     return phone

# # student["Phone"] = student["Phone"].apply(clean_phone)
# # print(student['Phone'])
# # student['Fee Currency']=student['Fee Currency'].str.strip().str.upper()

# # student['Fee Currency']='USD'
# # print(student['Fee Currency'])

# # bad_chars=['Rs.','USD','$','INR']
# student['Fee Amount']=(student['Fee Amount'].str.replace(r'\$|USD|Rs\.|INR|,','',regex=True).str.strip())
# student['Fee Amount']=student['Fee Amount'].astype(float)
# # def conditions (row):
# #     if row['Fee Amount']>9000:
# #        return row['Fee Amount']/80
# #     else :
# #         return row['Fee Amount']
# # student['Fee Amount']=student.apply(conditions,axis=1).  shorter and faster vrsion ahead


# student['Fee Paid'] = np.where(student['Fee Amount'] > 9000, student['Fee Paid'] / 80, student['Fee Paid'])

# student['Fee Amount'] = np.where(student['Fee Amount'] > 9000, student['Fee Amount'] / 80, student['Fee Amount'])

# # print(student['Fee Amount'].head(50))
# # #Fee Paid 

# # print(student['Fee Paid'])
# # print(student['Balance Due'])
# # # DATE TIME

# # student['Deadline Date']= pd.to_datetime(student['Deadline Date'],format='mixed',dayfirst=True)
# # print(student['Deadline Date'])
# print(student['Fee Paid'])

import pandas as pd
import numpy as np

student = pd.read_csv('../data/raw/student.csv')

# ==========================================================
# EXPLORATION
# ==========================================================

# print(student.columns)
# print(student.info())
# print(student.isnull().sum())
# print(student.isnull())
# print(student.dtypes)
# print(student.describe)
# is_all_unique = student['Student ID'].is_unique
# print(is_all_unique)
# duplicate = student[student['Student ID'].duplicated()]
# print(duplicate)
# print(student['Student ID'].duplicated().sum())
# duplicate_id = student['Student ID'].value_counts()
# print(duplicate_id[duplicate_id > 1])
# print(student.duplicated().sum())
# print(student[student['Student ID'] == 'EDO8757'])
# id_counts = student['Student ID'].value_counts()
# duplicate_ids = id_counts[id_counts > 1]
# print(len(duplicate_ids))
# print(student['Balance Due'])
# print(student.dtypes)
# print(student['Fee Amount'])
# print(student['Fee Payment Status'])
# print(student['Deadline Date'])
# print(student['Country'].unique())
# print(student['Enrollment Status'].unique())
# print(student['Fee Currency'].unique())
# print(student['College'])
# print(student['Counsellor'])
# print(student['Fee Paid'])
# print(student['First Name'].isnull().sum())

# ==========================================================
# FIRST NAME
# ==========================================================

student['First Name'] = student['First Name'].str.strip().str.title()

# print(student['First Name'])

# ==========================================================
# LAST NAME
# ==========================================================

student['Last Name'] = student['Last Name'].str.strip().str.title()

# ==========================================================
# COLLEGE
# ==========================================================


student['College'] = student['College'].str.split().str.join(" ").str.title()
student['College'] = student['College'].replace('Not Assigned',np.nan)
# print(student['College'])
# print(student['College'].isnull().sum())

# ==========================================================
# COUNSELLOR
# ==========================================================

# print(student['Counsellor'])

student['Counsellor'] = student['Counsellor'].str.split().str.join(" ").str.title()

# print(student['Counsellor'])
# print(student.head(10))

# ==========================================================
# PHONE
# ==========================================================

# print(student['Phone'])
# print(student[student['Phone'] == 'Not Found'])
# print(student['Phone'].isnull().sum())
# print(student[student['Phone'] == 'Not Found'])
# print((student['Phone'] == 'Not Found').sum())
# print(student[student['Phone'].str.startswith('+')])
# print((student['Phone'].str.startswith('+', na=False)).sum())
# print(student[['Country', 'Phone']].head(50))

phone_list = (
    '250', '233', '265', '255', '27', '264',
    '260', '254', '267', '263', '234', '251'
)

new_dict = {
    'Rawanda': '250',
    'Ghana': '233',
    'Malawi': '265',
    'Tanzania': '255',
    'South Africa': '27',
    'Namibia': '264',
    'Zambia': '260',
    'Kenya': '254',
    'Botswana': '267',
    'Zimbabwe': '263',
    'Nigeria': '234',
    'Ethiopia': '251',
    'Rwanda': '250'
}

student['Phone'] = student['Phone'].replace('Not Found', np.nan)

# student['Country'] = student['Country'].map(new_dict)
# student['Country'] = student['Country'].isnull()
# student['Phone'] = student['Phone'].apply(lambda x: student['Phone'].add_prefix('+') if x.startswith(phone_list) else x)

def clean_phone(phone):

    if pd.isna(phone):
        return np.nan

    if phone == "Not Found":
        return np.nan

    phone = phone.replace(" ", "")

    if phone.startswith("+"):
        return phone

    if phone.startswith(phone_list):
        return "+" + phone

    return phone

student["Phone"] = student["Phone"].apply(clean_phone)

print(student['Phone'])

# ==========================================================
# FEE CURRENCY
# ==========================================================

student['Fee Currency'] = student['Fee Currency'].str.strip().str.upper()

student['Fee Currency'] = 'USD'

print(student['Fee Currency'])

# ==========================================================
# FEE AMOUNT
# ==========================================================

bad_chars = ['Rs.', 'USD', '$', 'INR']

student['Fee Amount'] = (
    student['Fee Amount']
    .str.replace(r'\$|USD|Rs\.|INR|,', '', regex=True)
    .str.strip()
)

student['Fee Amount'] = student['Fee Amount'].astype(float)

# Save condition before converting
condition = student['Fee Amount'] > 9000

# def conditions(row):
#     if row['Fee Amount'] > 9000:
#         return row['Fee Amount'] / 80
#     else:
#         return row['Fee Amount']

# student['Fee Amount'] = student.apply(conditions, axis=1)

student['Fee Amount'] = np.where(
    student['Fee Amount'] > 9000,
    student['Fee Amount'] / 80,
    student['Fee Amount']
)

print(student['Fee Amount'])

# ==========================================================
# FEE PAID
# ==========================================================

student['Fee Paid'] = np.where(
    condition,
    student['Fee Paid'] / 80,
    student['Fee Paid']
)

print(student['Fee Paid'])

# ==========================================================
# DEADLINE DATE
# ==========================================================

student['Deadline Date'] = pd.to_datetime(
    student['Deadline Date'],
    format='mixed',
    dayfirst=True
)

print(student['Deadline Date'])

# ==========================================================
# BALANCE DUE
# ==========================================================

student['Balance Due'] = student['Fee Amount'] - student['Fee Paid']

print(student['Balance Due'])

# ==========================================================
# FEE PAYMENT STATUS
# ==========================================================

student['Fee Payment Status'] = np.where(
    student['Balance Due'] > 0,
    'Payment Due',
    'No Payment Due'
)

print(student['Fee Payment Status'])
student['Phone'] = student['Phone'].astype('string')
student.to_csv("~/student_intelligence/data/cleaned/cleaned.csv",index=False)

clean = pd.read_csv("~/student_intelligence/data/cleaned/cleaned.csv",dtype={'Phone': 'string'})

print(clean['Phone'])
print(student['Phone'].dtype)
