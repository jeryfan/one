FROM node:23-alpine AS builder

WORKDIR /app

COPY package.json package-lock.json /app/
RUN npm config set registry https://registry.npmmirror.com \
&& npm install

COPY . .

RUN npm run build

FROM node:23-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production

COPY --from=builder /app/.next/standalone /app/
COPY --from=builder /app/public /app/public
COPY --from=builder /app/.next/static /app/.next/static

COPY docker/entrypoint.sh ./entrypoint.sh
COPY docker/pm2.json ./pm2.json

RUN npm config set registry https://registry.npmmirror.com \
&& npm install pm2 -g && npm cache clean --force

EXPOSE 3000

CMD ["/bin/sh", "/app/entrypoint.sh"]