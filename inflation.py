INFLATION_RATES = {
    2024: 1.00,
    2025: 1.05,
    2026: 1.11
}

def adjust_for_inflation(cost, year) -> float:
    return cost * INFLATION_RATES.get(year, 1.0)

