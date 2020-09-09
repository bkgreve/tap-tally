FROM node:14.9.0-alpine3.10 AS react
WORKDIR /usr/src/node
COPY package.json .
RUN npm install
COPY public/ ./public
COPY src/ ./src
RUN npm run build

FROM nginx
WORKDIR /var/www
COPY --from=react /usr/src/node/build /var/www/build
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf