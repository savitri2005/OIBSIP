# BMI Calculator

## Python Programming Internship - Task 2

## Project Overview

The BMI Calculator is a Python-based command-line application that calculates a user's Body Mass Index (BMI) using their weight and height.

The program calculates the BMI value, classifies the result into standard BMI categories, and provides a general health suggestion based on the category.

## Features

- Accepts user's name
- Accepts weight in kilograms
- Accepts height in meters
- Calculates BMI using the standard formula
- Displays BMI rounded to two decimal places
- Classifies BMI into four categories
- Displays the healthy BMI range
- Provides a general health suggestion
- Handles invalid numeric input
- Validates positive weight and height
- Allows multiple BMI calculations
- Provides a professional command-line interface

## BMI Formula

BMI is calculated using:

BMI = Weight / (Height × Height)

Where:

- Weight is measured in kilograms
- Height is measured in meters

## BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal |
| 25.0 - 29.9 | Overweight |
| 30.0 and above | Obese |

## Technologies Used

- Python
- Python input() function
- Basic arithmetic operations
- Conditional statements
- Functions
- Exception handling

## Project Structure

```text
Python-Task2-BMICalculator/
│
├── main.py
├── README.md
└── screenshots/
    ├── bmi_normal.png
    ├── bmi_categories.png
    └── bmi_validation.png