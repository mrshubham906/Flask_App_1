# Flask_App_1

 run the following commands for setup this project

 pip install virtualenv  
 virtualenv env  
 pip install flask     
 pip install flask_mysqldb    
 .\env\Scripts\activate.ps1   

 run the project by the following command 
 .\app.py   



# SQL queries used in “Task 2” point no “c” 

    
insert into users(
	id,
    name,
    email,
    role
    )values(
    1,
    "Amit",
   "amit@gmail.com",
    "Frontend developer"
    ),(
    2,
    "Rajat",
    "rajat@gmail.com",
    "backend developer"
    ),(
    3,
    "Ravi",
    "ravi@gmail.com",
    "UI designer"
    ),(
    4,
    "Gulshan",
    "gulshan@gmail.com",
    "fullstack developer"
    ),(
    5,
    "Abhishek",
    "abhi@gmail.com",
   "web developer"
    ),(
    6,
    "shubham",
    "shub@gmail.com",
    "java developer"
    );


select * from users;

select * from users u where u.id = 4;
 