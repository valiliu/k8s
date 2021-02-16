APISERVER:所有服务访问统一入口

ControllerManager：维持副本期望数目

Sheduler:负责介绍人物，选择合适的节点进行分配任务

ETCD:键值对数据库，存储K8S集群所有重要信息（持久化）【数据存储】

Kubelet：直接跟容器引擎交互，实现容器的生命周期管理

Kube-Proxy：负责写入规则至IPTABLES、IPVS实现服务映射访问的



高可用集群副本数目最好是 >=3



其他插件：

CoreDNS:可以为集群中的SVC创建一个域名IP的对应关系解析。

DashBoard： 给K8S集群提供一个B/S的结构访问体系。

Ingress Controller：官方只能实现四层代理，Ingress可以实现七层代理。

Fedration:可以提供一个可以跨级群中心多K8S统一管理功能。

Prometheus：提供一个k8s集群的监控能力。

ELK：提供K8S集群日志统一分析接入平台。

OCI
Open Container Initiative，也就是常说的OCI，是由多家公司共同成立的项目，并由linux基金会进行管理，致力于container runtime的标准的制定和runc的开发等工作。

CNI（Container Networking Interface）
CSI（Container Storage Interface）

像这样使用一种 API 对象（Deployment）管理另一种 API 对象（Pod）的方法，在 Kubernetes 中，叫作“控制器”模式（controller pattern）

“Namespace 做隔离，Cgroups 做限制，rootfs 做文件系统”
