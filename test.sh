#!/bin/bash
for i in {0..10}
do
   curl localhost:12000/HelloWorld.html &
done
