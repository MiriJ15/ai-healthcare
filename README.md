# AI in Healthcare Project

Welcome to the **AI in Healthcare** project repository! This project aims to analyze the impact of COVID-19 on various aspects of daily life using AI techniques. Below is a detailed explanation of the datasets and variables used in this project.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
  - [Merged Dataset (`merged_dataset.csv`)](#merged-dataset-merged_datasetcsv)
    - [Variables](#variables)
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

## Data Source and Citation

The dataset used in this project was taken from the following source:

Subigya Nepal, Wenjun Liu, Arvind Pillai, Weichen Wang, Vlado Vojdanovski, Jeremy F. Huckins, Courtney Rogers, Meghan L. Meyer, and Andrew T. Campbell. 2024. **Capturing the College Experience: A Four-Year Mobile Sensing Study of Mental Health, Resilience, and Behavior of College Students during the Pandemic**. *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*, 8(1), Article 38 (March 2024), 37 pages. [https://doi.org/10.1145/3643501](https://doi.org/10.1145/3643501)
