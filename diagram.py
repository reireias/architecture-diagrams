from diagrams import Diagram, Cluster
from diagrams.onprem.compute import Server

with Diagram('Kubernetes on Raspberry Pi', filename='diagram'):
    with Cluster('Cluster'):
        Server('A')
        Server('B')
