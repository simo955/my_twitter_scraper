# My personal version of a Twitter screaper



### Build image
```docker build -v data:data/app my-screaper .```
## Run
 - Through image: ```docker run -v ${PWD}/data:/app/data simopatu/my-screaper```
- Through docker-compose: ```docker-compose run my-screaper```