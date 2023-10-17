'''
    HR DATA - EMPLOYEE DATA ANALYTICS
'''
# Libraries 
import pandas as pd

# Loading the data and reading the CSV file

df = pd.read_csv('C:/Users/rizwa/Desktop/Rizwan/projects/HR_Data_Analysis_and_Visualization/HR_Employee_data_kaggle.csv')

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

#---------------------------------------------------------------------------------------------------

# DISTANCE CATEGORY :

# Define Distance Category based on distance
def assign_distance_category(distance):
    if distance <= 10:
        return "Less than 10km"
    elif distance <= 20:
        return "Between 10-20km"
    else:
        return "Greater than 20km"
    
# Apply the function to create the " Distance Category" column
df['Distance Category'] = df['Distance to Office'].apply(assign_distance_category)

# Check the first few rows to verify the new column
print(df[['Distance to Office', 'Distance Category']].head())

#---------------------------------------------------------------------------------------------------

# EXPERIENCE LEVEL :
# Tenure in Company

# Define experience level based on Tenure in Company
def assign_experience(tenure):
    if tenure <= 2:
        return "0-2 Years"
    elif tenure <= 5:
        return "2-5 Years"
    elif tenure <= 10:
        return "5-10 Years"
    elif tenure <= 15:
        return "10-15 Years"
    else:
        return "15+ Years"
    
# Apply the function to create the "Experience" column
df['Experience'] = df['Tenure in Company'].apply(assign_experience)

# Check the first few rows to verify the new column
print(df[['Tenure in Company', 'Experience']].head())

#---------------------------------------------------------------------------------------------------

# changing column name Rating to Performance and creating new column Rating range 1-5
df.rename(columns={'Rating': 'Performance'}, inplace=True)

# RATING :

# Define Rating based on Performance Rating
def assign_rating(rating):
    if rating == 'Very Good':
        return 5
    elif rating == 'Good':
        return 4
    elif rating == 'Average':
        return 3
    elif rating == 'Poor':
        return 2
    elif rating == 'Very Poor':
        return 1
    else:
        return 0
    
# Apply the function to create the "RATING" column
df['Rating'] = df['Performance'].apply(assign_rating)

# Check the first few rows to verify the new column
print(df[['Performance', 'Rating']].head())

#---------------------------------------------------------------------------------------------------

print(df.columns)

'''
Index(['Name', 'Gender', 'Department', 'Annual Salary', 'Location',
       'Performance', 'Distance to Office', 'Age', 'Tenure in Company',
       'Salary Category', 'Age Group', 'Distance Category', 'Experience',
       'Rating'],
      dtype='object')
'''

#---------------------------------------------------------------------------------------------------

print(df.head())

'''
                     Name  Gender   Department  Annual Salary   Location  ...       Salary Category        Age Group  Distance Category   Experience Rating
0           Aarti Panchal  Female          CEO       10000000     Mumbai  ...  Greater than 10 LPA     Between 31-40  Greater than 20km  10-15 Years      5
1             Aastha Behl  Female        Sales         880500  Bengaluru  ...          8LPA - 10LPA  Greater than 40     Less than 10km    15+ Years      5
2           Abhinaw Sinha    Male  Engineering         682200  Bengaluru  ...           6LPA - 8LPA     Less than 30    Between 10-20km   5-10 Years      4
3           Abhishek Dabb    Male        Legal         563700  New Delhi  ...           4LPA - 6LPA    Between 31-40     Less than 10km  10-15 Years      5
4  Abhishek Kumar Preetam    Male      Support        1070900  New Delhi  ...  Greater than 10 LPA      Less than 30     Less than 10km    2-5 Years      2
'''

#---------------------------------------------------------------------------------------------------

# Save the DataFrame to a CSV file
df.to_csv('Processed_HR_Data.csv', index=False)