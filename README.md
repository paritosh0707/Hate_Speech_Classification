# Hate_Speech_Classification

## Intro to project
### Background:
In today's digital age, social media platforms and online forums have become breeding grounds for hate speech, which can propagate harmful ideologies and contribute to the proliferation of discrimination and violence. Detecting and mitigating hate speech online is crucial to fostering inclusive and safe online environments.

### Objective:
The objective of this project is to develop a robust hate speech classification system using natural language processing (NLP) techniques. The system aims to accurately identify and categorize text data into hate speech, offensive language, and non-offensive language categories.


### Scope:
The scope of the project includes:

Data Collection: Gathering a diverse dataset containing textual content from social media platforms, forums, and other online sources.
Preprocessing: Cleaning and preprocessing the text data to remove noise, including stopwords, punctuation, and special characters.
Feature Extraction: Utilizing NLP techniques to extract relevant features from the text data, such as word embeddings, n-grams, and sentiment analysis.
Model Development: Training and fine-tuning machine learning and deep learning models to classify text into hate speech, offensive language, and non-offensive language categories.
Evaluation: Assessing the performance of the developed models using appropriate evaluation metrics such as accuracy, precision, recall, and F1-score.
Deployment: Implementing the trained model into a user-friendly application or API for real-time hate speech detection.


### Challenges:
Several challenges may arise during the course of the project, including:

Imbalanced Dataset: Dealing with imbalances in the dataset where hate speech instances may be significantly fewer than non-hate speech instances.
Ambiguity and Context: Addressing the ambiguity and contextual nuances present in hate speech, which may vary based on cultural, social, and linguistic factors.
Model Interpretability: Ensuring the interpretability of the developed model to understand the factors contributing to hate speech classification decisions.


### Deliverables:
The deliverables of the project include:

A comprehensive dataset annotated with hate speech labels.
Trained hate speech classification models with documented performance metrics.
Codebase and documentation for model development, evaluation, and deployment.
A report detailing the methodology, results, and insights gained from the project.
Significance:
By successfully developing an effective hate speech classification system, this project contributes to the ongoing efforts to combat online hate speech, promote digital inclusion, and foster respectful online discourse.


## Further To do task 
1. create a sreamlit app and deploy over streamlit


## Project Workflows

- constants
- config_enity
- artifact_enity
- components
- pipeline
- app.py


## How to run?

```bash
conda create -p venv python=3.8 -y
```

```bash
conda activate venv/
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```


## Deployment

1. Setting up circleCI
2. Switch on self hosted runner
3. Create Project
4. Configure EC2
5. config.yml
6. env variables
7. 



## Bug to fix
1.  To fix issue -> Model pusher to a folder model in ASW S3 bucket