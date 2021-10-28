class company:
    companyname = "JVT"
    def eligibility(self):
        self.education = "B.E,B.TECH"
        print(self.education)
    def skills(self):
        self.computerlang = "c,c++"
        self.exp    = "oneyear"
        if __name__ == '__main__':      
            print(self.education,self.computerlang,self.exp,company.companyname)
      
class intcompany:
    worldpermit=True
    salary =230000
    def location(self):  
        self.location = "bangalore"
        print(self.location)
    def contact(self):
        self.mobile=9135678482
        self.email="jvt5@gmail.com"
        print(self.location,self.mobile,self.email,intcompany.salary,intcompany.worldpermit)
class emplaye:
    name = "reddy"
    def emplaye(self):
        self.dateofbirth = "2/6/1997"
        self.gender = "mail"
        self.idno = 6784567
        self.pancardno = "AWU76943"
        print(self.dateofbirth,self.gender,self.idno,self.pancardno,emplaye.name)

uday=company()
bhaskar=intcompany()
uday.eligibility()
uday.skills()
bhaskar.location()
bhaskar.contact()     
reddy=emplaye()
reddy.emplaye()

