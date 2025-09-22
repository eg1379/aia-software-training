"""Modelling of the global fleet based on average passenger and aircraft data."""


def passengers_per_day(passengers_per_year, days_per_year):
    """The number of passengers per day globally.

    Args:
        passengers_per_year (float): The number of passengers flying per year globally.
        days_per_year (float): The number of days in the modelled year.
    """
    return passengers_per_year / days_per_year


def required_global_fleet(passengers_per_day, seats_per_aircraft, flights_per_aircraft_per_day):
    """The size of the required global fleet.

    Args:
        passengers_per_day (float): The number of passengers flying per day globally.
        seats_per_aircraft (float): The average number of seats on a commercial aircraft.
        flights_per_aircraft_per_day (float): The average number of flights a commercial aircraft makes on
            average per day.
    """
    return passengers_per_day / (seats_per_aircraft * flights_per_aircraft_per_day)
