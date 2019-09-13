CREATE TABLE Cohort (
    CohortId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    [Name] TEXT NOT NULL UNIQUE
    );

CREATE TABLE Student (
	StudentId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL UNIQUE,
	LastName  TEXT NOT NULL UNIQUE,
	SlackHandle TEXT NOT NULL UNIQUE,
	CohortId INTEGER NOT NULL,
	FOREIGN KEY (CohortId) REFERENCES Cohort(CohortId)
	);

CREATE TABLE Instructor (
	InstructorId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL UNIQUE,
	LastName  TEXT NOT NULL UNIQUE,
	SlackHandle TEXT NOT NULL UNIQUE,
	CohortId INTEGER NOT NULL,
	Specialty TEXT NOT NULL UNIQUE,
	FOREIGN KEY (CohortId) REFERENCES Cohort(CohortId)
	);

CREATE TABLE Exercise (
	ExerciseId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	[Language] TEXT NOT NULL UNIQUE
	); 
	
CREATE TABLE StudentExercise (
	StudentExerciseId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	StudentId INTEGER NOT NULL,
	ExerciseId INTEGER NOT NULL,
	FOREIGN KEY (StudentId) REFERENCES Student(StudentId),
	FOREIGN KEY (ExerciseId) REFERENCES Exercise(ExerciseId)
	);

-- 3 cohorts
INSERT INTO Cohort (CohortId, [Name])
VALUES (null, "33");

INSERT INTO Cohort (CohortId, [Name])
VALUES (null, "37");

INSERT INTO Cohort (CohortId, [Name])
VALUES (null, "35");
-- 5 exercises
INSERT INTO Exercise (ExerciseId, [Language])
VALUES (NULL, "Javascript");

INSERT INTO Exercise (ExerciseId, [Language])
VALUES (NULL, "HTML");

INSERT INTO Exercise (ExerciseId, [Language])
VALUES (NULL, "CSS");

INSERT INTO Exercise (ExerciseId, [Language])
VALUES (NULL, "React");

INSERT INTO Exercise (ExerciseId, [Language])
VALUES (NULL, "Python");

-- 3 instructors
INSERT INTO Instructor (InstructorId, FirstName, LastName, SlackHandle, CohortId, Specialty)
VALUES (NULL, "Joe", "Shep", "JoeShep", 1, "Dad Jokes"); 

INSERT INTO Instructor (InstructorId, FirstName, LastName, SlackHandle, CohortId, Specialty)
VALUES (NULL, "Steve", "Steve", "SteveSteve", 2, "Using the pointer"); 

INSERT INTO Instructor (InstructorId, FirstName, LastName, SlackHandle, CohortId, Specialty)
VALUES (NULL, "Leah", "Leah", "Leah", 3, "Drinking caffinated water"); 

-- 7 students (don't put all students in the same cohort
INSERT INTO Student (StudentId, FirstName, LastName, SlackHandle, CohortId)
VALUES (NULL, "Sydney", "Noh", "SydneyNoh", 3); 

INSERT INTO Student (StudentId, FirstName, LastName, SlackHandle, CohortId)
VALUES (NULL, "Shane", "Miller", "ShaneMiller", 2); 

INSERT INTO Student (StudentId, FirstName, LastName, SlackHandle, CohortId)
VALUES (NULL, "Danny", "Barker", "Dannybarker", 3); 

INSERT INTO Student (StudentId, FirstName, LastName, SlackHandle, CohortId)
VALUES (NULL, "Dustin", "Hobbs", "DustinHobbs", 1); 

INSERT INTO Student (StudentId, FirstName, LastName, SlackHandle, CohortId)
VALUES (NULL, "Tyler", "Carpenter", "TylerCarpenter", 1); 

INSERT INTO Student (StudentId, FirstName, LastName, SlackHandle, CohortId)
VALUES (NULL, "Jake", "Scott", "JakeScott", 2); 

INSERT INTO Student (StudentId, FirstName, LastName, SlackHandle, CohortId)
VALUES (NULL, "Curt", "Cato", "CurtCato", 3); 

-- Assign 2 exercises to each student
INSERT INTO StudentExercise (StudentExerciseId, StudentId, ExerciseId)
VALUES (NULL, 2, 2);

INSERT INTO StudentExercise (StudentExerciseId, StudentId, ExerciseId)
VALUES (NULL, 5, 4);


