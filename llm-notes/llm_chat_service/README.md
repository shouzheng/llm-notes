# 环境搭建步骤

1. 搭建GPU服务器
2. 按照相应依赖 @requirements.txt
3. 下载大模型文件
4. 修改start_service.sh.template，按需修改大模型文件路径、端口、日志路径等内容
5. 执行`sh start_service.sh`，启动大模型服务
6. 执行gradio_app.py，启动gradio可视化聊天界面
7. 在jupyter环境中，导入`chat_client`模块，使用chat方法直接使用大模型服务

# 参考

- [本地部署大模型服务全攻略：从零到一的实战教程](https://mp.weixin.qq.com/s/z8h1nIBWqn3S_9ayhRGT1g)

# 可能存在的问题

若使用其他大模型，可能存在不支持vllm加载的方式，则需要做进一步的研究。