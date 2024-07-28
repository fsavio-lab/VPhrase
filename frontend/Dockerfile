FROM node:22-alpine AS builder

WORKDIR /client
COPY . .
RUN npm install 
RUN npm run build

FROM node:22-alpine AS runner
WORKDIR  /client 
COPY --from=builder /client/package.json .
COPY --from=builder /client/package-lock.json .
COPY --from=builder /client/next.config.mjs ./
COPY --from=builder /client/public ./public
COPY --from=builder /client/.next/standalone ./
COPY --from=builder /client/.next/static ./.next/static
ENV HOSTNAME 0.0.0.0

EXPOSE 3000
USER node
ENTRYPOINT ["npm","run","start"]
