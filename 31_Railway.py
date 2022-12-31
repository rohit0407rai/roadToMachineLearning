class RailwayForm:
    formType="Railway Form"
    def printdata(self):
        print(f"Name is  {self.name}")
        print(f"Train is {self.train}")
arr = RailwayForm()
arr.name="Rohit"
arr.train="Gareeb rath"
arr.printdata()