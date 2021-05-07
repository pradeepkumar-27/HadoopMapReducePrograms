# HadoopMapReducePrograms
MapReduce programs using Python to perform operations on Hadoop clusters

## Usage

    hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming.jar --input "Your input file from HDFS" --file ./mapper.py 
    --mapper ./mapper.py --file ./reducer.py --reducer ./reducer.py --output "Your directory where the output to be stored"
