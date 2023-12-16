Create database HospitalData;
use HospitalData;

create table Patient(
	Patient_ID int auto_increment primary key,
    First_Name varchar(50),
    Last_Name varchar(50)
);

insert into Patient (First_Name,Last_Name) values ("om","Un");