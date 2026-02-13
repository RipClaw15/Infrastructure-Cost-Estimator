from costs import STRUCTURE_COSTS_PER_KM, ROAD_BASE_COSTS_PER_KM, STRUCTURE_METHOD_MULTIPLIERS, ACCESS_POINT_BASE_COSTS, ACCESS_POINT_TYPE_MULTIPLIERS, TBM_FIXED_MOBILIZATION, TERRAIN_MULTIPLIERS, RAILWAY_BASE_COSTS_PER_KM

# import matplotlib.pyplot as plt


class Location:
    def __init__ (self, name, county = None, country="Romania", km = None):
        self.name = name
        self.country = country
        self.county = county
        self.km = km

    def __str__ (self):
        if self.km is not None:
            return f"{self.name} in {self.county} county, {self.country} ({self.km} km)"
        return f"{self.name} in {self.county} county, {self.country}"

class InfrastructureProject:
    def __init__ (self, name, length_km, year, terrain = None, start_location = None, end_location = None):
        self.name = name
        self.length_km = length_km
        self.year = year
        self.terrain = terrain
        self.start_location = start_location
        self.end_location = end_location
        self.structures = []
        self.access_points = []

    def add_structure(self, structure):
        self.structures.append(structure)

    def add_access_point(self, access_point):
        self.access_points.append(access_point)

    def base_cost(self):
        raise NotImplementedError("Subclasses must implement base_cost()")

    def cost_breakdown(self):
        raise NotImplementedError("Subclasses must implement cost_breakdown()")

    # method to calculate the cost of the infrastructure project
    def total_cost(self):
        cost = self.base_cost()
        # calculate the total structure and access point costs and add to the total cost
        cost += sum(s.cost() * s.span_cost(self) for s in self.structures)
        cost += sum(ap.cost() for ap in self.access_points)

        return cost

    @property
    def route(self):
        if self.start_location and self.end_location:
            return f"{self.start_location} to {self.end_location}"
        return "Unknown route"

    @property
    def structure_total_length_km(self):
        total_length_km = 0
        for s in self.structures:
            total_length_km += s.length_km
        return round (total_length_km, 2)

    @property
    def structure_count(self):
        return len(self.structures)

    @property
    def access_point_count(self):
        return len(self.access_points)

    @property
    def road_noad_count(self):
        count_node = 0
        for ap in self.access_points:
            if isinstance(ap, RoadNode):
                count_node += 1
        return count_node

    def show_route(self):
        print(self.start_location.name, "O", end="")
        for ap in self.access_points:
            print("---", end="")
            if isinstance(ap,RoadNode):
                print("X", end="")
            elif isinstance(ap,ParkingArea):
                print("▢", end="")
        print("---O", self.end_location.name)


    @property
    def length_km(self):
        return self._length_km

    @length_km.setter
    def length_km(self,value):
        if value <= 0:
            raise ValueError("Length must be positive")
        self._length_km = value

    # # visual representation of the project using the matplot library

    # def plot_project(self, filename="project_plot.png"):


    #     """
    #     Draw a simple liniar representation for the project
    #     """

    #     fig, ax = plt.subplots(figsize=(12,2))
    #     ax.set_title(f"{self.name} {self.year}")
    #     ax.set_xlim(0, self.length_km)
    #     ax.set_ylim(-1, 1)
    #     ax.set_yticks([])
    #     ax.set_xlabel("Project length (km)")

    #     # cumulative length for structures

    #     current_pos = 0

    #     # plot structures

    #     for s in self.structures:
    #         rect_color = "gray"
    #         if s.structure_type == "bridge":
    #             rect_color = "brown"
    #         elif s.structure_type == "tunnel":
    #             rect_color = "black"
    #         elif s.structure_type == "viaduct":
    #             rect_color = "orange"

    #         ax.barh(0, width=s.length_km, left=current_pos, height=0.6, color=rect_color, edgecolor = "k")
    #         current_pos += s.length_km

    #     step = self.length_km / (len(self.access_points) + 1) if self.access_points else 0
    #     pos = step
    #     # plot access points

    #     for ap in self.access_points:
    #         if isinstance(ap, RoadNode):
    #             ax.plot(pos, 0, marker = 'o', color = "blue", markersize=8)
    #         elif isinstance(ap, ParkingArea):
    #             ax.plot(pos, 0, marker = 's', color = "green", markersize=7)
    #         elif isinstance(ap, RailwayStation):
    #             ax.plot(pos, 0, marker = '^', color = "red", markersize=8)

    #         pos += step
    #     plt.tight_layout()
    #     plt.savefig(filename, dpi=150)
    #     plt.close()


    def __str__(self):
        return (
                f"This {self.name} project starts in the year of {self.year} in a {self.terrain} "
                f"has a length of {self.length_km} km, has {self.structure_count} structures,"
                f" with a total length of {self.structure_total_length_km} km and {self.road_noad_count} Nodes"
                )
