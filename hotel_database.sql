-- Create a Schema First
CREATE Schema if NOT EXISTS hotel_database;

-- Initialize the schema
USE hotel_database;

-- Customer Table

-- 10 columns in total 

CREATE TABLE if NOT EXISTS Customers(
    ID int AUTO_INCREMENT PRIMARY KEY,
    L_Name varchar(255) not null,
    F_Name varchar(255) not null,
    Passport_No varchar(255) not null UNIQUE,
    Passport_Exp date not null,
    DOB date not null,
    Phone_no int(11) not null UNIQUE,
    Nationality varchar(255) not null,
    Sex varchar(10) check (Sex in ('Female','Male')),
    Email varchar(300) not null UNIQUE,
    Credit_Card varbinary(256) UNIQUE
);

-- Hotel Room

--7 Columns in total

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

--6 Columns in total

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

--Guest

--8 Columns in total

Create Table if NOT EXISTS Guest(
    Guest_ID int AUTO_INCREMENT PRIMARY KEY NOT null,
    ID int not null,
    FOREIGN KEY (ID) REFERENCES Customers(ID),
    Hotel_ID int not null,
    FOREIGN KEY (Hotel_ID) REFERENCES Room(Hotel_ID),
    Booking_ID int not null,
    FOREIGN Key (Booking_ID) REFERENCES Booking(Booking_ID),
    Guest_F_Name varchar(255) not null,
    Guest_L_Name varchar(255) not null,
    Guest_Passport varchar (255) not null,
    G_Notes varchar (255) DEFAULT '-'
);

