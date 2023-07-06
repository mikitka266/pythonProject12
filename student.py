import csv


class Student:
    def __init__(self, first_name, last_name, patronomic, mark, average_mark):
        self.first_name = first_name
        self.last_name = last_name
        self.patronomic = patronomic
        self.mark = mark
        self.average_mark = average_mark


    @property
    def full_name(self):
        return f'{self.first_name} {self.patronomic} {self.last_name}'


    @property
    def average_mark(self):
        return self._average_mark

    @average_mark.setter
    def average_mark(self, mark, test):
        testing=[]
        marks = []
        if 0<= test <= 100:
            testing.append(test)
        if 2<= mark <=5:
            marks.append(mark)
        else:
            raise ValueError(f'Marks and tests are not corrected')



    def __exit__(self, file_name):
        csv.dump()