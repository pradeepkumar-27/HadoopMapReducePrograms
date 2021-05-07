# HadoopMapReducePrograms
MapReduce programs using Python to perform operations on Hadoop clusters

## Requirements
Hadoop HDFS and MapReduce clusters to be configured. Client system to be configured with access to HDFS and MapReduce clusters. MapReduce programs to be run from client machine.

Ansible roles to configure Hadoop [HDFS](https://github.com/pradeepkumar-27/AnsibleRole-HadoopHDFS) and [MapReduce](https://github.com/pradeepkumar-27/AnsibleRole-HadoopMapReduce) clusters

## Usage

    hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming.jar --input "Your input file from HDFS" --file ./mapper.py 
    --mapper ./mapper.py --file ./reducer.py --reducer ./reducer.py --output "Your directory where the output to be stored"
