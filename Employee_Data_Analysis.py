#    HR DATA - EMPLOYEE DATA ANALYTICS

# Libraries 
import pandas as pd

# Loading the data and reading the CSV file

df = pd.read_csv('C:/Users/rizwa/Desktop/Rizwan/Projects/HR_Data_Analysis_and_Visualization/HR_Employee_data_kaggle.csv')

print(df.head())    # Display the first few rows of the DataFrame

print(df.info())    # Display data types and missing values

#---------------------------------------------------------------------------------------------------

# Creating additional columns 

# SALARY CATEGORY :

# Define Salary Category
def assign_Salary_Category(salary):
    if salary <= 200000:
        return "Less than 2 LPA"
    elif salary <= 400000:
        return "2LPA - 4LPA"
    elif salary <= 600000:
        return "4LPA - 6LPA"
    elif salary <= 800000:
        return "6LPA - 8LPA"
    elif salary <= 1000000:
        return "8LPA - 10LPA"
    else:
        return "Greater than 10 LPA "
    
# Apply the function to create the "Salary Category" column
df['Salary Category'] = df['Annual Salary'].apply(assign_Salary_Category)

# Check the first few rows to verify the new column
print(df[['Annual Salary', 'Salary Category']].head())

#---------------------------------------------------------------------------------------------------

# AGE GROUP :

# Define age groups 
def assign_age_group(age):
    if age <= 30:
        return "Less than 30"
    elif age <= 40:
        return "Between 31-40"
    else:
        return "Greater than 40"
    
# Apply the function to create the "Age Group" column
df['Age Group'] = df['Age'].apply(assign_age_group)

# Check the first few rows to verify the new column
print(df[['Age', 'Age Group']].head())