class RoadProject(InfrastructureProject):

    DICT_KEY = "simple_road"

    def __init__ (self, name, length_km, year, terrain = None, lanes = 1, start_location = None, end_location = None):
        super().__init__(name, length_km, year, terrain, start_location, end_location)
        self.lanes = lanes

    def cost_breakdown(self):

        print("+---------------------------------------+")

        base_road_cost = self.base_cost()

        print(f"Base road work costs:{base_road_cost:,.0f} EUR")

        structure_cost = sum(s.cost()*s.span_cost(self) for s in self.structures)

        print(f"Structure work costs:{structure_cost:,.0f} EUR")

        access_point_cost = sum(ac.cost() for ac in self.access_points)

        print(f"Access point work costs:{access_point_cost:,.0f} EUR")

        print("+---------------------------------------+")




    def base_cost(self):

        base_per_km = ROAD_BASE_COSTS_PER_KM[self.DICT_KEY]

        multiplier = TERRAIN_MULTIPLIERS.get(self.terrain, 1.0)

        return base_per_km * multiplier * (self.length_km-self.structure_total_length_km)



class MotorwayProject(RoadProject):
    DICT_KEY = "motorway"

    DEFAULT_SPEED_LIMIT = 130
    DEFAULT_LANES = 2
    DEFAULT_EMERGENCY_LANE = True
    DEFAULT_IS_TOLL_ROAD = False

    def __init__ (self, name, length_km, year, terrain = None, lanes = None, start_location = None, end_location = None):
        if lanes == None:
            lanes = self.DEFAULT_LANES
        super().__init__(name, length_km, year, terrain, lanes, start_location, end_location)
        self.speed_limit = self.DEFAULT_SPEED_LIMIT
        self.emergency_lane = self.DEFAULT_EMERGENCY_LANE
        self.toll_road = self.DEFAULT_IS_TOLL_ROAD



class ExpresswayProject(RoadProject):
    DICT_KEY = "expressway"

    DEFAULT_SPEED_LIMIT = 120
    DEFAULT_LANES = 2
    DEFAULT_EMERGENCY_LANE = False
    DEFAULT_IS_TOLL_ROAD = False

    def __init__ (self, name, length_km, year, terrain = None, lanes = None, start_location = None, end_location = None):
        if lanes == None:
            lanes = self.DEFAULT_LANES
        super().__init__(name, length_km, year, terrain, lanes, start_location, end_location)
        self.speed_limit = self.DEFAULT_SPEED_LIMIT
        self.emergency_lane = self.DEFAULT_EMERGENCY_LANE
        self.toll_road = self.DEFAULT_IS_TOLL_ROAD


class RailwayProject(InfrastructureProject):

    DICT_KEY = "simple_track"

    DEFAULT_SPEED_LIMIT = 90
    DEFAULT_TRACKS = 1

    def __init__ (self, name, length_km, year, terrain = None, tracks = None, start_location = None, end_location = None):
        if tracks == None:
            tracks = self.DEFAULT_TRACKS
        super().__init__(name, length_km, year, terrain)

        self.speed_limit = self.DEFAULT_SPEED_LIMIT

    def cost_breakdown(self):

        print("+---------------------------------------+")

        base_railway_cost = self.base_cost()

        print(f"Base railway work costs:{base_railway_cost:,.0f} EUR")

        structure_cost = sum(s.cost() for s in self.structures)

        print(f"Structure work costs:{structure_cost:,.0f} EUR")

        access_point_cost = sum(ac.cost() for ac in self.access_points)

        print(f"Station point work costs:{access_point_cost:,.0f} EUR")

        print("+---------------------------------------+")




    def base_cost(self):

        base_per_km = RAILWAY_BASE_COSTS_PER_KM[self.DICT_KEY]

        multiplier = TERRAIN_MULTIPLIERS.get(self.terrain, 1.0)

        return base_per_km * multiplier * (self.length_km-self.structure_total_length_km)


