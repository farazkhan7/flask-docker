# Skeleton project for flask based applications
## For Development
### Build
```shell 
docker-compose -f docker-compose.dev.yml build --no-cache
```

### Up
```shell 
docker-compose -f docker-compose.dev.yml up -d
```

### Down
```shell 
docker-compose -f docker-compose.dev.yml down
```

## For Production
### Build
```shell 
docker-compose build --no-cache
```

### Up
```shell 
docker-compose up -d
```

### Down
```shell 
docker-compose down
```
### The site will be live on port 8000 by default
