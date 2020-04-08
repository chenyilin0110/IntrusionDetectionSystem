#!/bin/bash

train="train"
test="test-21"
estimators="100"

END=5

# Random Forest 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/RandomForest/main.py $train $test $outputLayer $estimators >> src/RandomForest/result/experimental_result_2-21.txt
    else
        python3 src/RandomForest/main.py $train $test $outputLayer $estimators >> src/RandomForest/result/experimental_result_2-21.txt &
    fi
done

# Random Forest 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/RandomForest/main.py $train $test $outputLayer $estimators >> src/RandomForest/result/experimental_result_5-21.txt
    else
        python3 src/RandomForest/main.py $train $test $outputLayer $estimators >> src/RandomForest/result/experimental_result_5-21.txt &
    fi
done