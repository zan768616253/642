from .person import Person, PersonType

from app import db

class Staff(Person):
    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer, db.ForeignKey('persons.id'), primary_key=True)
    date_joined = db.Column(db.Date, nullable=False)
    dept_name = db.Column(db.String(100), nullable=False)

    __mapper_args__ = {'polymorphic_identity': PersonType.STAFF.value, 'inherit_condition': staff_id == Person.id}

    def __init__(self, first_name, last_name, username, password, date_joined, dept_name):
        super().__init__(first_name, last_name, username, password, PersonType.STAFF.value)
        self.date_joined = date_joined
        self.dept_name = dept_name

    @staticmethod
    def create_staff_with_person(person, date_joined, dept_name):
        return Staff(
            first_name=person.first_name,
            last_name=person.last_name,
            username=person.username,
            password=person.password,
            date_joined=date_joined,
            dept_name=dept_name
        )
