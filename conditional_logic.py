# charge tax 
# if canadian
# and 
# when Price is greter than 1.00 dollarz

def check_country(country):
    if country.lower() == 'e':
        exit()
    elif country.lower() in ('y','n'):
        if country.lower()=='y':
            province = input("Enter Province? ('Alberta','Nunavut','Yukon','Swach','Ontario') ")
            check_province(province)
        else:
            tax = 0
            print('Tax rate is: '+ str(tax))
            print("______________________________")
            start()
    else :
        print('Please enter  Y or N')
        country = input('Are you from canada? (Y/N) ')
        check_country(country)

def check_province(province):
    if province.capitalize() in ('Alberta','Nunavut','Yukon','Swach','Ontario'):
       calculate_tax(province)
    else :
        print(province)
        print('Invalid Province')
        province = input("Enter Provice? ('Alberta','Nunavut','Yukon','Swach','Ontario') ")
        check_province(province)       

def calculate_tax(province):
    price = input('how much did yoy pay? ')
    price = float(price)
    if price  >= 1.00:
            if  province.capitalize() == 'Alberta' or province == 'Nunavut':
                tax = 0.05
            elif province.capitalize() in('Yukon','Swach'):
                tax = 0.07
            elif province.capitalize() == 'Ontario':
                tax = .13
            else:
                tax= 0.15
    else:
        tax = 0
    print('Tax rate is: '+ str(tax))
    print("______________________________")
    start()


def start():
    country = input("***Press 'e' to exit*** \nAre you from canada? (Y/N) ")
    check_country(country)


# using "and" instend of "nested if"
gpa = float(input('What is your Grade Point Average?'))
lowest_grade =float(input('What is your lowest grade?'))

if gpa>=.85 and lowest_grade>=.70:
    honour_roll=True
else:
    honour_roll=False 

if honour_roll:
    print('You made honour roll')
else:
    print('Sorry.... You did not make Honour roll')


# start Program
start()


#  be careful when comparing strings
#string comparison are string sensitive
country = 'CANADA'
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are  not from Canada') 


