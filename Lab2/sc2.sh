#!/bin/sh

if echo "$1" | grep '*'
then 
	echo "Symbol is not Required"
else
	echo "'*' is Required"
	echo ""$1"/*"
fi
