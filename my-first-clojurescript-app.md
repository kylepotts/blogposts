---
title: My first clojurescript app
date: 2016-01-02 12:30
---

Over the last few months I have been learning Clojure and Clojurescript. If you don't know what Clojurescript is, then you can find more information [here](https://github.com/clojure/clojurescript) but basically its a way to write clojure code and convert that into Javascript which can be included in any webpage. You can use all the normal functions you have in js like dom manipulation or ajax calls. Its a really awesome way to write functional clojure and also target the web as a platform. 


I used a a plugin for Leiningen called called [lein-fighweel](https://github.com/bhauman/lein-figwheel)  which allows you to do live reloading of your code as you work. It is really helpful for beiing more productive. I also use the [Matieral Design Light](http://www.getmdl.io/) UI framework for creating the app so it could emulate an Android App which is already  being built for thr same purpose. 


***

The idea of this app comes from this terribly ugly [website](http://wpvitassuds01.itap.purdue.edu/washalertweb/washalertweb.aspx?location=f681e273-d865-4274-bf4a-ba9dea2229ce) which currently displays the status (available, unavailable, out of order, etc) of each machine and if a machine is in use then it also displays the time left till the machine is done. 

My app is redesigned version of the website. It allows you to easily view each machine status in a way that doesn't hurt your eyes. It doesn't have all the features of the Purdue Website like setting up to be emailed when a machine finishes, but I plan to implement a local version of that which gives you web notifications. I also plan on adding a filtering option as well to only display machine which are open, unavailable, etc.

Overall this was a fun way to start to learn clojurescript. I will make some follow up posts about how I made the app and what other libraries I used to help me out. 


You can find the code for the site [here](https://github.com/kylepotts/purdue-laundry-web)  and you can view the website [https://github.com/kylepotts/purdue-laundry-web](here) . And here is an screenshot of the site. 

![](http://i.imgur.com/m8c89i3.png) 
