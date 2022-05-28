class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, change_name):
        self.change_name = change_name
        print("Name was changed from", self.name, "to", change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        print("Age was changed from", self.age, "to", change_age)

    def add_track(self, add_track):
        self.add_track = add_track
        #print("add_track was added to", self.tracks)
        print("add track to", self.tracks)

    def get_score(self, get_score):
        self.get_score = self.score
        print("Score wasn't changed and remains", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(20.90)
