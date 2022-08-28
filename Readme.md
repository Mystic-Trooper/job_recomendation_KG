# Job Recomendation System Using Knowledge Graph

Dealing with the enormous amount of recruiting information on the Internet, a job seeker
always spends hours to find useful ones. To reduce this laborious work, we design and
implement a recommendation system for online job-hunting. **Instead of using CF
algorithms we contrast on a Knowledge RS approach** to figure out more interrelations between
candidates and job description

## Glimps of the Knowledge Graph
![image](https://user-images.githubusercontent.com/54329870/187092922-81087f78-d320-45c4-bd57-fd64cd515d7b.png)


## Architectural Overview
![image](https://user-images.githubusercontent.com/54329870/187093350-a75f5db9-8631-4911-90cc-e5f40bd0c1c3.png)

Open in the [whimsical](https://whimsical.com/knowledge-graph-A3Q7SpW1mvQQeCMRfRZdR3) for better viewing experience
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

## Future Scope
- Extending KG to more dimensions like location, salery
- Using unstructured dataset
- Native language support

## FAQ's
### 1. What is the problem statement?

we are going to leverage a knowledge graph-based recommendation system that helps candidates to find jobs according to their skillsets.

### 2. What all are the general tasks?
We analysed various aspects which help to recommend job and job descriptions based on location, age group, etc. Future - Build homogenous graph's as in resume-skills, resume-location, resume-dev_type(backend/frontend),
after that take the most popular nodes and build a heterogeneous knowledge graph

### 3. Why knowledge Graph?
A knowledge graph is self-descriptive, as it provides a single place to find the data and understand what it is all about. Knowledge graphs are being used for a wide range of applications from space, journalism, biomedicine to entertainment, network security, and pharmaceuticals.

### 4. Why Neo4j?
Neo4j delivers the lightning-fast read and write performance you need, while still protecting your data integrity.Neo4j graph algorithms are scalable and production-ready. Neo4j algorithms are written in Java and performance tested. NetworkX is a single node implementation of a graph written in Python. The response time is much faster in Neo4j.
