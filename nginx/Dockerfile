FROM nginx:1.21.0-alpine AS production

RUN rm /etc/nginx/conf.d/*

COPY ./default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx","-g","daemon off;"] 