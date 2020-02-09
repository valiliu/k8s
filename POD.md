一、自主式Pod

​	无政府主义状态，一旦挂掉，无人理。

二、控制器管理的Pod

​	HPA  Horizontal Pod Autoscaling仅仅适用于Deploment和ReplicaSet，在V1版本在红仅支持根据Pod的CPU利用率扩缩容，在vlalpha版本汇总，支持根据内存和用户自定义的metric扩缩容。

​	StatefulSet 是为了解决有装填服务的问题。（Deployment和ReplicaSet是为无状态服务而设计。）	场景包括：

​	