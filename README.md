# Student Management System Project

**Explanation:**

1. **Classes:**
   - `Person`: The base class with `name` and `id_number`.
   - `Student`: Inherits from `Person` and adds `major`.
   - `Instructor`: Inherits from `Person` and adds `department`.
   - `Course`: Represents a course with `course_name`, `course_id`, and `enrolled_students` (a list).
   - `Enrollment`: Represents the relationship between a student and a course, including `grade`.

2. **Methods:**
   - **Person:**
     - `__str__()`: Returns a string representation of the person.
   - **Student & Instructor:**
     - `__str__()`: Overrides the base class method to include major or department.
   - **Course:**
     - `add_student()`: Adds a student to the enrolled list.
     - `remove_student()`: Removes a student from the enrolled list.
     - `__str__()`: Returns a string representation of the course.
   - **Enrollment:**
     - `assign_grade()`: Sets the grade for the student.
     - `__str__()`: Returns a string representation of the enrollment.
   - **StudentManagementSystem:**
     - Methods for adding, removing, updating students, instructors, courses, enrolling students, assigning grades, and retrieving student/course information.
     - `get_enrollment()`: Retrieves an `Enrollment` object based on student and course.
     - `remove_enrollments_by_student()`: Removes enrollments associated with a student.
     - `remove_enrollments_by_course()`: Removes enrollments associated with a course.

3. **OOP Principles:**
   - **Encapsulation:** Data is hidden within classes, and access is controlled through methods.
   - **Inheritance:** `Student` and `Instructor` inherit from `Person`, reducing code duplication.
   - **Polymorphism:** The `__str__()` method is overridden in subclasses to provide specific output.

4. **Example Usage:**
   - Creates an instance of `StudentManagementSystem`.
   - Demonstrates how to add, remove, update, enroll, assign grades, and retrieve information.
   - Shows how to handle removing enrollments when removing a student or a course.

This implementation follows the requirements and provides a robust structure for managing student data in an OOP manner.
