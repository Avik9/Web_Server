#!/bin/bash
for i in {0..20}
do
   curl localhost:12009/HelloWorld.html &
done
