# STATS418-Final-Project


The data is obtianed by webscraping HTML from IMDB Movie website, the total attribute of the data is 


1. Introduction
2. Deployment
3. Exploratory Data Analysis 
4. Modeling 
5. Conclusion

```
give examples 
```




The data is obtained by the webscraping movies' information using HTML from IMDb website by sorting the number of votes descending. The total number of instance is 351, and the reason is the number is very small is that I drop those movies whose `metascore` are not available. 


```
Deployment 
```
Everyone could access this API by following the instruction down below

** 1. To run this API, you will need change your directiory to the docker folder and run the following command line: **
`docker-compose up`

**2. You will need to open a new terminal (be in the same directory) and run the following curl command to get a response**

`curl http://localhost:5000/`

**3. We will pass these through a json formatted input through a curl POST request to the API. This is done as**

`curl -H "Content-Type: application/json" -X POST -d '{"imdb":"6.7", "metascore":"53"}' "http://localhost:5000/votes"`

This should return 
`{
  "predicted votes":52869.3919191900185
}`

Note: You may try different input value to check the predicted votes number.
**4. To stop this server, press `ctrl-C`. Furthermore, if you need to check any runing docker containers, you should enter `docker container ls` and stop them through `docker container kill <container-name>`**



THe project is using webscraping by the API and the last minutes 

This is going to be a important file to explain the main content of the project.
If you have any question, please email me at huilin.tang@ucla.edu
