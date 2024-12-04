# AI in Healthcare Project

Welcome to the **AI in Healthcare** project repository! This project aims to analyze the impact of COVID-19 on various aspects of daily life using AI techniques. Below is a detailed explanation of the datasets and variables used in this project.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
  - [Merged Dataset (`merged_dataset.csv`)](#merged-dataset-merged_datasetcsv)
    - [Variables](#variables)
- [Results](#results)
- [Data Source and Citation](#data-source-and-citation)

## Project Overview

This project leverages various datasets to analyze the impacts of COVID-19, daily activities, and personal routines on participants’ mental health and behavior using advanced AI techniques. Through mobile sensing and surveys, it provides insights into changes in physical activity, emotional states, and social interactions.

## Dataset Description

This project utilizes five primary datasets to analyze the impact of COVID-19 and other factors on individuals' mental health and daily activities:

1. **Demographics Dataset (`demographics.csv`):** Contains demographic information of the survey participants, including gender and race.
2. **COVID EMA Dataset (`covid_ema.csv`):** Contains survey responses related to participants' concerns, behaviors, and daily activities during the COVID-19 pandemic.
3. **General EMA Dataset (`general_ema.csv`):** Contains additional survey responses assessing various aspects of participants' emotional states, self-esteem, stress levels, and time spent on EMAs.
4. **Steps Dataset (`steps.csv`):** Contains data on step counts segmented by different parts of the day and by hour, capturing activity patterns throughout a full day.
5. **Sensing Dataset (`sensing.csv`):** Contains detailed sensor data on participants' phone usage, physical activities, audio data, and location information.
6. **Demographics Dataset (`demographics.csv`):** This data is crucial for understanding the survey respondents' diversity and performing stratified analyses.

## Merged Dataset (`merged_dataset.csv`)

The `merged_dataset.csv` file combines data from various sources, including survey responses and sensor data, into a single comprehensive dataset. Each row represents a unique user's data on a specific date.

#### Variables
| **Variable**                | **Description**                                                                                                                                                                                                                             |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                        | **Unique User ID**<br>A unique identifier assigned to each participant in the study.                                                                                                                                                        |
| `date`                      | **Date**<br>Date of the data record in the format `YYYYMMDD`. Example: `20240430` represents April 30, 2024.                                                                                                                                |
| `covid_overall_concern`     | **Overall Concern about COVID-19**<br>Measures how concerned the participant is about COVID-19.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                                                                              |
| `covid_activity_impact`     | **Impact on Daily Activities**<br>Assesses how much the COVID-19 situation has impacted the participant's day-to-day activities in the last week.<br>**Scale:**<br>1: Not at All<br>7: Very Much                                             |
| `covid_behavior_change`     | **Behavioral Changes Due to COVID-19**<br>Evaluates the extent to which the participant has changed their behaviors in response to COVID-19 in the last week.<br>**Scale:**<br>1: Not at All<br>7: Very Much                                 |
| `covid_concern_self`        | **Concern for Self Regarding COVID-19**<br>Measures how concerned the participant is for themselves regarding COVID-19.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                                                       |
| `covid_concern_classmates`  | **Concern for Classmates Regarding COVID-19**<br>Assesses how concerned the participant is for their classmates regarding COVID-19.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                                           |
| `covid_concern_family`      | **Concern for Family Regarding COVID-19**<br>Evaluates how concerned the participant is for their family regarding COVID-19.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                                                  |
| `covid_concern_supplies`    | **Concern about Obtaining Supplies**<br>Measures how concerned the participant is about obtaining food, supplies, etc., during COVID-19.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                                      |
| `feeling_supported`         | **Feeling of Support**<br>Assesses how supported the participant feels.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                                                                                                      |
| `social_media_usage_change` | **Change in Social Media Usage**<br>Evaluates whether the participant's social media usage has increased or decreased compared to normal.<br>**Scale:**<br>1: Much Less Than Normal<br>4: Normal<br>7: Much More Than Normal                |
| `phq4_total_score`          | **PHQ-4 Total Score**<br>Aggregated score from the PHQ-4 questionnaire, measuring symptoms of anxiety and depression.<br>**Range:** 0 to 12<br>Higher scores indicate greater severity.                                                     |
| `current_stress_level`      | **Current Stress Level**<br>Assesses the participant's current stress level at the time of the survey.<br>**Scale:**<br>1: Not at All<br>5: Extremely                                                                                       |
| `is_ios`                    | **Device Type**<br>Indicates whether the participant is using an iOS device (`1`) or an Android device (`0`).                                                                                                                               |
| `sleep_duration_hours`      | **Sleep Duration (Hours)**<br>Total sleep duration in hours, as reported by the participant through surveys.                                                                                                                                |
| `sleep_heathkit_dur`        | **Sleep Duration from HealthKit (Hours)**<br>Total sleep duration in hours, as recorded by Apple HealthKit (available for iOS devices only).                                                                                                |
| `steps_full_day`            | **Full Day Steps**<br>Total number of steps recorded over the full day.                                                                                                                                                                     |
## Results
![image](https://github.com/user-attachments/assets/dce13339-df82-4797-829f-a2e0d9887282)
![image](https://github.com/user-attachments/assets/526e52fe-7486-4adf-aad6-6415dfa43f8e)
![image](https://github.com/user-attachments/assets/ee3b7164-0aae-4785-b3c1-c16650f4a407)
Before COVID
![image](https://github.com/user-attachments/assets/a8f01877-1874-4475-9dc0-8133f666ef59)
After COVID
![image](https://github.com/user-attachments/assets/300bf3b1-bc0a-40f9-bc93-e2092ab251e0)
![image](https://github.com/user-attachments/assets/f4cf462a-dccc-446d-896e-b5b9d8c38999)
![image](https://github.com/user-attachments/assets/ca64eded-a2d2-4be4-8fe4-e4a9dc81279e)
![image](https://github.com/user-attachments/assets/43006d4a-4c90-404e-b6e6-0f4598250f68)
![image](https://github.com/user-attachments/assets/66e74183-c0f8-499f-af2e-bd2d3d914524)
![image](https://github.com/user-attachments/assets/27a093c6-ac5b-4bf0-8e9b-8323803caff6)

### Comparative Analysis of Sleep Duration Trends: Pre-COVID vs. During-COVID
![image](https://github.com/user-attachments/assets/9ce67454-ef72-4230-87e6-46acf460a990)
![image](https://github.com/user-attachments/assets/180f003e-a075-441b-820d-4dffc3a12707)

### Comparative Analysis of Stress Level Trends: Pre-COVID vs. During-COVID
![image](https://github.com/user-attachments/assets/39a6a1fd-d7d2-499c-ba3d-efb6178227ad)
![image](https://github.com/user-attachments/assets/dee258ff-a34d-48a2-b50b-34c663124f1a)

### Feature Importance for Pre-COVID Stress Prediction Model
![image](https://github.com/user-attachments/assets/10841c86-1dcf-4b04-9f9b-e09e1ef6f18b)

### Feature Importance for During-COVID Stress Prediction Model
![image](https://github.com/user-attachments/assets/ad5826c7-61d8-4bdb-84dd-ec5cdcbe9390)

### Feature Importance for Pre-COVID Sleep Prediction Model
![image](https://github.com/user-attachments/assets/b3704fbb-76c2-4cc6-85ea-0327d63a1134)

### Feature Importance for During-COVID Sleep Prediction Model
![image](https://github.com/user-attachments/assets/d6a557a6-56ae-473c-9b49-83a2cf2adffe)

### Sleep Duration Trends
- **Pre-COVID Sleep Duration:** Average sleep duration before the pandemic was **7.42 hours**.
- **During-COVID Sleep Duration:** During the pandemic, sleep duration increased to **7.58 hours**, a statistically significant difference (**p-value < 0.001**).
- **Variability:** Sleep duration variability remained consistent across both periods.

### Stress Level Trends
- **Pre-COVID Stress Levels:** Average reported stress level was **2.44** (scale: 1 to 5).
- **During-COVID Stress Levels:** Stress levels increased to **2.65**, a statistically significant rise (**p-value < 0.001**).
- **Correlation Analysis:** During the pandemic, a stronger negative correlation between sleep duration and stress was observed (**correlation: -0.124**) compared to pre-pandemic (**correlation: -0.066**), though neither was statistically significant.

### Predictive Modeling Results

#### Stress Prediction
- **Pre-COVID Model Performance:**
  - **RMSE:** 0.4270
  - **R²:** 22.76%
  - **Top Feature:** Sleep duration, followed by PHQ-4 scores.
- **During-COVID Model Performance:**
  - **RMSE:** 0.3578
  - **R²:** 25.57%
  - **Top Features:** Sleep duration, PHQ-4 scores, and general COVID concerns.

#### Sleep Prediction
- **Pre-COVID Model Performance:**
  - **RMSE:** 2.6309
  - **R²:** 2.49%
  - **Top Feature:** Step count was the strongest predictor, followed by PHQ-4 scores.
- **During-COVID Model Performance:**
  - **RMSE:** 2.5922
  - **R²:** 3.01%
  - **Top Features:** Step count remained the most significant factor, with stress levels and COVID-related impacts also contributing.

### Feature Importance
- **Stress Prediction Models:**
  - **Pre-COVID:** Sleep duration and PHQ-4 scores were the dominant predictors.
  - **During-COVID:** Sleep duration, PHQ-4 scores, and general COVID concerns were the most impactful.
- **Sleep Prediction Models:**
  - **Pre-COVID:** Physical activity (step count) was the strongest determinant of sleep duration.
  - **During-COVID:** Step count and stress levels retained significance, with COVID-related disruptions emerging as additional predictors.

### Summary of Insights
- Sleep duration increased slightly during the pandemic, likely due to lifestyle adjustments such as remote learning.
- Stress levels also rose modestly, with peaks aligning with academic stressors.
- Predictive models emphasized the role of sleep duration in managing stress and highlighted physical activity as a consistent determinant of sleep.

These results provide valuable insights into the interplay between sleep, stress, and pandemic-related disruptions, highlighting opportunities for targeted interventions.

## Data Source and Citation

The dataset used in this project was taken from the following source:

Subigya Nepal, Wenjun Liu, Arvind Pillai, Weichen Wang, Vlado Vojdanovski, Jeremy F. Huckins, Courtney Rogers, Meghan L. Meyer, and Andrew T. Campbell. 2024. **Capturing the College Experience: A Four-Year Mobile Sensing Study of Mental Health, Resilience, and Behavior of College Students during the Pandemic**. *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*, 8(1), Article 38 (March 2024), 37 pages. [https://doi.org/10.1145/3643501](https://doi.org/10.1145/3643501)
