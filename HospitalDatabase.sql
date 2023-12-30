Create database HospitalData;
use HospitalData;

CREATE TABLE Patient (
  Patient_ID int auto_increment,
  First_Name varchar(50),
  Last_Name varchar(50),
  Phone_Number int,
  Adress varchar(50),
  Date_of_birth varchar(50),
  Email varchar(50),
  PRIMARY KEY (Patient_ID)
);

CREATE TABLE Doctor (
  Doctor_ID int auto_increment,
  First_Name varchar(50),
  Last_Name varchar(50),
  Department varchar(50),
  Specialty varchar(50),
  PRIMARY KEY (Doctor_ID)
);

CREATE TABLE Appointment (
  Appointment_ID int auto_increment,
  Doctor_ID int,
  Patient_ID int,
  Date varchar(50),
  Time varchar(50),
  Location varchar(50),
  PRIMARY KEY (Appointment_ID),
  FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID),
  FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE Medical_Prescription (
  Prescription_ID int auto_increment,
  Patient_ID int,
  Doctor_ID int,
  Medication_Name varchar(50),
  Dosage varchar(50),
  Instructions varchar(50),
  Diagnosis varchar(50),
  PRIMARY KEY (Prescription_ID),
  FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID),
  FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

SHOW COLUMNS FROM Doctor;

select * from Doctor;
