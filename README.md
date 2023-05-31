# HotelCoderFornia (Hotel Management Booking System)

<a href="https://github.com/Oshiran/HotelCoderFornia/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Oshiran/HotelCoderFornia" />
</a>

![downloads](https://img.shields.io/github/downloads/Oshiran/HotelCoderFornia/total?style=flat)
![issues](https://img.shields.io/github/issues/Oshiran/HotelCoderFornia?style=flat)
![issues-pr](https://img.shields.io/github/issues-pr/Oshiran/HotelCoderFornia?style=flat)

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

The project is Python foundation level of Hotel Booking System. The applicaiton has been built with Python and Streamlit. This has features such as a modern and intuitiave GUI for easy and fast functionality along with increased productiviey. It allows an improved user experience and makes Hotel Staff (our clients) have an easier time in booking.
PySQL is the connecting librabry to our locally hosted database hosted by XAMPP. The application has the ability to download Queries and as well as read the text files made from queries.


Feel free to reach out to any of the contributors should you need more information about the project.

## Getting Started <a name = "getting_started"></a>

To run the code in this project you will need:

- Python
- Streamlit
- Anaconda
- Xampp

### Installing

You'll need to clone the repository as below in order to run the notebooks.

```
git clone https://github.com/Oshiran/HotelCoderFornia.git
```
Download the following:
1)XAMPP
 [Download XAMPP](https://www.apachefriends.org/ "XAMPP Homepage")

2)Anaconda Virtual Enviorment
[Download Anaconda](https://www.anaconda.com/ "Anaconda Homepage")

## Usage <a name = "usage"></a>
1) Clone this Repository
Proceed as below:

```
cd /HotelCoderFornia
git clone https://github.com/Oshiran/HotelCoderFornia.git
```
2) Run XAMPP --> Apache and SQL
Check Port of SQL and match to port line 9 of main.py

3) Run SQL in PHPAdmin

    a) Create New Database
    b) Import hotel_database.sql to import database

4) Create Virtual Enviorment with Anaconda

```
conda create --name name-of-environment python=3.8
pip install -r requirements.txt
```

5) Run Streamlit App

```
streamlit run main.py
```
