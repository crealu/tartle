#!bin/bash

function run {
	echo $1
	echo 'running tart.py ... :0'
  python3 tartle$1/tart.py
}

run $1


