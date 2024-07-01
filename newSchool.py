from index import School

# newSchool = School('Oshogbo')
# newSchool.home_page()

class NewSchool(School):
   def __init__(self, branch, location=None):
      super().__init__(branch, location)
      self.name = 'Yello Schools'


newschool = NewSchool('Oyo')
newschool.home_page()