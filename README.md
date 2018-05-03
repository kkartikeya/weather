# weather
Collect home location's Weather data and push it to Graphite through AMQP. 

* API Keys are stored in a private repository and imported via configparser python module.
* Retrieves data from both DarkSky as well as Openweather. 
* Parses and creates a protobuf. Proto file is in another repository (git@github.com:kkartikeya/protos.git)[Protos]
* Publishes the proto to an AMQP Queue from (https://www.cloudamqp.com/)[CloudAMQP]








### To clone this project:
```
git clone --recurse-submodules git@github.com:kkartikeya/weather.git
```

### To fetch latest commits from submodule
```
git submodule foreach git pull origin master
git commit -am "Pulled down update to submodule_dir"
```

### To compile the weather.proto
```
protoc --proto_path=protos/ --python_out=. protos/com/kkartikeya/home/weather/weather.proto 
```



