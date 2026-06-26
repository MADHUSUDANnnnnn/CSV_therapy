-->This is data cleaning plan column by column
First name->Casing going to standradise first letter capital 
Last name->Casing going to be standradise First letter capital 
Phone->Preserving countryh code it have and flag where it dont have and remove 
unnecessary space and add Not found where phone number not available  
Country->Looks Fine,No need to done anything
College->Standradise Casing 
Enrollement Status->Looks Fine No need to done anything
Counsellor->>Casing required 
Fee Currency->>Must have to be standradise to USD and INR then converted to USD
Fee Amount--> Going to change in Dollar in total also convert type to numeric
Fee paid->>Going to change value in dollar
Balance Due->Have to calculate this 
Fee Payment Status->Have to calculate this
Student ID-There are 50 duplicate id that are presented same id for more than 1
person have to mark them 
Deadline Date->Have to convert datatype into datetime

Missing Values Handling-¯\_(ツ)_/¯
Each missing value is to Nan if there any placeholdr for missing value then its be 
converted to Nan
