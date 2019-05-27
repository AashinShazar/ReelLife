# Methodology

## Data Collection
When it came to data collection, we were on a severe time crunch given the nature of the hackathon. So we made the decision to focus solely on action shots in popular movies. We defined an action shot as anything that was significant or revealing about the character or the movie itself. We established a loose criteria that primarily focusde on the clear visibility of an actor's face. But at the same time we also allowed for each individual within the group to select what we thought were "cool" shots. 

You may see some examples at the following link: https://imgur.com/a/OmwP63S

## Machine Learning
When it came to machine learning, we believe it was best to apply a convolutional neural network for the image classification task at hand. We first established a benchmark model just to have a baseline to compare to for future improved iterations. We then experimented with transfer learning, freezing layers and varying levels of data augmentation to see if this benchmark model could be further improved. We finally arrived at a final model that combined the usage of transfer learning and data augmentation. 

## Website
When it came to the interactive and presentation portion, we had hoped to link this website to the backend jupyter notebook so that users could input youtube videos and watch our application perform. Due to time constraints, unfortunately this linkage did not happen and were two seperate componenets instead. 

## Credits

### IMDb-Face.csv

@article{wang2018devil,
	title={The Devil of Face Recognition is in the Noise},
	author={Wang, Fei and Chen, Liren and Li, Cheng and Huang, Shiyao and Chen, Yanjie and Qian, Chen and Loy, Chen Change},
	journal={arXiv preprint arXiv:1807.11649},
	year={2018}
}
