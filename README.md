[![Build Status - GitHub](https://github.com/dazzag24/ridge_map_demo/workflows/Python%20application/badge.svg)](https://github.com/dazzag24/ridge_map_demo/actions?query=workflow%3A%22Python+application%22)

ridge_map Flask Wrapper
=======================

A simple flask wrapper of the excellent ridge plot library from [ColCarroll](https://github.com/ColCarroll/ridge_map). Live demo hosted on fly.io https://ridge-map-demo.fly.dev/ridge_map?inputcoords=-3.529,54.1743,-2.5128,54.6998&label=Lakes

Usage
-----

To build the docker image:

```
docker build -t <username>/ridge_map:1.0 .
```

To run the image:
```
docker run -p 8080:8080 <username>/ridge_map:1.0 
```

To invoke the web application:

```
http://127.0.0.1:8080/ridge_map?inputcoords=-3.529,54.1743,-2.5128,54.6998&label=Lakes
```

Examples
--------

![png](https://github.com/dazzag24/ridge_map_demo/blob/master/examples/lakes.png?raw=true)


Notes
-----
To obtain the coordinates to use in the HTTP request to the service use this [bounding box tool](https://boundingbox.klokantech.com/) and select CSV output (bottom left).



