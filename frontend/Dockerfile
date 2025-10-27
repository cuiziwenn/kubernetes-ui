# 使用轻量级 Nginx 作为前端生产环境
FROM nginx:alpine

# 设置工作目录
WORKDIR /usr/share/nginx/html

# 拷贝本地构建好的 dist 文件
COPY ./dist .

# 暴露端口
EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]

