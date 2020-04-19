#!/bin/bash
test=20

data=15
END=10

# Random forest 2 categories
finder="2"
outputLayer="2"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/RandomForest_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/RandomForest_ICS/main.py $finder $filename $outputLayer $test >> $path
        else
            python3 src/RandomForest_ICS/main.py $finder $filename $outputLayer $test >> $path &
        fi
    done
done

# Random forest 3 categories
finder="3"
outputLayer="3"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/RandomForest_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/RandomForest_ICS/main.py $finder $filename $outputLayer $test >> $path
        else
            python3 src/RandomForest_ICS/main.py $finder $filename $outputLayer $test >> $path &
        fi
    done
done

# Random forest multi categories
finder="multi"
outputLayer="41"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/RandomForest_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/RandomForest_ICS/main.py $finder $filename $outputLayer $test >> $path
        else
            python3 src/RandomForest_ICS/main.py $finder $filename $outputLayer $test >> $path &
        fi
    done
done