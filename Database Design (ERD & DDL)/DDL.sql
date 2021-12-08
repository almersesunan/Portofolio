--DDL
CREATE TABLE Class (
  ID        INT NOT NULL, 
  CourseID  INT NOT NULL, 
  StudentID INT NOT NULL, 
  PRIMARY KEY (ID));
 
CREATE TABLE Course (
  ID           INT NOT NULL, 
  DepartmentID INT NOT NULL, 
  LecturerID   INT NOT NULL, 
  CourseName   varchar(255), 
  PRIMARY KEY (ID));
 
CREATE TABLE Department (
  ID             INT NOT NULL, 
  DepartmentName varchar(255), 
  Location       varchar(255), 
  PRIMARY KEY (ID));
 
CREATE TABLE Lecturer (
  ID            INT NOT NULL, 
  DepartmentID  INT NOT NULL, 
  FirstName     varchar(255), 
  LastName      varchar(255), 
  LecturerPhone varchar(255), 
  PRIMARY KEY (ID));
 
CREATE TABLE Student (
  ID           INT NOT NULL, 
  FirstName    varchar(255), 
  LastName     varchar(255), 
  StudentPhone varchar(255), 
  PRIMARY KEY (ID));
 
ALTER TABLE Class ADD CONSTRAINT FKClassStudent FOREIGN KEY (StudentID) REFERENCES Student (ID);
ALTER TABLE Class ADD CONSTRAINT FKClassCourse FOREIGN KEY (CourseID) REFERENCES Course (ID);
ALTER TABLE Course ADD CONSTRAINT FKCourseLecturer FOREIGN KEY (LecturerID) REFERENCES Lecturer (ID);
ALTER TABLE Course ADD CONSTRAINT FKCourseDepartment FOREIGN KEY (DepartmentID) REFERENCES Department (ID);
ALTER TABLE Lecturer ADD CONSTRAINT FKLecturerDepartment FOREIGN KEY (DepartmentID) REFERENCES Department (ID);

--DML
INSERT INTO Student
VALUES 
  (1, 'Almer', 'Sesunan', '082188778887'),
  (2, 'Evi', 'Millenia', '082299273682'),
  (3, 'Dandi', 'Hanoman', '081371829364');
 
INSERT INTO Department
VALUES 
  (1, 'Computer Science', 'Anggrek'),
  (2, 'Cyber Security', 'Kijang'),
  (3, 'Game Application Technology', 'Syahdan');
 
INSERT INTO Lecturer
VALUES 
  (1, 1, 'Rendi', 'Saskia', '088991376867'),
  (2, 2, 'Ghina', 'Nabila', '081293751034'),
  (3, 3, 'Akbar', 'Mahendra', '088728160098');
 
INSERT INTO Course
VALUES 
  (1, 1, 1, 'Algorithm'),
  (2, 2, 2, 'Database'),
  (3, 3, 3, 'Networking');
 
INSERT INTO Class
VALUES 
  (001, 1, 1),
  (002, 2, 2),
  (003, 3, 3);


