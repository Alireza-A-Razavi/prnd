FROM node:16.13.2-alpine3.15

WORKDIR /app

COPY package.json yarn.lock ./

RUN npm install

COPY . .
ENV DB_LOCAL_URL=mongodb://localhost:27017/next-docker 	: will be override in compose file
EXPOSE 3000
RUN npm build
# CMD ["npm", "dev"] 					: use as development purpose
CMD ["npm", "start"] 		