class School():
    def __init__(self, school_name):
        self.school_name = school_name
        self.db = {}
        
    def add(self, name, student_grade):
        if student_grade in self.db:
            self.db[student_grade].add(name)
        else: self.db[student_grade] = {name}

    def sort(self):
        sorted_students={}
        for key in sorted(self.db.keys()):
            sorted_students[key] = tuple(sorted(self.db[key]))
        return sorted_students

    def grade(self, check_grade):
        if check_grade not in self.db: return None
        return self.db[check_grade]

