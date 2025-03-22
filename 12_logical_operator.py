#Used for multiple conditions
#if applicant has high income AND  good credit 
#Eligible for loans

# has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loans")