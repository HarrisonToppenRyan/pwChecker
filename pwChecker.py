# Author :  Harrison Toppen-Ryan
# Description :  Password Checker, HW5, CSCI 141
# Date :  November 21st, 2020

#Function to create a list and check if each password is valid or not
def validatePassword():
    #empty list 
    passwordList = [ ]
    #length of the password list
    lenthPasswordList = len(passwordList)
    #when the user wants to end, 'i' searches for eachpassword index in the list and checks if they are valid or not.            
    i = 0
    while True:
        #while loop that takes inouts and puts them into the list
        total_passwords = str(input())
        passwordList.append(total_passwords)
        if total_passwords == "END":
            for i in range(5):
                #if any digit in a password does not have a digit in it
                if (any(c.isdigit() for c in passwordList[i])) == False:
                    print("password", passwordList[i], "is bad. It has no digits." )
                    i += 1
                #if any digit in a password does not have a uppercase letter in it
                elif (any(c.isupper() for c in passwordList[i])) == False:
                    print("password", passwordList[i], "is bad. It has no upper case letters." )
                    i += 1
                #if any digit in a password does not have a loweercase letter in it
                elif (any(c.islower() for c in passwordList[i])) == False:
                    print("password", passwordList[i], "is bad. It has no lower case letters." )
                    i += 1
                #if any digit in a password has a space in it
                elif ' ' in passwordList[i]:
                    print("password", passwordList[i], "is bad. It has a space in it." )
                    i += 1 
                #if the password is good and can be used 
                else:
                    print("password", passwordList[i], "is good.")
                    i += 1
           
                


       
# main function that calls the vaidatePassword function after printing the text.
def main():
    print("Please input passwords one-by-one for validation.")
    print("Input END after you've entered your last password")
    validatePassword()
#call the main function 
main()