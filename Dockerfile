FROM nginx
COPY ["/home/runner/work/website/website/_site", "/usr/share/nginx/html"]
EXPOSE 80
