#!/bin/sh

mvn compile && mvn exec:java -Dexec.mainClass="example.twitterstreaminglocation.LocationTrainerApp"
