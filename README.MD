## Simple tool to analyze facebook conversations

### Run web interface 
> git clone https://github.com/vladk1/fbChatTools.git

> python server.py

### in case of problems
> virtualenv venv --distribute
> . venv/bin/activate
> pip install Flask
> python server.py

you might need to install:
> sudo pip install https://pypi.python.org/packages/source/Y/YahooBoss-Python/YahooBoss-Python-0.2.0.tar.gz

Also in case you have problems with Flask, follow:
http://flask.pocoo.org/docs/0.10/installation/

### Download messages.htm from facebook
Download your messages from facebook: https://www.facebook.com/help/131112897028467/

### Choose to upload messages:
![](http://s2.postimg.org/ok79yo84p/Screen_Shot_2015_03_30_at_14_04_30.png)

### Upload and wait around 20-30s until your messages parced 
![](http://s28.postimg.org/4r8q1aqkd/Screen_Shot_2015_03_30_at_14_04_42.png)
![](http://oi58.tinypic.com/2s85pa9.jpg)

## Now you can:


### Search for people to view statistics of most common things and frequency of conversation
/search_people
![](http://i60.tinypic.com/x5s8rm.png)



### Search for tags to find people you talk about this topic most
/search_tags
![](http://i60.tinypic.com/2s9rket.png)



### Get a matrix of your friends to compare your conversation similarity
/matrix
![](http://i60.tinypic.com/e6xb4k.png)

developed by EastSide team: [jmedvesek](https://github.com/jmedvesek) [ppalasek](https://github.com/ppalasek) [vladk1](https://github.com/vladk1)

special thanks to [nicola](https://github.com/nicola) [martol01](https://github.com/martol01)

in case you want to change messages parcer, go to:
https://github.com/vladk1/fbChatPersStats
make changes and upload new jar (fbChat.jar) here
