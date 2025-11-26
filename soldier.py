from xmlrpc.client import Boolean


class Soldier:
    def __init__(self, personal_number: int, first_name: str, last_name: str, gender: str, city: str, distance: int, placement_status: bool=False ):
        self.personal_number = personal_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.distance = distance
        self.placement_status = placement_status
        