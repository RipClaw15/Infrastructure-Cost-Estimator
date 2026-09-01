# INFRASTRUCTURE COST ESTIMATOR

A **Python based infrastructure cost estimator tool** built as a **CS50 Final Project**.
The program models and estimates construction costs about different road and railway projects using realistic engineering parameters and real Romanian case studies.

#### Video Demo: 

https://youtu.be/PqcufKvVMP0

## Project Overview

The calculator can estimate the total construction cost of large-scale infrastructure project such as:
- Motorways
- Expressways
- Different types of railwayprojects (ex. hsr)

Costs are calculated using:
- Project length
- Terrain type
- Structures (bridges, tunnels, viaducts)
- Access points (road nodes, parking areas, stations)
- Construction methods (ex. tunnel boring machine)
- Dual carriageway span logic (2 tubes of tunnel could mean almost double the cost)

The goal is not exact pricing (which let be honest is impossible cause of many different factors), but a realistic pricing method (based on the pricing it is in a **5-10% cost estimate margin**)

## Key Features

- **Object-oriented design**
    - Clear class hierarchy in models.py:
        - `Structures -> Tunnel`
        - `InfrastructureProject -> RoadProject -> ExpresswayProject`
        - `Location`
- **Realistic way to calculate price/cost**
    - Bridges, Viaducts, Tunnels (with construction methods)
    - Terrain difficulty multiplier (it requires more work (bigger costs) to make room for the road itself in a hilly/mountainous area (digging and filling up spaces) than on a flat surface)
    - Dual carriageway span cost logic (a motorway could have double tunnel tubes, or a 2 seperate viaduct structures/pillars next to each other)
- **Factory functions**
    - Faster and more dynamic object creation read from a file
- **Real Romanian project case studies**
    - A3 Nusfalau-Poarta Salajului motorway section
    - DEx6 Focsani-Braila expressway section
- **Detailed cost breakdown**
    - Base road works
    - Structure costs
    - Access point costs
- **ASCII route visualisation**
- **Fully testable with `pytest`**

## Example Project Output

This DEx6 Focsani-Braila project starts in the year of 2026 in a plain
has a length of 73 km, has 43 structures and 6 access points

Base road work costs: 746,064,000 EUR
Structure work costs: 92,736,000 EUR
Access point work costs: 145,000,000 EUR

Total estimated cost: 983,800,000 EUR

## Project Structure

```
final_project/
├── project.py
├── models.py
├── test_project.py
├── README.md
├── data.py
└── costs.py
---
```

## How to Run

In data.py, you can check for the available example projects to load, which you can add as a command-line argument after:

python project.py

## How to Test

Run all tests using:

pytest test_project.py

All tests pass without an error

## Design Choices

- Different files for:
    - models.py handles classes and behavior
    - costs.py handles cost configurations
    - data.py stores real project datas in dictionaries
- Factory functions simplify object creations from data.py
- Real-world pricing data is simplified but grounded in public contracts


