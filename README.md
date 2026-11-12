# Lab Overview
This lab is about filter data form the dataset to show only the data that we want to know

## Project Structure

- `README.md` : This file
- `Cities.csv` : The dataset
- `data_processing.py` : The analysis code

## Design Overview

- `Cities.csv` : Dataset
- `data_processing.py` : Defines `DataLoader` class with attributes and methods for convert `Cities.cvs` to `cities`.`Table` class with attributes and methods for filter item, aggregate and get item

### DataLoader Class
#### Attributes 
`filepath` : File's name and location
#### Methods
`load()` : Load data into dictionary name `cities`

### Table Class
#### Attributes 
`data` : Data in `cities`
#### Methods
`filter_item(condition)` : Use condition to filter item in `data`
`aggregate(aggregation_key, aggregation_function)` : Get value form `aggregation_key`
`get_data()` : Return the Data

## How to running
To run the simulation, execute `data_processing.py`:

```bash
python data_processing.py