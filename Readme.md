# Run Network with Docker.


### Create image from Dockerfile:

~~~
root@mypc:~/myfolder$ docker build -t [image-name] [/path-folder*]         
~~~
> \* dot for current folder   

#### Example:
~~~
root@mypc:~/myfolder$ docker build -t mynetwork .
~~~


------------------------------------------------------------------------------------------------------




### Create container for local use from image:
~~~
root@mypc:~/myfolder$ docker run --name [container_name] --network host -d -p 8000:8000 [image-name]
~~~



------------------------------------------------------------------------------------------------------



### Use terminal inside container:
~~~
root@mypc:~/myfolder$ docker exec -it [container_name] bash *
~~~
> \* "sh" instead of "bash" depending on your OS


#### Now, the prompt looks like this:
~~~
root@mypc:/usr/src/app#                                                  
~~~
> exit of the container: Ctrl-D



------------------------------------------------------------------------------------------------------



### First time:
~~~
root@mypc:/usr/src/app# python3 manage.py makemigrations
~~~
~~~
root@mypc:/usr/src/app# python3 manage.py migrate
~~~
~~~
root@mypc:/usr/src/app# python3 manage.py cretesuperuser  *
~~~
> \* (optional)




------------------------------------------------------------------------------------------------------



### Run Django server:
~~~
root@mypc:/usr/src/app# python3 manage.py runserver
~~~



------------------------------------------------------------------------------------------------------




#### Open in your browser: localhost:8000





------------------------------------------------------------------------------------------------------




## End.