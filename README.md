# Yes/No games

This is a client-server application. Client is written on R and server is written on python with django framework. Connection is provided with django rest framework. Server is hosted on heroku, client is hosted on shinyapps.io service. The whole application is designed to show/add so called "yes/no games".

## Accessing application

Application is available here: https://dojyandr.shinyapps.io/clientapplication/

## Running server at localhost

Aside python at PATH as environment variable, you wil have to install third-party modules via typing
```  
pip install -r requirements.txt  
```  
in terminal. Then go to diectory with "manage.py" file and write 
```
python manage.py runserver
``` 
Server will be availalble at localhost ("1217.0.0.1").

## Running client at localhost

You will have to install R and add a corresponding path environment variable path.
To run app type
```
R -e "shiny::runApp('app.R')"
```
in terminal.

## Application review
![alt-текст](https://github.com/Drusiand/SPbSTU_2021-RShiny_DjangoRest/blob/main/ClientApplication/client.png)
Left sidebar allows you to add new games in database, main panel shows panel ith avalibale games. To see answer press "+" button.
