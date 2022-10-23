FROM nginx:1.23.2-alpine
RUN apk update; apk upgrade --no-cache
COPY ["build", "/usr/share/nginx/html"]
EXPOSE 80
HEALTHCHECK --interval=10s --timeout=4s CMD curl -f http://localhost/ || exit 1
