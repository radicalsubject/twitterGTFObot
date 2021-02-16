# twitterGTFObot
Beware! Twitter screenshot memes is no more! 
* State-enforced content originality is active on these premises. 
* The only chatbot filter you will need from here on >;) 
* No elon musks offering bitcoins!

## create environment
* _conda create -n twibot python=3.8_
* _conda env export --name twibot > env.yml_
_conda env export --no-builds > env.yml_
* _conda env create -f env.yml_
* _conda activate twibot_

## DOCKER STARTUP
docker-compose up --build

## dokku pipeline
# build the image
docker build -t dokku/test-app:v12 .
# copy the image to the dokku host
docker save dokku/test-app:v12 | ssh 178.176.224.186 "docker load"
# tag and deploy the image
ssh 178.176.224.186 "dokku tags:create test-app previous; dokku tags:deploy test-app v12"

<!-- 
docker save dokku/test-app:v12 | bzip2 | ssh 178.176.224.186 "bunzip2 | docker load" -->
git remote add dokku dokku@178.176.224.186:test