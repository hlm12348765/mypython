#!/bin/bash

for file in ex{1..100}.py
do
cat something.txt >>$file
done
