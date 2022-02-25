#Armin Darabi Mahboub

import re

def main():
    """input"""
    userEmail = input()

    """main progress"""
    #we are going to use regex for detecting if the email is valid or not
    if not (email_validation_check(userEmail)):
        print("WRONG")
        return
    else:
        print("OK")
        return
    

def email_validation_check(userEmail):
    #example: info8569@maktabkhooneh.org
    howManyAtsign = len(re.findall(r"@", userEmail))
    howManyDots =  len(re.findall(r"\.", userEmail))
    isThereAnySpace = len(re.findall(r"\s", userEmail))
    if howManyAtsign != 1 or howManyDots != 1 or isThereAnySpace != 0:
        return False

    beforeAtsign = re.findall(r"(.*)@", userEmail)[0]
    beforeDot = re.findall(r"@(.*)\.", userEmail)[0]
    afterDot = re.findall(r"\.(.*)", userEmail)[0]
    #afterDot must be included 2 or 3 characters
    if len(beforeAtsign) == 0 or len(beforeDot) == 0 or len(afterDot) not in [2, 3]:
        return False
    
    #beforeDot and afterDot cannot have numbers
    if not beforeDot.isalpha() or not afterDot.isalpha():
        return False

    return True

if (__name__) == "__main__":
    main()