1、配置代理
    go env -w GOPROXY=https://goproxy.cn
2、配置vendor
    goget -u github.com/kardianos/govendor 

​	govendor init

​	go mod vendor 

3、