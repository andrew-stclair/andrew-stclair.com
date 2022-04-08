FROM nginx
COPY ["/github/workspace/_site", "/usr/share/nginx/html"]
EXPOSE 80
