
# asheng : an effective movie recommendation system based on viewers' emotion reactions and and movie contents.

This repository contains the code for asheng, a prototype system we developed for Start Hack Hackthon. asheng employes an optimal algorithm that combines users tracked emotion reaction while watching the movie and and movies' contents, to recommend most personalized movies for viewers to watch:


## Algorithm in detail

### Part 1: Emotional Reaction Tracking
asheng tracks real-time the following users reactions for every movies they have watched:
1.  Body movements ( wifi-based csi radar)
2.  ComputerVision to recognizes user's posture, sightline, facial expressions, and measures heart rate and respiration non-contact
3 . Wearable devices (like appleWatch) to get the movement, breath and heartbeat

    
        
      
 ### Part 2: Combining Viewers Emotion data and Content-Based Filtering ("asheng algorithm")

    asheng tracks emotion reaction status for each movie a viewer has watched and based on that it ranks ten similar movies.
    On the other end Machine Learning based content filtering is perfomed for each watched move to determine another ten most similar 
    movies based on contents. To give effective recommendation to the user, asheng optimally select most accurate top 
    10 similar from both ranking (emotions and content-based filtering).



## Sample recommendation based on emotion tracking
![alt text](https://github.com/AsheryMbilinyi/nyx/blob/main/asheng/asheng_algorithm.png)


## Sample recommendation based on "asheng algorithm"
![alt text](https://github.com/AsheryMbilinyi/nyx/blob/main/asheng/content_based_rec.png)
        
