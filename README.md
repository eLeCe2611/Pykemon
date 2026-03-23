# Pykemon: Data Analysis & Python Fundamentals 🐉🐍

This project was developed for the **Information Systems Fundamentals** course as part of the Computer Science Engineering degree. The primary goal is to demonstrate proficiency in Python for data processing, storage, and visualization using a real-world Pokémon dataset.

## 📊 About the Dataset
The project is based on the `15_pokemon.csv` file, which includes detailed statistics from the first 6 generations:
* **Identifiers**: ID, Name, and Types (Primary & Secondary).
* **Combat Stats**: HP, Attack, Defense, Sp. Atk, Sp. Def, and Speed.
* **Metadata**: Generation and Legendary status.

## 📁 Project Structure (P1 - P6)
Following academic requirements, the source code is organized into six packages within the `/Experimentos` directory. Each package addresses a specific stage of the data pipeline:

| Package | Description | Key Files |
| :--- | :--- | :--- |
| **P1** | Python fundamentals, logic gates, and basic structures. | `P1.py` |
| **P2** | Object-Oriented Programming (OOP) and data modeling. | `P2.py`, `P2_UML.png` |
| **P3** | Data persistence using **SQLite** and database management. | `P3.py`, `pokemon.db` |
| **P4** | Advanced data manipulation and business logic. | `P4.py` |
| **P5** | Exploratory Data Analysis (EDA) with **Pandas**. | `p5.ipynb` |
| **P6** | Data visualization with **Seaborn** and **Matplotlib**. | `P6.ipynb`, `*.png` |

---

## 📈 Insights & Visualizations
The **P6** module automates the generation of visual insights from the raw dataset. Some of the featured analyses include:

* **HP Distribution by Type**: A comparative study of base health across elemental types.
* **Type Correlations**: Analysis of the most common type combinations and their average stats.
* **Type Frequency**: Bar charts displaying type predominance across all 6 generations.

![Analysis Example](Experimentos/P6/tipo_x_hp_medio.png)

## 📝 Additional Documentation
* **Assignment**: The `Trabajo de Python.pdf` file contains the official guidelines and grading criteria.
* **Modeling**: The `P2` folder includes a UML diagram describing the class architecture used in the project.
* **Environment**: This repository includes **PyCharm** configuration files (folder `.idea`) to ensure technical consistency during review.
* **Examples**: An `Ejemplo` folder is provided with alternative datasets (e.g., `VinoBlanco.csv`) used during the initial testing phase.

## 👤 Author
* **Luis Carmona** - [@eLeCe2611](https://github.com/eLeCe2611)

---
*This project was created for academic purposes for the Computer Science Engineering Department.*
