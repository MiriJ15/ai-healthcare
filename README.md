# AI in Healthcare Project

Welcome to the **AI in Healthcare** project repository! This project aims to analyze the impact of COVID-19 on various aspects of daily life using AI techniques. Below is a detailed explanation of the datasets and variables used in this project.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
  - [Demographics Dataset (`demographics.csv`)](#demographics-dataset-demographicscsv)
    - [Variables](#variables-1)
  - [COVID EMA Dataset (`covid_ema.csv`)](#covid-ema-dataset-covid_emacsv)
    - [Variables](#variables)
  - [General EMA Dataset (`general_ema.csv`)](#general-ema-dataset-general_emacsv)
    - [Variables](#variables-2)
  - [Steps Dataset (`steps.csv`)](#steps-dataset-stepscsv)
    - [Variables](#variables-3)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview


## Dataset Description

This project utilizes three primary datasets to analyze the impact of COVID-19 and other factors on individuals' mental health and daily activities:

1. **Demographics Dataset (`demographics.csv`):** Contains demographic information of the survey participants, including gender and race.
2. **COVID EMA Dataset (`covid_ema.csv`):** Contains survey responses related to participants' concerns, behaviors, and daily activities during the COVID-19 pandemic.
3. **General EMA Dataset (`general_ema.csv`):** Contains additional survey responses assessing various aspects of participants' emotional states, self-esteem, stress levels, and time spent on EMAs.
4. **Steps Dataset (`steps.csv`):** Contains data on step counts segmented by different parts of the day and by hour, capturing activity patterns throughout a full day.


### Demographics Dataset (`demographics.csv`)

The `demographics.csv` file contains demographic information of the survey participants. This data is crucial for understanding the diversity of the survey respondents and for performing stratified analyses.

#### Variables

Below is a detailed description of each variable in the `demographics.csv` dataset:

| **Variable** | **Description**                                                                                                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`         | **Unique User ID**<br>A unique identifier that matches the `id` in the `covid_ema.csv` and `general_ema.csv` datasets, ensuring that demographic information corresponds to the correct survey responses.     |
| `gender`     | **Gender**<br>The gender of the participant.                                                                                                                                         |
| `race`       | **Race**<br>The racial background of the participant.                                                                                                                                |

### COVID EMA Dataset (`covid_ema.csv`)

The `covid_ema.csv` file consists of survey responses collected to assess the impact of COVID-19 on individuals' concerns, behaviors, and daily activities. Each row in the dataset represents a unique user's responses on a specific date.

#### Variables

Below is a detailed description of each variable in the `covid_ema.csv` dataset:

| **Variable**                | **Description**                                                                                                                                                                                                                                      |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                        | **Unique User ID**<br>A unique identifier assigned to each participant in the survey.                                                                                                                                                              |
| `date`                      | **Date**<br>Date of the survey response in the format `YYYYMMDD`. Example: `20240430` represents April 30, 2024.                                                                                                                                    |
| `covid_overall_concern`     | **Overall Concern about COVID-19**<br>Measures how concerned the participant is about COVID-19.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                                                                                 |
| `covid_activity_impact`     | **Impact on Daily Activities**<br>Assesses how much the COVID-19 situation has impacted the participant's day-to-day activities in the last week.<br>**Scale:**<br>1: Not at All<br>7: Very much                                           |
| `covid_behavior_change`     | **Behavioral Changes Due to COVID-19**<br>Evaluates the extent to which the participant has changed their behaviors in response to COVID-19 in the last week.<br>**Scale:**<br>1: Not at All<br>7: Very much                                   |
| `covid_concern_self`        | **Concern for Self Regarding COVID-19**<br>Measures how concerned the participant is for themselves regarding COVID-19.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                                          |
| `covid_concern_classmates`  | **Concern for Classmates Regarding COVID-19**<br>Assesses how concerned the participant is for their classmates regarding COVID-19.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                               |
| `covid_concern_family`      | **Concern for Family Regarding COVID-19**<br>Evaluates how concerned the participant is for their family regarding COVID-19.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                                          |
| `covid_concern_supplies`    | **Concern about Obtaining Supplies**<br>Measures how concerned the participant is about obtaining food, supplies, etc., during COVID-19.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                               |
| `feeling_supported`         | **Feeling of Support**<br>Assesses how supported the participant feels.<br>**Scale:**<br>1: Not at All<br>7: Extremely                                                                                                                  |
| `supporting_others`         | **Supporting Others**<br>Measures how much the participant has supported others.<br>**Scale:**<br>1: Not at All<br>7: Very much                                                                                                             |
| `social_media_usage_change` | **Change in Social Media Usage**<br>Evaluates whether the participant's social media usage has increased or decreased compared to normal.<br>**Scale:**<br>1: Much less than normal<br>4: Normal<br>7: Much more than normal          |

### General EMA Dataset (`general_ema.csv`)

The `general_ema.csv` file contains survey responses assessing various aspects of participants' emotional states, self-esteem, stress levels, and time spent on Ecological Momentary Assessments (EMAs). Each row represents a unique user's responses on a specific date.

#### Variables

Below is a detailed description of each variable in the `general_ema.csv` dataset:

| **Variable**                | **Description**                                                                                                                                                                                                                                      |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                        | **Unique User ID**<br>A unique identifier assigned to each participant in the survey.                                                                                                                                                              |
| `date`                      | **Date**<br>Date of the survey response in the format `YYYYMMDD`. Example: `20240430` represents April 30, 2024.                                                                                                                                    |
| `photographic_affect_meter_score` | **Photographic Affect Meter Score**<br>Photographic Affect Meter scores. The user chooses an image from 16 pictures. Valence and arousal are calculated based on the rubric mentioned [here](https://dl.acm.org/doi/10.1145/1978942.1979047). Range: 1 to 16 |
| `phq4_feeling_nervous`      | **PHQ4 - Feeling Nervous**<br>Over the last 2 weeks, how often have you been bothered by feeling nervous, anxious, or on edge?<br>**Scale:**<br>0: Not at all;<br>1: Several days;<br>2: More than half the days;<br>3: Nearly every day |
| `phq4_worry_control`        | **PHQ4 - Worry Control**<br>Over the last 2 weeks, how often have you been bothered by not being able to stop or control worrying?<br>**Scale:**<br>0: Not at all;<br>1: Several days;<br>2: More than half the days;<br>3: Nearly every day |
| `phq4_feeling_depressed`    | **PHQ4 - Feeling Depressed**<br>Over the last 2 weeks, how often have you been bothered by feeling down, depressed, or hopeless?<br>**Scale:**<br>0: Not at all;<br>1: Several days;<br>2: More than half the days;<br>3: Nearly every day |
| `phq4_little_interest`      | **PHQ4 - Little Interest**<br>Over the last 2 weeks, how often have you been bothered by having little interest or pleasure in doing things?<br>**Scale:**<br>0: Not at all;<br>1: Several days;<br>2: More than half the days;<br>3: Nearly every day |
| `phq4_response_time_mean_sec` | **PHQ4 - Mean Response Time (sec)**<br>Mean time spent on PHQ4 EMAs (in seconds).                                                                                                                                                                |
| `phq4_response_time_median_sec` | **PHQ4 - Median Response Time (sec)**<br>Median time spent on PHQ4 EMAs (in seconds).                                                                                                                                                            |
| `phq4_total_score`          | **PHQ4 Total Score**<br>Aggregated PHQ4 Score (Sum of `phq4_feeling_nervous` to `phq4_little_interest`).                                                                                                                                       |
| `social_interaction_level`  | **Social Interaction Level**<br>Have you spent most of your time alone or with others today?<br>**Scale:**<br>1: Almost always alone;<br>2: Mostly alone, a little time with others;<br>3: Equal amounts of time alone and with others;<br>4: Mostly with others, a little time alone;<br>5: Almost always with others |
| `sse3_worry_about_others_think` | **SSE3 - Worry About Others' Thoughts**<br>Right now, I worry about what other people think of me.<br>**Scale:**<br>1: Not at All;<br>2: A Little Bit;<br>3: Somewhat;<br>4: Very Much;<br>5: Extremely |
| `sse3_pleased_with_appearance` | **SSE3 - Pleased with Appearance**<br>Right now, I am pleased with my appearance.<br>**Scale:**<br>1: Not at All;<br>2: A Little Bit;<br>3: Somewhat;<br>4: Very Much;<br>5: Extremely |
| `sse3_feel_as_smart_as_others` | **SSE3 - Feel as Smart as Others**<br>Right now, I feel as smart as others.<br>**Scale:**<br>1: Not at All;<br>2: A Little Bit;<br>3: Somewhat;<br>4: Very Much;<br>5: Extremely |
| `sse3_overall_self_feelings` | **SSE3 - Overall Self Feelings**<br>Right now, overall, I feel good about myself.<br>**Scale:**<br>1: Not at All;<br>2: A Little Bit;<br>3: Somewhat;<br>4: Very Much;<br>5: Extremely |
| `sse3_response_time_mean_sec` | **SSE3 - Mean Response Time (sec)**<br>Mean time spent on self-esteem EMAs (in seconds).                                                                                                                                                    |
| `sse3_response_time_median_sec` | **SSE3 - Median Response Time (sec)**<br>Median time spent on self-esteem EMAs (in seconds).                                                                                                                                              |
| `current_stress_level`      | **Current Stress Level**<br>Are you feeling stressed now?<br>**Scale:**<br>1: Not at All;<br>2: A Little Bit;<br>3: Somewhat;<br>4: Very Much;<br>5: Extremely |
| `average_ema_time_sec`      | **Average EMA Time (sec)**<br>Average time spent on the EMA (in seconds).                                                                                                                                                                        |

### General EMA Dataset (`general_ema.csv`)

The `general_ema.csv` file contains survey responses assessing various aspects of participants' emotional states, self-esteem, stress levels, and time spent on Ecological Momentary Assessments (EMAs). Each row represents a unique user's responses on a specific date.

#### Variables

Below is a detailed description of each variable in the `general_ema.csv` dataset:

| **Variable**                | **Description**                                                                                                                                                                                                                                      |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                        | **Unique User ID**<br>A unique identifier assigned to each participant in the survey.                                                                                                                                                              |
| `date`                      | **Date**<br>Date of the survey response in the format `YYYYMMDD`. Example: `20240430` represents April 30, 2024.                                                                                                                                    |
| `photographic_affect_meter_score` | **Photographic Affect Meter Score**<br>Photographic Affect Meter scores. The user chooses an image from 16 pictures. Valence and arousal are calculated based on the rubric mentioned [here](https://dl.acm.org/doi/10.1145/1978942.1979047). Range: 1 to 16 |
| `phq4_feeling_nervous`      | **PHQ4 - Feeling Nervous**<br>Over the last 2 weeks, how often have you been bothered by feeling nervous, anxious, or on edge?<br>**Scale:**<br>0: Not at all;<br>1: Several days;<br>2: More than half the days;<br>3: Nearly every day |
| `phq4_worry_control`        | **PHQ4 - Worry Control**<br>Over the last 2 weeks, how often have you been bothered by not being able to stop or control worrying?<br>**Scale:**<br>0: Not at all;<br>1: Several days;<br>2: More than half the days;<br>3: Nearly every day |
| `phq4_feeling_depressed`    | **PHQ4 - Feeling Depressed**<br>Over the last 2 weeks, how often have you been bothered by feeling down, depressed, or hopeless?<br>**Scale:**<br>0: Not at all;<br>1: Several days;<br>2: More than half the days;<br>3: Nearly every day |
| `phq4_little_interest`      | **PHQ4 - Little Interest**<br>Over the last 2 weeks, how often have you been bothered by having little interest or pleasure in doing things?<br>**Scale:**<br>0: Not at all;<br>1: Several days;<br>2: More than half the days;<br>3: Nearly every day |
| `phq4_response_time_mean_sec` | **PHQ4 - Mean Response Time (sec)**<br>Mean time spent on PHQ4 EMAs (in seconds).                                                                                                                                                                |
| `phq4_response_time_median_sec` | **PHQ4 - Median Response Time (sec)**<br>Median time spent on PHQ4 EMAs (in seconds).                                                                                                                                                            |
| `phq4_total_score`          | **PHQ4 Total Score**<br>Aggregated PHQ4 Score (Sum of `phq4_feeling_nervous` to `phq4_little_interest`).                                                                                                                                       |
| `social_interaction_level`  | **Social Interaction Level**<br>Have you spent most of your time alone or with others today?<br>**Scale:**<br>1: Almost always alone;<br>2: Mostly alone, a little time with others;<br>3: Equal amounts of time alone and with others;<br>4: Mostly with others, a little time alone;<br>5: Almost always with others |
| `sse3_worry_about_others_think` | **SSE3 - Worry About Others' Thoughts**<br>Right now, I worry about what other people think of me.<br>**Scale:**<br>1: Not at All;<br>2: A Little Bit;<br>3: Somewhat;<br>4: Very Much;<br>5: Extremely |
| `sse3_pleased_with_appearance` | **SSE3 - Pleased with Appearance**<br>Right now, I am pleased with my appearance.<br>**Scale:**<br>1: Not at All;<br>2: A Little Bit;<br>3: Somewhat;<br>4: Very Much;<br>5: Extremely |
| `sse3_feel_as_smart_as_others` | **SSE3 - Feel as Smart as Others**<br>Right now, I feel as smart as others.<br>**Scale:**<br>1: Not at All;<br>2: A Little Bit;<br>3: Somewhat;<br>4: Very Much;<br>5: Extremely |
| `sse3_overall_self_feelings` | **SSE3 - Overall Self Feelings**<br>Right now, overall, I feel good about myself.<br>**Scale:**<br>1: Not at All;<br>2: A Little Bit;<br>3: Somewhat;<br>4: Very Much;<br>5: Extremely |
| `sse3_response_time_mean_sec` | **SSE3 - Mean Response Time (sec)**<br>Mean time spent on self-esteem EMAs (in seconds).                                                                                                                                                    |
| `sse3_response_time_median_sec` | **SSE3 - Median Response Time (sec)**<br>Median time spent on self-esteem EMAs (in seconds).                                                                                                                                              |
| `current_stress_level`      | **Current Stress Level**<br>Are you feeling stressed now?<br>**Scale:**<br>1: Not at All;<br>2: A Little Bit;<br>3: Somewhat;<br>4: Very Much;<br>5: Extremely |
| `average_ema_time_sec`      | **Average EMA Time (sec)**<br>Average time spent on the EMA (in seconds).                                                                                                                                                                        |

### Steps Dataset (`steps.csv`)

The `steps.csv` file contains step count data, providing information about users' physical activity throughout the day. Steps are aggregated by parts of the day as well as hourly.

#### Variables

Below is a detailed description of each variable in the `steps.csv` dataset:

| **Variable**        | **Description** |
|---------------------|-----------------|
| `id`                | **Unique User ID**<br>A unique identifier for each participant. |
| `date`              | **Date**<br>The date of the recorded steps, in the format `YYYYMMDD`. |
| `steps_full_day`    | **Full Day Steps**<br>Total number of steps recorded over the full day. |
| `steps_12am_9am`    | **Early Morning Steps**<br>Number of steps taken between 12 AM and 9 AM. |
| `steps_9am_6pm`     | **Daytime Steps**<br>Number of steps taken between 9 AM and 6 PM. |
| `steps_6pm_12am`    | **Evening Steps**<br>Number of steps taken between 6 PM and 12 AM. |
| `steps_hour_00`     | **Hourly Steps - 12 AM**<br>Number of steps taken between 12 AM and 1 AM. |
| `steps_hour_01`     | **Hourly Steps - 1 AM**<br>Number of steps taken between 1 AM and 2 AM. |
| `steps_hour_02`     | **Hourly Steps - 2 AM**<br>Number of steps taken between 2 AM and 3 AM. |
| `steps_hour_03`     | **Hourly Steps - 3 AM**<br>Number of steps taken between 3 AM and 4 AM. |
| `steps_hour_04`     | **Hourly Steps - 4 AM**<br>Number of steps taken between 4 AM and 5 AM. |
| `steps_hour_05`     | **Hourly Steps - 5 AM**<br>Number of steps taken between 5 AM and 6 AM. |
| `steps_hour_06`     | **Hourly Steps - 6 AM**<br>Number of steps taken between 6 AM and 7 AM. |
| `steps_hour_07`     | **Hourly Steps - 7 AM**<br>Number of steps taken between 7 AM and 8 AM. |
| `steps_hour_08`     | **Hourly Steps - 8 AM**<br>Number of steps taken between 8 AM and 9 AM. |
| `steps_hour_09`     | **Hourly Steps - 9 AM**<br>Number of steps taken between 9 AM and 10 AM. |
| `steps_hour_10`     | **Hourly Steps - 10 AM**<br>Number of steps taken between 10 AM and 11 AM. |
| `steps_hour_11`     | **Hourly Steps - 11 AM**<br>Number of steps taken between 11 AM and 12 PM. |
| `steps_hour_12`     | **Hourly Steps - 12 PM**<br>Number of steps taken between 12 PM and 1 PM. |
| `steps_hour_13`     | **Hourly Steps - 1 PM**<br>Number of steps taken between 1 PM and 2 PM. |
| `steps_hour_14`     | **Hourly Steps - 2 PM**<br>Number of steps taken between 2 PM and 3 PM. |
| `steps_hour_15`     | **Hourly Steps - 3 PM**<br>Number of steps taken between 3 PM and 4 PM. |
| `steps_hour_16`     | **Hourly Steps - 4 PM**<br>Number of steps taken between 4 PM and 5 PM. |
| `steps_hour_17`     | **Hourly Steps - 5 PM**<br>Number of steps taken between 5 PM and 6 PM. |
| `steps_hour_18`     | **Hourly Steps - 6 PM**<br>Number of steps taken between 6 PM and 7 PM. |
| `steps_hour_19`     | **Hourly Steps - 7 PM**<br>Number of steps taken between 7 PM and 8 PM. |
| `steps_hour_20`     | **Hourly Steps - 8 PM**<br>Number of steps taken between 8 PM and 9 PM. |
| `steps_hour_21`     | **Hourly Steps - 9 PM**<br>Number of steps taken between 9 PM and 10 PM. |
| `steps_hour_22`     | **Hourly Steps - 10 PM**<br>Number of steps taken between 10 PM and 11 PM. |
| `steps_hour_23`     | **Hourly Steps - 11 PM**<br>Number of steps taken between 11 PM and 12 AM. |

