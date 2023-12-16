Create database HospitalData;
use HospitalData;

CREATE TABLE `Patient` (
  `Patient ID` int auto_increment,
  `First Name` varchar(50),
  `Last Name` varchar(50),
  `Phone Number` int,
  `Adress` varchar(50),
  `Date of birth` varchar(50),
  `Email` varchar(50),
  PRIMARY KEY (`Patient ID`)
);

CREATE TABLE `Doctor` (
  `Doctor ID` int auto_increment,
  `First Name` varchar(50),
  `Last Name` varchar(50),
  `Department` varchar(50),
  `Specialty` varchar(50),
  PRIMARY KEY (`Doctor ID`)
);

CREATE TABLE `Appointment` (
  `Appointment ID` int auto_increment,
  `Doctor ID` int,
  `Patient ID` int,
  `Date` varchar(50),
  `Time` varchar(50),
  `Location` int,
  PRIMARY KEY (`Appointment ID`),
  FOREIGN KEY (`Doctor ID`) REFERENCES `Doctor`(`Doctor ID`),
  FOREIGN KEY (`Patient ID`) REFERENCES `Patient`(`Patient ID`)
);

CREATE TABLE `Medical Prescription` (
  `Prescription ID` int auto_increment,
  `Patient ID` int,
  `Doctor ID` int,
  `Medication Name` varchar(50),
  `Dosage` varchar(50),
  `Instructions` varchar(50),
  `Diagnosis` varchar(50),
  PRIMARY KEY (`Prescription ID`),
  FOREIGN KEY (`Doctor ID`) REFERENCES `Doctor`(`Doctor ID`),
  FOREIGN KEY (`Patient ID`) REFERENCES `Patient`(`Patient ID`)
);



select * from Patient;
