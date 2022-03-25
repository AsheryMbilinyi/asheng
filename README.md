
# asheng : an effective movie recommendation system based viewers' emotions and and content-based filtering

This repository contains the code for asheng, a prototype system we developed for Start Hack Hackthon. asheng employes an optimal algorithm that combines users tracked emotions while watching the movie and and movies' content-based filtering, to recommend most personalized movies for viewers to watch:


## Algorithm in detail

### Part 1: Emotional Reaction Tracking

    
        
      
 ### Part 2: Combining Viewers Emotion data and Content-Based Filtering ("asheng algorithm")

    asheng tracks emotion reaction status for each movie a viewer has watched and based on that it ranks ten similar movies.
    On the other end Machine Learning based content filtering is perfomed for each watched move to determine another ten most similar 
    movies based on contents. To give effective recommendation to the user, asheng optimally select most accurate top 
    10 similar from both ranking (emotions and content-based filtering).



## Sample recommendation based on emotion tracking
![alt text](https://github.com/AsheryMbilinyi/nyx/blob/main/asheng/asheng_algorithm.png)


## Sample recommendation based on "asheng algorithm"
![alt text](https://github.com/AsheryMbilinyi/nyx/blob/main/asheng/content_based_rec.png)
        
