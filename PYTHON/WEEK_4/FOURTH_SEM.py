import copy
import random


class FourthSem:
    def __init__(self):
        self.roll_no = []
        self.test1marks = []
        self.test2marks = []
        self.test3marks = []
        for i in range(20):
            self.roll_no.append(i)
            self.test1marks.append(random.randint(0, 100))
            self.test2marks.append(random.randint(0, 100))
            self.test3marks.append(random.randint(0, 100))

    def class_avg(self):
        test1avg = 0
        test2avg = 0
        test3avg = 0
        for i in range(20):
            test1avg += self.test1marks[i]
            test2avg += self.test2marks[i]
            test3avg += self.test3marks[i]
        test1avg = round(test1avg / 20, 2)
        test2avg = round(test2avg / 20, 2)
        test3avg = round(test3avg / 20, 2)
        avg = [test1avg, test2avg, test3avg]
        return avg

    def avg_each_student(self):
        avg_student = []
        for i in range(20):
            avg_student.append(round((self.test1marks[i] + self.test2marks[i] + self.test3marks[i]) / 3, 2))
        return avg_student

    def top_list(self):
        test1 = copy.deepcopy(self.test1marks)
        test2 = copy.deepcopy(self.test2marks)
        test3 = copy.deepcopy(self.test3marks)
        test1.sort(reverse=True)
        test2.sort(reverse=True)
        test3.sort(reverse=True)
        print("Test1\tTest2\tTest3")

        print("Top 5 scores")

        for i in range(5):
            print(f" {test1[i]}  \t {test2[i]}  \t {test3[i]}")

        print("Last 5 scores")

        for i in range(15, 20):
            print(f" {test1[i]}  \t {test2[i]}  \t {test3[i]}")


test = FourthSem()
print(f"Each test class avg:{test.class_avg()}")
print(f"Each student avg in test:{test.avg_each_student()}")
test.top_list()
