#!/bin/bash

for file in ex{1..100}.py
do
sed '1,4d'
done
