FROM node:20-alpine

WORKDIR /react-vite-app

EXPOSE 3000

COPY package.json ./

RUN npm install

COPY . .

RUN npm run build

CMD ["npm", "run", "preview"]