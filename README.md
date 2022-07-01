# funnyfactsapp

Solution has been wrtten in Django Rest Framework for it's simplicity. 
For the database engine i chose MySQL. The choice was made only by my private preferences. 
For testingpurposes i am using pytest. This module is the moste convinient way to do the tests, in my opinion.


!! Before instalation provide propper value of secret key in line 4 of Dockerfile !!

Installation guide
  Requirements : 
    1. Docker
    2. Git
  Installation : 
    If requirements are met do as follow :
      1. Clone git repository https://github.com/mpasz/funnyfactsapp
      2. In the terminal pass : docker-compose up --build
  
  Note : 
    if you have MySql installed, stop the services to avoid ports conflict. 
    
  
