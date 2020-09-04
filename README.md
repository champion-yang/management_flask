# management_flask
flask 简易框架（麻雀虽小，五脏俱全的嗷）  
## 使用到的技术记录
- 日志输出使用封装好的logger，可以将日志输出到指定文件`logs`进行持久化。
- 通过 gunicorn 在生产服务器启动。
直接启动方式`gunicorn -c gunicorn_conf.py -w 3 -b 127.0.0.1:8080 index:app`,启动
失败检查`gunicorn_conf.py`中的日志输出路径（errorlog，accesslog）
- docker 容器技术
docker主要理解镜像和容器的概念。镜像是别人封装好的上传到docker官方的镜像管理仓库的，容器是由镜像生成的运行在linux系统之上的一个玩意。
1.下载镜像`docker pull '镜像名'`
2.创建运行容器 `docker run '镜像名' `
3.构建自己的镜像 `docker build -t '镜像名' . `
4.更多容器技术可以查看官方文档呀
## 运行项目步骤
1. 把项目克隆在本地 `git clone git@github.com:champion-yang/management_flask.git`
2. 打开该项目，在终端进入 'management_flask' 目录下
3. 执行docker操作，创建自己的 'management'镜像 `docker build -t management . `
4. 通过 `docker images` 查看本机所有的镜像列表是否包括了刚刚创建的 'management' 镜像。如果没有，不可以往下执行的嗷。
5. 通过docker启动项目， `docker run -d -p 4000:8000 management` ,将项目中启动的8000端口映射到4000
6. 浏览器请求 `http://127.0.0.1:4000` ，页面又返回数据，项目启动ok。
