The YoloV7 object detection model can be trained and evaluated in the following [Google Colab notebook](https://colab.research.google.com/drive/1mWgiQCeH25H3pVLu7JI98-XJGNznew_4?usp=sharing).

The weights trained on 5/23/2023 can be found here: [weights_5_24_2023.pt](./weights_5_24_2023.pt).

We used roboflow.com to annotate image and perform data augmentation. In order to annotate a large number of images we captured a video on the jetson nano board and split it frame by frame. We then uploaded the images to robolow and after annotating a few 100 we trained a model in robolfow to autolabel the rest of the images so they would only have to be verified rather than annotated from scratch.

The guide below shows you how to use the Colab notebook provided above to scrape the annotated images from roboflow and train a custom model.
https://blog.roboflow.com/yolov7-custom-dataset-training-tutorial/

The github linked below can be used as a comprehensive guide to set up the yolov7 model on a 4GB Jetson Nano.
After following all the steps outlined above, the only step remaining to run inference is to transfer your custom trained weights into the proper directory on the Jetson Nano.
https://github.com/patharanordev/jetson-nano-gstreamer-yolov7
