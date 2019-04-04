# ReelLife
## You already do the hard work making the content. Let us help you reel it in.

## What is it?
Life is short. Too much goes on in our busy days. In this world, where everyone is competing for our attention, it is hard to stand out in your walk of life. Whether you are a content creator, a videographer, a vlogger or just a regular everyday person; we want to maximize your visibility while minimizing the time spent doing so.

## What does it do?
You give us videos and we'll give you a set of the best shots to choose from. ReelLife gives any content creator an easy way to find thumbnails, highlights, or even the perfect shot for your promotional material. By giving a curated list of top quality images we will cut down on time spent digging through footage looking for only the best shots.

## Who's it for?
Any and every content creator. We aspire to branch out to all mediums of content but for now focus on the visual sort.
Examples of ReelLife users:

* Instagram influencer selecting the best snapshot to post that will have the highest conversion advertising a product
* Pinterest or Reddit Subreddit user who want's to post themed content pictures that serve to highlight a subject
* Movie industry professional seeking to make trailers, promo material (posters, insta posts, tweets and online ad campaigns)
* Bloggers, magazines and photographers covering issues/events

## Core Tech
ReelLife is coded entirely in python, and runs on a Google Cloud virtual machine instance. Our Convolutional Neural Network was built using the Keras library with Tensorflow as the backend. We also used the cv2, pytube, sci-kit, and various other data science and python libraries. The dataset used to build the machine learning model was largely found on [film-grab](http://film-grab.com).

ReelLife is trained to find only the shots which best show off your videos and the people in them. Our convolutional neural network lives on Google Cloud server and is trained to find only the best shots, you can cut down on the time needed to find what you need.

![CoretechImages](https://github.com/mk1159/CookieMonster/blob/master/html5up-hyperspace/images/coretech2.jpg)

## What's next?
Our next steps would be to tackle the three different fronts that comprise this project. 

Firstly, our data. Our current dataset consists only of frontal shots of people within movie scenes. This proved to work great in the identification of a majority of highlight scenes within videos. However, a great highlight scene can still lack this frontal shot criteria and still convey a significant message to the video as a whole. We would like to expand this dataset to identify the various different highlight scenes that can exist.

Secondly, our machine learning model. Our final machine learning model was constructed by leveraging transfer learning through VGG16 as well as freezing the final layers to add our (super simple) neural network to the end of it. While this proved the concept of machine learning, various optimizations and finetuning can still be made. Research into the various paramaters used will prove beneficial in aiding any potential improvements that can be made.

Thirdly, extended functionality. While this demo proves the concept with the criteria we have specified, further improvements can still be made. Some ideas that were discussed for the next steps include being able to choose an individual within the video clip supplied and produce a highlight reel of them alone. This would allow for greater user customizability and selection of our application. 

## Who are we and why?
We are a group of computer nerds from San Francisco State University. 

We as in:
* Mohammad Khan: 
* Aashin Shazar: 
* Aaron Jacobson: 

ReelLife is a project that we came together to build during the 2019 hackathon at San Francisco State University. In this repository you may find two main folders, one consisting of all the rapid prototyped scripts and our methodology taken to ensure success and another containing our final approach.
