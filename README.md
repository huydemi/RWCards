# RWCards

In this Introduction to Protocol Buffers on iOS, you will learn:

- the basic features of protocol buffers
- how to define a .proto file and generate Swift code with the compiler
- how to startup a small local server using Flask where you created a service to send a protocol buffer binary to the client
- how effortless it was to deserialize the data

##### Environment Setup
pip

```
sudo easy_install pip
```

Flask

```
sudo pip install Flask
```

Python Protocol Buffer

```
sudo -H pip install protobuf --ignore-installed six
```

Google Protocol Buffer

```
brew install protobuf
```

Swift Protocol Buffer

```
brew install swift-protobuf
```

##### Compile Structs
Swift

```
protoc --swift_out=. contact.proto
```

Python

```
protoc -I=. --python_out=. ./contact.proto
```

##### Running the Local Server:
```
python RWServer.py
```

---

Source:

- [Introduction to Protocol Buffers on iOS](https://www.raywenderlich.com/149335/introduction-protocol-buffers-ios)
