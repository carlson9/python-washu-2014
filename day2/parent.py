class Parent():
    def __init__(self, sex, firstname, lastname):
        self.sex = sex
        self.firstname = firstname
        self.lastname = lastname
        self.kids = []

    def role(self):
        if self.sex == "Male": return "Father"
        else: return "Mother"

    def have_child(self, name):
        print self.firstname + " is having a child named " + name
        print "They will make a very good " + self.role()
        child = Child(name, self)
        self.kids.append(child)
        return child

    def list_children(self):
        for kid in self.kids:
            print "I am the " + self.role() + " of " + kid.name()

class Child():
    def __init__(self, firstname, parent):
        self.parent = parent
        self.lastname = parent.lastname
        self.firstname = firstname

    def name(self):
        return self.firstname + " " + self.lastname

    def introduce(self):
        return "Hi I'm " + self.name()


mom = Parent("Female", "Jane", "Smith")
jill = mom.have_child("Jill")
jack = mom.have_child("Jack")
mom.list_children()
print jack.introduce()
print jill.introduce()
jack.parent.kids[0].parent.list_children()
