#!/bin/bash

cd ../data
myfiles=`ls | grep .gr`
for myfile in $myfiles
do
	wc -l < $myfile
done
cd ../results
myfiles=`ls | grep _output.txt`
for myfile in $myfiles
do
	awk '{print $2}' $myfile
done
