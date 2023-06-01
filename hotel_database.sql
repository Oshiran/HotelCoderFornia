-- Create a Schema First
CREATE Schema if NOT EXISTS hotel_database;

-- Initialize the schema
USE hotel_database;

-- Customer
-- 10 columns in total 

CREATE TABLE if NOT EXISTS Customers(
    ID int AUTO_INCREMENT PRIMARY KEY,
    L_Name varchar(255) not null,
    F_Name varchar(255) not null,
    Passport_No varchar(255) not null UNIQUE,
    Passport_Exp date not null,
    DOB date not null,
    Phone_no varchar(15) not null UNIQUE,
    Nationality varchar(255) not null,
    Sex varchar(10) check (Sex in ('Female','Male')),
    Email varchar(300) not null UNIQUE,
    Credit_Card varbinary(256) UNIQUE
);

-- Hotel Room
-- 7 Columns in total

Create TABLE if NOT EXISTS Room(
    Hotel_ID int AUTO_INCREMENT PRIMARY KEY,
    Beds int(255) not null,
    Bed_Type varchar(50) check (Bed_Type in ('Single','Double','Twin','Queen','King')),
    Price int(255) not null,
    Minibar BOOLEAN not null,
    Entertainment_system BOOLEAN not null,
    BathTub BOOLEAN not null,
    Notes varchar(255) DEFAULT '-'
);

-- Booking
-- 6 Columns in total

Create TABLE if NOT EXISTS Booking(
    Booking_ID int AUTO_INCREMENT PRIMARY KEY NOT null,
    ID int not null,
    FOREIGN KEY(ID) REFERENCES Customers(ID),
    Hotel_ID int not null,
    FOREIGN KEY(Hotel_ID) REFERENCES Room(Hotel_ID),
    Arrival_Date date not null,
    Departure_Date date not null,
    Pax int(255) not null 
);

-- Guest
-- 8 Columns in total

Create Table if NOT EXISTS Guest(
    Guest_ID int AUTO_INCREMENT PRIMARY KEY NOT null,
    Booking_ID int not null,
    FOREIGN Key (Booking_ID) REFERENCES Booking(Booking_ID),
    Guest_F_Name varchar(255) not null,
    Guest_L_Name varchar(255) not null,
    Guest_Passport varchar (255) not null,
    G_Notes varchar (255) DEFAULT '-'
);

-- When adding Records follow this order Room & Customers --> Booking --> Guest
-- Add record test to Customers
Insert into Customers () Values (null,'Jack','who','11223344','2050-12-31','1975-01-01','01234567899','Filipino','Male','1254@something.com',null);
Insert into Customers () Values (null,'Car','loss','065432456','2045-5-13','2000-3-14','4271322306','Malaysia','Male','0721@yahoo.com',null);

-- Add record test to Rooms for testing
Insert into Room () Values (null,'1','Single','250','no','no','no',null);
Insert into Room () Values (null,'2','Single','350','no','no','no',null);
Insert into Room () Values (null,'2','Double','500','yes','yes','yes',null);
Insert into Room () Values (null,'2','Twin','600','yes','yes','yes',null);
Insert into Room () Values (null,'1','Queen','750','yes','yes','yes',null);
Insert into Room () Values (null,'1','King','1000','yes','yes','yes',null);

--Add record test to booking
Insert into booking () Values (null, '1', '1', '2023-06-01', '2023-06-01','1');
Insert into booking () Values (null,'2','2','2023-05-30','2023-06-15','2');

--Add record test to Guest
Insert into Guest () Values(null,'1','Aldriech','Jones','101010101010100','-');