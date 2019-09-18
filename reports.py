import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort


    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'

class Instructor():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort


    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""


    def __init__(self):
        self.db_path = "/Users/krystalgates/workspace/python/StudentExercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
            row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.StudentId,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.CohortId
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()
            for student in all_students:
                print(student)

    def all_instructors(self):

        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
            row[0], row[1], row[3], row[4]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.FirstName,
                i.LastName,
                i.SlackHandle,
                i.CohortId,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.CohortId
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()
            for instrutor in all_instructors:
                print(instrutor)

    def all_cohorts(self):

        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[0])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select [Name]
            from Cohort
            """)

            all_cohorts = db_cursor.fetchall()
            for cohort in all_cohorts:
                print(cohort)


    def all_javascriptExercises(self):

        """Retrieve all javascript exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: JavascriptExercises(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT [Language], [Name]
            FROM Exercise
            WHERE [Language] in ("Javascript");
            """)

            all_javascriptExercises = db_cursor.fetchall()
            for exercise in all_javascriptExercises:
                print(exercise)

    def all_pythonExercises(self):

        """Retrieve all python exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: PythonExercises(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT [Language], [Name]
            FROM Exercise
            WHERE [Language] IN ("Python");
            """)

            all_pythonExercises = db_cursor.fetchall()
            for exercise in all_pythonExercises:
                print(exercise)

    def all_cSharpExercises(self):

        """Retrieve all C# exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: CSharpExercises(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT [Language], [Name]
            FROM Exercise
            WHERE [Language] IN ("C#");
            """)

            all_cSharpExercises = db_cursor.fetchall()
            for exercise in all_cSharpExercises:
                print(exercise)

# Practice: Student Workload
# List the exercises assigned to each student. Display each student name and the exercises s/he has been assigned beneath their name. Use a dictionary to track each student. Remember that the key should be the student id and the value should be the entire student object.

    def students_exercise_join(self):
        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.ExerciseId,
                    e.Name,
                    s.StudentId,
                    s.FirstName,
                    s.LastName
                from Exercise e
                join StudentExercise se on se.ExerciseId = e.ExerciseId
                join Student s on s.StudentId = se.StudentId
            """)

        dataset = db_cursor.fetchall()

        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'

            if student_name not in students:
                students[student_name] = [exercise_name]
            else:
                students[student_name].append(exercise_name)

        for student_name, exercises in students.items():
            print(f'{student_name} is working on:')
            for exercise in exercises:
                print(f'\t* {exercise}')

# Practice: Assigned Exercises
# List all exercises assigned by each instructor. Display each instructor name and the exercises s/he has assigned beneath their name. Use a dictionary to track each instructor. Remember that the key should be the instructor id and the value should be the entire instructor object.

    def instructors_exercise_join(self):
        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.ExerciseId,
                    e.Name,
                    i.InstructorId,
                    i.FirstName,
                    i.LastName
                from Exercise e
                join StudentExercise se on se.ExerciseId = e.ExerciseId
                join Instructor i on i.InstructorId = se.InstructorId;
            """)

        dataset = db_cursor.fetchall()

        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            instructor_id = row[2]
            instructor_name = f'{row[3]} {row[4]}'

            if instructor_name not in instructors:
                instructors[instructor_name] = [exercise_name]
            else:
                instructors[instructor_name].append(exercise_name)

        for instructor_name, exercises in instructors.items():
            print(f'{instructor_name} has assigned:')
            for exercise in exercises:
                print(f'\t* {exercise}')

#  Practice: Popular Exercises
# Output a report in your terminal that lists all students and the exerices each is assigned. Use a dictionary to track each exercise. Remember that the key should be the exercise id and the value should be the entire exercise object.
    def exercises_students_join(self):
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.ExerciseId,
                    e.Name,
                    s.StudentId,
                    s.FirstName,
                    s.LastName
                from Exercise e
                join StudentExercise se on se.ExerciseId = e.ExerciseId
                join Student s on s.StudentId = se.StudentId;
            """)

        dataset = db_cursor.fetchall()

        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'

            if exercise_name not in exercises:
                exercises[exercise_name] = [student_name]
            else:
                exercises[exercise_name].append(student_name)

        for exercise_name, students in exercises.items():
            print(f'{exercise_name} is being worked on by:')
            for student in students:
                print(f'\t* {student}')

# Advanced Challenge: Who is Working on What and Why?
# List the students working on each exercise. Also include the instructor who assigned the exercise. Use a dictionary to track each exercise.
    def exercise_instructors_students_join(self):
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.ExerciseId,
                    e.Name,
                    i.InstructorId,
                    i.FirstName,
                    i.LastName,
                    s.FirstName,
                    s.LastName
                from Exercise e
                join StudentExercise se on se.ExerciseId = e.ExerciseId
                join Instructor i on i.InstructorId = se.InstructorId
                join Student s on s.StudentId = se.StudentId;
            """)

        dataset = db_cursor.fetchall()

        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            instructor_id = row[2]
            instructor_name = f'{row[3]} {row[4]}'
            student_name = f'{row[5]} {row[6]}'

            if exercise_name not in exercises:
                exercises[exercise_name] = [[instructor_name], [student_name]]
            else:
                exercises[exercise_name].append([[instructor_name], [student_name]])

        for exercise_name, student_teacher_names in exercises.items():
            print(f'{exercise_name}:')
            for name in student_teacher_names:
                print(f'\t* {name[0]} assigned this to {name[1]}')


class Cohort():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Cohort {self.name}'

class JavascriptExercises():

    def __init__(self, language, name):
        self.language = language
        self.name = name

    def __repr__(self):
        return f'{self.language}: {self.name}'

class PythonExercises():

    def __init__(self, language, name):
        self.language = language
        self.name = name

    def __repr__(self):
        return f'{self.language}: {self.name}'

class CSharpExercises():

    def __init__(self, language, name):
        self.language = language
        self.name = name

    def __repr__(self):
        return f'{self.language}: {self.name}'

reports = StudentExerciseReports()
# reports.all_students()
# reports.all_cohorts()
# reports.all_javascriptExercises()
# reports.all_pythonExercises()
# reports.all_cSharpExercises()
# reports.all_instructors()
# reports.students_exercise_join()
# reports.instructors_exercise_join()
# reports.exercises_students_join()
reports.exercise_instructors_students_join()





