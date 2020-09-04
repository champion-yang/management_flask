# management_flask
flask 简易框架（麻雀虽小，五脏俱全的嗷）  
## 使用到的技术记录
- 日志输出使用封装好的logger，可以将日志输出到指定文件`logs`进行持久化。
- 通过 gunicorn 在生产服务器启动。
直接启动方式`gunicorn -c gunicorn_conf.py -w 3 -b 127.0.0.1:8080 index:app`,启动
失败检查`gunicorn_conf.py`中的日志输出路径（errorlog，accesslog）

## 