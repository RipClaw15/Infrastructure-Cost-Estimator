from models import MotorwayProject, ExpresswayProject, Tunnel, Viaduct, Bridge, RoadNode, ParkingArea, RailwayStation, Location, RailwayProject

from data import DEX_OAR_SATU_MARE, FOCSANI_BRAILA_EXPRESSWAY, A3_NUSFALAU_POARTA_SALAJULUI, A1_MARGINA_HOLDEA, A7_PASCANI_ROSCANI, PROJECTS

import sys

PROJECT_CLASS_MAP = {
    "motorway" : MotorwayProject,
    "expressway" : ExpresswayProject,
    "railway" : RailwayProject,
}


# create the correct structure

def create_structure(structure_type, length_km, method=None):
    if structure_type == "bridge":
        return Bridge(length_km)
    if structure_type == "viaduct":
        return Viaduct(length_km)
    if structure_type == "tunnel":
        return Tunnel(length_km,method)
    raise ValueError("Unknown structure type")

# create the correct access point

def create_access_point(access_point_type, variant="simple", location=None):
    if access_point_type == "road_node":
        return RoadNode(variant, location)
    if access_point_type == "parking":
        return ParkingArea(variant, location)
    if access_point_type == "station":
        return RailwayStation(variant, location)

    raise ValueError("Unknown variant type")

# load the all the data for a specific project from data.py

def load_project_from_data(data):
    project_type = PROJECT_CLASS_MAP[data["project_type"]]

    project = project_type(
        name = data["name"],
        length_km=data["length_km"],
        year=data["year"],
        terrain=data["terrain"],
        start_location = Location(data["start_location"]),
        end_location = Location(data["end_location"])
        )

    for s in data["structures"]:
        for _ in range(s["count"]):
            project.add_structure(
                create_structure(
                    s["type"],
                    s["length"],
                    s.get("method")
                    )
            )
    for ap in data["access_points"]:
        project.add_access_point(
            create_access_point(
                ap["type"],
                ap["variant"],
                ap["location"]
                )
        )
    return project

# prints into the console the route and the detailed cost breakdowns

def print_project_details(project):
    print(project)

    project.show_route()
    project.cost_breakdown()

    print(f"Total estimated cost: {project.total_cost():,.0f} EUR\n")

def main():

    if len(sys.argv) < 2:
        print("Usage: python project.py <project_key")
        print("Available projects:")
        for key in PROJECTS:
            print(f"    - {key}")
        sys.exit(1)

    project_key = sys.argv[1]

    if project_key not in PROJECTS:
        print(f"Error: unkown project '{project_key}'")
        print("Available projects")
        for key in PROJECTS:
            print(f"    - {key}")
        sys.exit(1)

    project = PROJECTS[project_key]

    project1 = load_project_from_data(project)


    print_project_details(project1)

    # # project1.plot_project("focsani_braila.png")


    # project2 = load_project_from_data(FOCSANI_BRAILA_EXPRESSWAY, ExpresswayProject)

    # print_project_details(project2)

    # project3 = load_project_from_data(A1_MARGINA_HOLDEA, MotorwayProject)

    # print_project_details(project3)

    # project4 = load_project_from_data(A7_PASCANI_ROSCANI, MotorwayProject)

    # print_project_details(project4)

    # project5 = load_project_from_data(DEX_OAR_SATU_MARE, ExpresswayProject)

    # print_project_details(project5)


if __name__ == "__main__":
    main()
