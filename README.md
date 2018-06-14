# RWCards

In this Introduction to Protocol Buffers on iOS, you will learn:

- xxx

##### Environment Setup
pip: 
```
sudo easy_install pip
```

Flask:
```
sudo pip install Flask
```

Python Protocol Buffer:
```
sudo -H pip install protobuf --ignore-installed six
```

Google Protocol Buffer:
```
brew install protobuf
```

Swift Protocol Buffer:
```
brew install swift-protobuf
```

##### Compile Structs
Swift:
```
protoc --swift_out=. contact.proto
```

Python:
```
protoc -I=. --python_out=. ./contact.proto
```

##### More:

- UDP Sockets
- [WebSockets](https://www.raywenderlich.com/143874/websockets-ios-starscream)

---

Source:

- [Real-Time Communication with Streams Tutorial for iOS](https://www.raywenderlich.com/157128/real-time-communication-streams-tutorial-ios)
