class Course:

    def __init__(self, course:str, seats:int, term:str, mode:bool ):

        self.course_name = course
        self.seats = seats
        self.term = term
        self.mode = mode
        self.course_lst = {}

    def __str__(self):

        return f'Course:{self.course_name}; Term:{self.term}; Mode:{self.mode};Available seats:{self.seats}'
   
    def get_course(self) -> str:
        return self.course_name
    
    def get_term(self) -> str:
        return self.term
    
    def get_mode(self) -> bool:
        return self.mode

    def get_num_of_seats(self) ->int:
        return self.seats
    
    def get_student(self, in_seat:int) :
        self.in_seat = in_seat
        if self.in_seat in self.course_lst.keys():
            return self.course_lst[self.in_seat][1]
        else:
            return None

    def enroll_student(self, ID:int, name:str, in_seats:int) ->bool:
        self.ID = ID
        self.name = name
        self.in_seats = in_seats
        if self.in_seats not in self.course_lst.keys():
            if 1 <= self.in_seats <= self.seats:
                self.course_lst[self.in_seats] = (self.ID, self.name )
                return True
            else:
                return 'No seats available!'   
        
        else:
            return False

    def students_from_file(self, filename:str) ->bool:
        if not self.course_lst:
        	# enroll a list of students from file and it them to course_lst dictionary
            file = open(f'{filename}.txt', "r")
            students = file.read().split("\n")
            for i in range(0, len(students)):
                value = students[i][2:].split(":")	 # student id, name
                key = students[i][0:1].split(":")    # seat number
                self.course_lst[int(key[0])] = value # add student id, name to a corresponding seat
            return True
        else:
            return False

#Creating an object from CourseADT class
course1 = Course('CS1920', 10, 'Winter', True)

#import individual student from enroll_student method
#course1.enroll_student(123, "ABC", 7) 

# #import  list of students from file 
# course1.students_from_file("your_file_name")
