# Demystifying K-Nearest Neighbors (KNN)

## Overview
This project explores the fundamental concepts of the **K-Nearest Neighbors (KNN)** algorithm. KNN is a simple yet powerful "lazy learning" algorithm used in machine learning for both classification (sorting things into categories) and regression (predicting numbers).

The core philosophy of KNN is simple: **"Tell me who your friends are, and I will tell you who you are."** It assumes that similar data points exist in close proximity to each other.

---

## How It Works: The 4-Step Process

Regardless of the specific problem, KNN generally follows these four conceptual steps:

1.  **Plot the Data:** Imagine every item in your dataset is a point on a graph. The coordinates of these points are determined by their features (e.g., sweetness, size, height).
2.  **Measure Distance:** When a new, unknown item is introduced, the algorithm calculates the straight-line distance (Euclidean distance) between this new item and every other item in the dataset.
3.  **Find the "K" Neighbors:** The algorithm sorts the distances and picks the top **K** closest items. These are the "nearest neighbors."
4.  **Make a Decision:**
    * **For Classification:** The neighbors vote on what the new item is.
    * **For Regression:** The values of the neighbors are averaged to predict a number.

---

## Key Concepts Demonstrated

### 1. Classification: The "Majority Vote"
*Seen in: The Mystery Fruit Scenario*

In classification problems, we want to assign a label to a new item.
* **The Scenario:** We have apples and pears plotted based on **Sweetness** and **Crunchiness**.
* **The Logic:** If we have a mystery fruit, we look at its 3 closest neighbors ($k=3$). If the majority of those neighbors are Apples, we classify the mystery fruit as an **Apple**.
* **The Takeaway:** The algorithm uses the "mode" (most frequent item) of the neighbors to make a prediction.

### 2. Regression: The "Neighborhood Average"
*Seen in: House Price Prediction*

In regression problems, we want to predict a continuous specific number (like a price).
* **The Scenario:** We have a list of houses with data on **Square Footage** and **Number of Rooms**, along with their sale prices.
* **The Logic:** To estimate the price of a target house, we find the 4 most similar houses ($k=4$) based on size and room count. Instead of voting, we calculate the **average (mean)** price of those 4 neighbors.
* **The Takeaway:** We assume the target house has a value similar to the average of similar houses nearby in the dataset.

### 3. Data Normalization: Leveling the Playing Field
*Seen in: Shirt Size Recommendation*

Sometimes, data features have vastly different units or scales (e.g., Height in cm vs. Weight in kg).
* **The Problem:** A difference of 5cm in height might look like a "small" distance compared to a difference of 5kg in weight if the raw numbers aren't scaled. The feature with larger numbers will dominate the distance calculation, making the other feature irrelevant.
* **The Solution (Normalization):** We scale all data points to a range between 0 and 1.
    * Height becomes a percentage of the max height.
    * Weight becomes a percentage of the max weight.
* **The Takeaway:** Normalization ensures that every feature contributes equally to the distance calculation, leading to more accurate predictions (like recommending the correct shirt size: S, M, or L).

---

## Technical Glossary

* **Euclidean Distance:** The mathematical formula (derived from the Pythagorean theorem) used to measure the straight-line distance between two points in space.
* **K (Hyperparameter):** The number of neighbors we choose to look at.
    * Small **K** (e.g., 1) makes the model sensitive to noise/outliers.
    * Large **K** makes the boundaries smoother but might include irrelevant data points.
* **Features:** The specific attributes used to describe the data (e.g., Sweetness, Square Footage, Height).