class ElectrifiedRailwayProject(RailwayProject):

    DICT_KEY = "electrification"

    DEFAULT_SPEED_LIMIT = 160
    DEFAULT_TRACKS = 1

    def __init__ (self, name, length_km, year, terrain = None, tracks = None, start_location = None, end_location = None):

        super().__init__(name, length_km, year, terrain)

class HighSpeedRailLight(RailwayProject):

    DICT_KEY = "hsr_light"

    DEFAULT_SPEED_LIMIT = 220
    DEFAULT_TRACKS = 2

    def __init__ (self, name, length_km, year, terrain = None, tracks = None, start_location = None, end_location = None):

        super().__init__(name, length_km, year, terrain)

class HighSpeedRail(RailwayProject):

    DICT_KEY = "hsr"

    DEFAULT_SPEED_LIMIT = 260
    DEFAULT_TRACKS = 2

    def __init__ (self, name, length_km, year, terrain = None, tracks = None, start_location = None, end_location = None):

        super().__init__(name, length_km, year, terrain)

class BulletTrain(RailwayProject):

    DICT_KEY = "bullet"

    DEFAULT_SPEED_LIMIT = 320
    DEFAULT_TRACKS = 2

    def __init__ (self, name, length_km, year, terrain = None, tracks = None, start_location = None, end_location = None):

        super().__init__(name, length_km, year, terrain)

class Structure():
    def __init__ (self, length_km, structure_type, method = None):
        if length_km <= 0:
            raise ValueError("Length must be positive")

        self.length_km = length_km
        self.structure_type = structure_type
        self.method = method

    @property
    def length_km(self):
        return self._length_km

    @length_km.setter
    def length_km(self,value):
        if value <= 0:
            raise ValueError("Length must be positive")
        self._length_km = value

    # method to calculate span cost multiplier
    def span_cost(self, project):

        return 1

    # method to calculate the cost of a structure
    def cost(self):


        base = self.length_km * STRUCTURE_COSTS_PER_KM[self.structure_type]

        # if the structure has a method to construct we have to calculate the price based on a multiplier,
        # so we can get a more accurate pricing
        if self.method:
            base *= STRUCTURE_METHOD_MULTIPLIERS[self.structure_type][self.method]


        return base

class Viaduct(Structure):
    def __init__ (self, length_km):
        super().__init__(length_km, "viaduct")

    # method to calculate span cost multiplier
    def span_cost(self, project):

        if isinstance(project, (MotorwayProject, ExpresswayProject)):
            return 1.8
        return 1

class Tunnel(Structure):
    def __init__ (self, length_km, method="natm"):
        super().__init__(length_km, "tunnel", method)

    # method to calculate span cost multiplier
    def span_cost(self, project):

        if isinstance(project, (MotorwayProject, ExpresswayProject)):
            return 1.8
        return 1

    def cost(self):
        base = super().cost()

        if self.method =="tbm":
            base += TBM_FIXED_MOBILIZATION
        return base

class Bridge(Structure):
    def __init__ (self, length_km):
        super().__init__(length_km, "bridge")

    # method to calculate span cost multiplier
    def span_cost(self, project):

        if isinstance(project, (MotorwayProject, ExpresswayProject)) and self.length_km > 0.06:
            return 1.8
        return 1

class AccessPoint:
    def __init__ (self, ap_type, variant=None, location= None):
        self.ap_type = ap_type
        self.variant = variant
        self.location = location

    @property
    def show_location(self):
        return str(self.location) if self.location else "Unknown location"

    def cost(self):
        base = ACCESS_POINT_BASE_COSTS[self.ap_type]

        if self.variant:
            base *= ACCESS_POINT_TYPE_MULTIPLIERS[self.ap_type][self.variant]

        return base

class ParkingArea(AccessPoint):
    def __init__(self, parking_type="medium_duration", location=None):
        super().__init__("parking", parking_type, location)

class RoadNode(AccessPoint):
    def __init__(self, variant="simple", location=None):
        super().__init__("road_node", variant, location)


class RailwayStation(AccessPoint):
    def __init__(self, location=None):
        super().__init__("station",None, location)

