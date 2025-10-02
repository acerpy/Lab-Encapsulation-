class EmailValidator:
    def __init__(self, min_length, mails, domanis):
        self.min_length = min_length # public attribute
        self.mails = mails # public attribute
        self.domanis = domanis # public attribute
    
    def __validate_name(self, name): # private methods
        return self.min_length <= len(name)
    
    def __validate_mail(self, mail): # private methods
        for i in range(len(self.mails)):
            if(self.mails[i] == mail):
                return True
        return False
    
    def __validate_domain(self, domain): # private methods
        for i in range(len(self.domanis)):
            if(self.domanis[i] == domain):
                return True
        return False
    
    def validate(self, email): # public methods
        name = email.partition('@')
        mail = name[2].partition('.')
        domain = mail[2]

        return self.__validate_name(name[0]) == self.__validate_mail(mail[0]) == self.__validate_domain(domain)



mails = ["gmail", "softuni"] 
domains = ["com", "bg"] 
email_validator = EmailValidator(6, mails, domains) 
print(email_validator.validate("pe77er@gmail.com")) 
print(email_validator.validate("georgios@gmail.net")) 
print(email_validator.validate("stamatito@abv.net")) 
print(email_validator.validate("abv@softuni.bg")) 