class Person:
    """Represents a person with a name and ID number."""

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id_number}"


class Student(Person):
    """Represents a student with a major."""

    def __init__(self, name, id_number, major):
        super().__init__(name, id_number)
        self.major = major

    def __str__(self):
        return f"{super().__str__()}, Major: {self.major}"


class Instructor(Person):
    """Represents an instructor with a department."""

    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def __str__(self):
        return f"{super().__str__()}, Department: {self.department}"


class Course:
    """Represents a course with a name, ID, and enrolled students."""

    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def add_student(self, student):
        """Adds a student to the enrolled students list."""
        self.enrolled_students.append(student)

    def remove_student(self, student):
        """Removes a student from the enrolled students list."""
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)

    def __str__(self):
        return f"Course Name: {self.course_name}, ID: {self.course_id}, Enrolled Students: {self.enrolled_students}"


class Enrollment:
    """Represents the enrollment of a student in a course."""

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None

    def assign_grade(self, grade):
        """Assigns a grade to the student for this course."""
        self.grade = grade

    def __str__(self):
        return f"Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade}"


class StudentManagementSystem:
    """Manages students, instructors, courses, and enrollments."""

    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = []

    def add_student(self, name, id_number, major):
        """Adds a new student to the system."""
        student = Student(name, id_number, major)
        self.students.append(student)
        return student

    def remove_student(self, student):
        """Removes a student from the system."""
        if student in self.students:
            self.students.remove(student)
            # Remove enrollments related to the student
            self.remove_enrollments_by_student(student)

    def update_student(self, student, name=None, id_number=None, major=None):
        """Updates a student's information."""
        if name is not None:
            student.name = name
        if id_number is not None:
            student.id_number = id_number
        if major is not None:
            student.major = major

    def add_instructor(self, name, id_number, department):
        """Adds a new instructor to the system."""
        instructor = Instructor(name, id_number, department)
        self.instructors.append(instructor)
        return instructor

    def remove_instructor(self, instructor):
        """Removes an instructor from the system."""
        if instructor in self.instructors:
            self.instructors.remove(instructor)

    def update_instructor(self, instructor, name=None, id_number=None, department=None):
        """Updates an instructor's information."""
        if name is not None:
            instructor.name = name
        if id_number is not None:
            instructor.id_number = id_number
        if department is not None:
            instructor.department = department

    def add_course(self, course_name, course_id):
        """Adds a new course to the system."""
        course = Course(course_name, course_id)
        self.courses.append(course)
        return course

    def remove_course(self, course):
        """Removes a course from the system."""
        if course in self.courses:
            self.courses.remove(course)
            # Remove enrollments related to the course
            self.remove_enrollments_by_course(course)

    def update_course(self, course, course_name=None, course_id=None):
        """Updates a course's information."""
        if course_name is not None:
            course.course_name = course_name
        if course_id is not None:
            course.course_id = course_id

    def enroll_student(self, student, course):
        """Enrolls a student in a course."""
        enrollment = Enrollment(student, course)
        self.enrollments.append(enrollment)
        course.add_student(student)

    def assign_grade(self, student, course, grade):
        """Assigns a grade to a student for a specific course."""
        enrollment = self.get_enrollment(student, course)
        if enrollment:
            enrollment.assign_grade(grade)

    def get_students_by_course(self, course):
        """Returns a list of students enrolled in a specific course."""
        return course.enrolled_students

    def get_courses_by_student(self, student):
        """Returns a list of courses a specific student is enrolled in."""
        courses = []
        for enrollment in self.enrollments:
            if enrollment.student == student:
                courses.append(enrollment.course)
        return courses

    def get_enrollment(self, student, course):
        """Returns the enrollment record for a student in a course."""
        for enrollment in self.enrollments:
            if enrollment.student == student and enrollment.course == course:
                return enrollment
        return None

    def remove_enrollments_by_student(self, student):
        """Removes all enrollments related to a specific student."""
        for i in range(len(self.enrollments) - 1, -1, -1):
            if self.enrollments[i].student == student:
                self.enrollments.pop(i)

    def remove_enrollments_by_course(self, course):
        """Removes all enrollments related to a specific course."""
        for i in range(len(self.enrollments) - 1, -1, -1):
            if self.enrollments[i].course == course:
                self.enrollments.pop(i)


# Example usage
if __name__ == "__main__":
    system = StudentManagementSystem()

    # Add students
    student1 = system.add_student("Alice", 1001, "Computer Science")
    student2 = system.add_student("Bob", 1002, "Mathematics")

    # Add instructors
    instructor1 = system.add_instructor("Dr. Smith", 2001, "Computer Science")

    # Add courses
    course1 = system.add_course("Introduction to Programming", "CS101")
    course2 = system.add_course("Calculus I", "MATH101")

    # Enroll students in courses
    system.enroll_student(student1, course1)
    system.enroll_student(student2, course2)

    # Assign grades
    system.assign_grade(student1, course1, 90)

    # Retrieve students in a course
    students_in_course1 = system.get_students_by_course(course1)
    print(f"Students in {course1.course_name}: {students_in_course1}")

    # Retrieve courses of a student
    courses_of_student1 = system.get_courses_by_student(student1)
    print(f"Courses of {student1.name}: {courses_of_student1}")

    # Remove a student
    system.remove_student(student1)

    # Retrieve students in a course again (should be empty)
    students_in_course1 = system.get_students_by_course(course1)
    print(f"Students in {course1.course_name}: {students_in_course1}")


