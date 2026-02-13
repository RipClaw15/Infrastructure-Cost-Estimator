STRUCTURE_COSTS_PER_KM = {
    "tunnel": 60_000_000,
    "viaduct": 28_000_000,
    "bridge": 15_000_000,
}

ROAD_BASE_COSTS_PER_KM = {
    "motorway": 16_000_000,
    "expressway": 12_000_000,
    "simple_road": 4_000_000,
}

RAILWAY_BASE_COSTS_PER_KM = {
    "simple_track": 3_000_000,      # non-electrified
    "electrification": 6_000_000,   # 100-160 km/h
    "hsr_light": 12_000_000,        # 160-220 km/h
    "hsr": 22_000_000,              # 220-260 km/h
    "bullet": 32_000_000,           # 260-320 km/h
}

TERRAIN_MULTIPLIERS = {
    "plain": 0.90,
    "hilly": 1.25,
    "mountains": 1.6,

}

STRUCTURE_METHOD_MULTIPLIERS = {
    "tunnel": {
        "cut_and_cover": 0.5,
        "natm": 1.0,
        "tbm": 1.25
    }
}

ACCESS_POINT_BASE_COSTS = {
    "road_node": 20_000_000,
    "parking": 3_000_000,
    "station": 5_000_000,
}

ACCESS_POINT_TYPE_MULTIPLIERS = {
    "road_node": {
        "simple": 0.5,
        "diamond": 1.0,
        "trumpet": 1.4,
        "round_about": 1.6,
        "y_type": 2.0,
        "double_trumpet": 2.2,
        "cloverleaf": 3.0,
        "turbion": 4.0,
    },
    "parking": {
        "short_duration": 0.7,
        "medium_duration": 1.0,
        "big_parking": 1.3,
        "parking_fueling_type": 2.0,
    }
}


TBM_FIXED_MOBILIZATION = 45_000_000

