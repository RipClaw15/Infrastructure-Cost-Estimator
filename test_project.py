from project import create_structure, create_access_point, load_project_from_data

from models import MotorwayProject, ExpresswayProject, Tunnel, Viaduct, Bridge, RoadNode, ParkingArea, RailwayStation, Location, RailwayProject

from data import FOCSANI_BRAILA_EXPRESSWAY, A3_NUSFALAU_POARTA_SALAJULUI


def test_create_structure():
    structure1 = create_structure("viaduct", 1.2)
    assert structure1.length_km == 1.2
    assert isinstance(structure1, Viaduct)

    structure2 = create_structure("tunnel", 6, "tbm")
    assert structure2.method == "tbm"
    assert isinstance(structure2, Tunnel)

def test_create_access_point():
    access_point1 = create_access_point("road_node")
    assert access_point1.variant == "simple"
    assert isinstance(access_point1, RoadNode)

    access_point2 = create_access_point("road_node","turbion","Pascani")
    assert access_point2.variant == "turbion"
    assert access_point2.location == "Pascani"
    assert isinstance(access_point2, RoadNode)

def test_load_project_from_data():
    project1 = load_project_from_data(A3_NUSFALAU_POARTA_SALAJULUI, MotorwayProject)

    assert isinstance(project1, MotorwayProject)
    assert project1.length_km == 41
    assert project1.structure_count == 27
