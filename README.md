# **Bayesian Personalized Ranking Recommendation systems**



Format: ![Alt Text](https://github.com/singhsonali978/Bayesian_personalized_ranking_recommendation_systems/blob/master/image.JPG)


## Our Recommendation System
The type of recommendation system that we will be discussing is known as collaborative filtering, where the features of the user (e.g. age, gender) or the item (e.g. perishable or not) itself do not play any role in the algorithm. Instead, we rely solely on the ratings that a user gave to the item

 ### Bayesian Personalized Ranking (BPR) 

#### Matrix factorization assumes that:

●	Each user can be described by features. For example, feature 1 might be a referring to how much each user likes disney movies.
●	Each item, movie in this case, can be described by an analogous set of features. To correspond to the above example, feature 1 for the movie might be a number that says how close the movie is to a disney movie.

This is all well and good, but a lot of times, what we wish to optimize for is not the difference between the true interaction and the predicted interaction, but instead is the ranking of the items. Meaning given a user, what is the top-N most likely item that the user prefers. 

And this is what Bayesian Personalized Ranking (BPR) tries to accomplish. The idea is centered around sampling positive (items user has interacted with) and negative (items user hasn't interacted with) items and running pairwise comparisons.

## Visualization

![Alt Text](https://github.com/singhsonali978/Bayesian_personalized_ranking_recommendation_systems/blob/master/Streamlit_visulaization%20App/prototype.png)
# **Steps**
1. To visualize the output open the folder Streamlit
2. Run the .py file in annaconda promt with proper path for csv files generated from the Recommender system
3. Input the User ID and type of Snack and Login
4. All set for the Snack now 

## **Reference**

1.https://github.com/microsoft/recommenders

2.https://www.streamlit.io/
