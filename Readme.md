# Job Recomendation System Using Knowledge Graph

Dealing with the enormous amount of recruiting information on the Internet, a job seeker
always spends hours to find useful ones. To reduce this laborious work, we design and
implement a recommendation system for online job-hunting. **Instead of using CF
algorithms we contrast on a Knowledge RS approach** to figure out more interrelations between
candidates and job description

## Glimps of the Knowledge Graph
![image](https://user-images.githubusercontent.com/54329870/187092922-81087f78-d320-45c4-bd57-fd64cd515d7b.png)


## Dataset

### Resume Dataset  
The resume dataset is provided by “stack
overflow” on the “Kaggle” website in 2018. Stack Overflow did a survey in which they asked
the developer community about everything from their favorite technologies to their job
preferences. 
- There are 98,855 responses in this public data release.
- [Dataset](https://www.kaggle.com/datasets/stackoverflow/stack-overflow-2018-developer-survey)

### Job Description Dataset
The job Description dataset was created by PromptCloud's in-house web-crawling service.
This is a pre-crawled dataset, taken as a subset of a bigger dataset (more than 4.6 million job
listings) that was created by extracting data from Dice, a prominent US-based technology job
board in 2017. 
- There are 22,000 job profiles in this public data release.
- [Dataset](https://data.world/promptcloud/us-jobs-on-dice-com)


## Testing and verifying results
### Adamic Adar
- Adamic Adar is a measure used to compute the closeness of nodes based on their shared
neighbors.
- The Adamic Adar algorithm was introduced in 2003 by Lada Adamic and Eytan Adar to predict
links in a social network. It is computed using the following formula:where N(u) is the set of nodes adjacent to u.

![image](https://user-images.githubusercontent.com/54329870/187093154-629eff85-40fe-44de-9522-5e90e610492e.png)

- A value of 0 indicates that two nodes are not close, while higher values indicate nodes are
closer.

- The library contains a function to calculate closeness between two nodes.
