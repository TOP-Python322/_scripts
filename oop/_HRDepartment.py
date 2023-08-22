from random import choice


class Employee:
    def __init__(self, name: str):
        self.name = name


class Candidate:

    class Form:
        questions: list[str]

        def __init__(self, answers: list[str]):
            self.answers = answers

    def __init__(
            self,
            name: str,
            email: str,
            form: Form,
    ):
        self.name = name
        self.email = email
        self.__form = form
        self._interviewer: Employee = None

    def __repr__(self):
        return f'<{self.name}: {self.email}>'

    def check_form(self) -> bool:
        ...
        return choice((True, True, True, True, False))

    def set_first_interview(self, interviewer: Employee) -> None:
        ...
        self._interviewer = interviewer
        ...

    def first_interview(self) -> bool:
        ...
        return choice((True, True, True, False))


class HRDepartment:
    def __init__(self):
        self.employees: list[Employee] = []
        self.candidates: list[Candidate] = []

    def hire(self, candidate: Candidate) -> Employee:
        self.candidates.remove(candidate)
        employee = Employee(candidate.name)
        self.employees.append(employee)
        return employee

