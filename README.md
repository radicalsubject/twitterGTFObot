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