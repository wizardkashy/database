DROP DATABASE IF EXISTS zot4plandb;
CREATE DATABASE zot4plandb;
GO
USE zot4plandb;
GO
CREATE TABLE courses (
    id VARCHAR(25) NOT NULL,
    name VARCHAR(200) NOT NULL,
    department VARCHAR(20) NOT NULL,
    units INT NOT NULL,
    description VARCHAR(1000) NOT NULL,
    prerequisite VARCHAR(1000) NOT NULL,
    restriction VARCHAR(1000) NOT NULL,
    repeatability INT NOT NULL,
    corequisite VARCHAR (1000),
    ge VARCHAR(25) NOT NULL,
    PRIMARY KEY(id));
ALTER TABLE courses ADD FULLTEXT(id);

CREATE TABLE majors(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    major_requirement json DEFAULT NULL,
    url VARCHAR(300) NOT NULL,
    PRIMARY KEY(id));

CREATE TABLE courses_in_ges(
    id INT NOT NULL AUTO_INCREMENT,
    courseId VARCHAR(25) NOT NULL,
    geId VARCHAR(5) NOT NULL,
    PRIMARY KEY(id));

CREATE TABLE generalEducations(
    id VARCHAR(5) NOT NULL,
    name VARCHAR(55) NOT NULL,
    note VARCHAR(100) NOT NULL,
    PRIMARY KEY(id));

/*   FOREIGN KEY(geId) REFERENCES generalEducations(id),
//   FOREIGN KEY(courseId) REFERENCES courses(id));

/* CREATE TABLE generalEducations(
    id VARCHAR(10) NOT NULL,
    name VARCHAR(55) NOT NULL,
    
    PRIMARY KEY(id));

 CREATE TABLE courses_in_ge(
    courseId VARCHAR(25) NOT NULL,
    geIds VARCHAR(20) NOT NULL,
    FOREIGN KEY(courseId) REFERENCES courses(id));

INSERT INTO generalEducations VALUES ("IA","Lower-Division Requirement","Two lower-division courses");
INSERT INTO generalEducations VALUES ("IB","Upper-Division Requirement","One upper-division course");
INSERT INTO generalEducations VALUES ("II","Science and Technology","Three courses");
INSERT INTO generalEducations VALUES ("III","Social and Behavioral Sciences", "Three courses");
INSERT INTO generalEducations VALUES ("IV","Arts and Humanities", "Three courses");
INSERT INTO generalEducations VALUES ("VA","Quantitative Literacy", "One Course (and an additional course from either Va or Vb - total of three courses)");
INSERT INTO generalEducations VALUES ("VB","Formal Reasoning","One Course (and an additional course from either Va or Vb - total of three courses)");
INSERT INTO generalEducations VALUES ("VI", "Language Other Than English","One course");
INSERT INTO generalEducations VALUES ("VII","Multicultural Studies","One course that may also satisfy another GE category");
INSERT INTO generalEducations VALUES ("VIII", "International/Global Issues","One course that may also satisfy another GE category");
 */
