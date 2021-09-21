from diagrams import Diagram, Cluster
from diagrams.onprem.compute import Server
from diagrams.k8s.infra import Master
from diagrams.k8s.infra import Node
from diagrams.k8s.storage import PV
from diagrams.onprem.monitoring import Prometheus
from diagrams.generic.blank import Blank
from diagrams.generic.storage import Storage

with Diagram('Kubernetes on Raspberry Pi', filename='diagram'):
    with Cluster('host: model3b'):
        prometheus = Prometheus()
    with Cluster('k8s cluster'):
        pv = PV()
        with Cluster('host: pikube01'):
            n01 = Master('pikube01')
            ex01 = Prometheus('node_exporter')
        with Cluster('host: pikube02'):
            n02 = Node('pikube02')
            ex02 = Prometheus('node_exporter')
        with Cluster('host: pikube03'):
            n03 = Node('pikube03')
            ex03 = Prometheus('node_exporter')
        with Cluster('host: pikube04'):
            nfs = Storage('NFS')
            ex04 = Prometheus('node_exporter')

    [n01, n02, n03] >> pv
    pv >> nfs
    [ex01, ex02, ex03, ex04] << prometheus
