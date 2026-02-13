FOCSANI_BRAILA_EXPRESSWAY = {
    "name": "DEx6 Focsani-Braila",
    "length_km":73,
    "year":2026,
    "terrain":"plain",
    "start_location":"Focsani",
    "end_location":"Braila",
    "project_type":"expressway",

    "structures":[
        {"type":"bridge","length":0.03,"count":15},
        {"type":"bridge","length":0.06,"count":18},

        {"type":"viaduct","length":0.13,"count":4},
        {"type":"viaduct","length":0.26,"count":1},
        {"type":"viaduct","length":0.20,"count":1},
        {"type":"viaduct","length":0.44,"count":1},
        {"type":"viaduct","length":0.17,"count":2},
        {"type":"viaduct","length":0.63,"count":1},
    ],

    "access_points":[
        {"type":"road_node","variant":"trumpet", "location":"Focsani A7 Sud"},
        {"type":"road_node","variant":"diamond", "location":"Focsani DN23A Sud"},
        {"type":"parking","variant":"medium_duration", "location":"Hangulesti Sud"},
        {"type":"road_node","variant":"diamond", "location":"Maicanesti DN23"},
        {"type":"parking","variant":"medium_duration", "location":"Gurguieti Sud"},
        {"type":"road_node","variant":"diamond", "location":"Corbu Nou DN23"},
        {"type":"parking","variant":"medium_duration", "location":"Gulianca Sud"},
        {"type":"road_node","variant":"diamond", "location":"Silistea DJ221C"},
        {"type":"road_node","variant":"trumpet", "location":"Braila DEx Sud"},



    ]
}


A3_NUSFALAU_POARTA_SALAJULUI = {
    "name": "A3 Nusfalau–Poarta Salajului",
    "length_km": 41,
    "year": 2026,
    "terrain": "mountains",
    "start_location": "Nusfalau",
    "end_location": "Poarta Salajului",
    "project_type":"motorway",

    "structures": [
        {"type": "tunnel", "length": 2.9, "method": "natm", "count": 1},

        {"type": "viaduct", "length": 0.50, "count": 2},
        {"type": "viaduct", "length": 0.30, "count": 1},
        {"type": "viaduct", "length": 0.18, "count": 2},
        {"type": "viaduct", "length": 0.24, "count": 2},
        {"type": "viaduct", "length": 0.27, "count": 2},
        {"type": "viaduct", "length": 0.65, "count": 1},
        {"type": "viaduct", "length": 1.00, "count": 1},
        {"type": "viaduct", "length": 0.33, "count": 1},
        {"type": "viaduct", "length": 0.55, "count": 1},
        {"type": "viaduct", "length": 0.13, "count": 2},

        {"type": "bridge", "length": 0.10, "count": 1},
        {"type": "bridge", "length": 0.08, "count": 1},
        {"type": "bridge", "length": 0.06, "count": 1},
        {"type": "bridge", "length": 0.03, "count": 8},
    ],

    "access_points": [
        {"type": "road_node", "variant": "trumpet","location":"Zalau VO Sud"},
        {"type": "parking", "variant": "big_parking", "location":"Ciumarna"},
    ]
}


A1_MARGINA_HOLDEA = {
    "name": "A1 Margina–Holdea",
    "length_km": 10,
    "year": 2026,
    "terrain": "hilly",
    "start_location": "Margina",
    "end_location": "Holdea",
    "project_type":"motorway",

    "structures": [
        # Twin tunnels
        {"type": "tunnel", "length": 0.41, "method": "natm", "count": 1},
        {"type": "tunnel", "length": 1.98, "method": "cut_and_cover", "count": 1},

        # Viaducts
        {"type": "viaduct", "length": 0.36, "count": 1},
        {"type": "viaduct", "length": 1.1, "count": 1},
        {"type": "viaduct", "length": 0.16, "count": 1},

        # Smaller bridges
        {"type": "bridge", "length": 0.05, "count": 4},
    ],

    "access_points": [

    ]
}

A7_PASCANI_ROSCANI = {
    "name": "A7 Pascani–Roscani",
    "length_km": 33,
    "year": 2026,
    "terrain": "plain",
    "start_location": "Pascani",
    "end_location": "Roscani",
    "project_type":"motorway",

    "structures": [

        # Viaducts
        {"type": "viaduct", "length": 1.1, "count": 1},
        {"type": "viaduct", "length": 0.63, "count": 1},
        {"type": "viaduct", "length": 0.16, "count": 1},
        {"type": "viaduct", "length": 0.42, "count": 1},
        {"type": "viaduct", "length": 0.85, "count": 1},
        {"type": "viaduct", "length": 0.35, "count": 2},
        {"type": "viaduct", "length": 0.65, "count": 1},

        # Smaller bridges
        {"type": "bridge", "length": 0.05, "count": 9},
        {"type": "bridge", "length": 0.1, "count": 1},
        {"type": "bridge", "length": 0.03, "count": 10},

    ],

    "access_points": [
        {"type": "parking", "variant": "medium_duration", "location":"Contesti"},
        {"type":"road_node","variant":"diamond", "location":"Heci DJ208F"},
        {"type": "parking", "variant": "big_parking", "location":"Gulia"},
        {"type":"road_node","variant":"trumpet", "location":"Silistea Noua DJ208I"},
        {"type": "parking", "variant": "medium_duration", "location":"Tudora"},
    ]
}


DEX_OAR_SATU_MARE = {
    "name": "DEx Oar–Satu Mare",
    "length_km": 11.0,
    "year": 2026,
    "terrain": "plain",
    "start_location": "Oar (HU Border)",
    "end_location": "Satu Mare",
    "project_type":"expressway",

    "structures": [
        # Short bridges over canals / local roads
        {"type": "bridge", "length": 0.03, "count": 5},

    ],

    "access_points": [
        {"type": "road_node", "variant": "trumpet", "location": "Satu Mare DN19H"},
        {"type": "road_node", "variant": "diamond", "location": "Decebal DN19"},
        {"type": "parking", "variant": "big_parking", "location": "Satu Mare Vest"},
    ]
}


PROJECTS = {
    "focsani_braila" : FOCSANI_BRAILA_EXPRESSWAY,
    "a3_nusfalau_poarta" : A3_NUSFALAU_POARTA_SALAJULUI,
    "a1_margina_holdea" : A1_MARGINA_HOLDEA,
    "a7_pascani_roscani" : A7_PASCANI_ROSCANI,
    "dex_oar_satu_mare" : DEX_OAR_SATU_MARE,
}


