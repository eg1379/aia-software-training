"""Modelling of the global fleet based on average passenger and aircraft data."""


def passengers_per_day(passengers_per_year, days_per_year):
    """The number of passengers per day globally.

    Args:
        passengers_per_year (float): The number of passengers flying per year globally.
        days_per_year (float): The number of days in the modelled year.
    """
    if not isinstance(passengers_per_year, float):
        message = (
            f"Argument `passengers_per_year` must be an instance of {str(float)}, instead got "
            f"{passengers_per_year}, which is a {type(passengers_per_year)}."
        )
        raise TypeError(message)
    if not isinstance(days_per_year, float):
        message = (
            f"Argument `days_per_year` must be an instance of {str(float)}, instead got "
            f"{days_per_year}, which is a {type(days_per_year)}."
        )
        raise TypeError(message)
    return passengers_per_year / days_per_year


def required_global_fleet(passengers_per_day, seats_per_aircraft, flights_per_aircraft_per_day):
    """The size of the required global fleet.

    Args:
        passengers_per_day (float): The number of passengers flying per day globally.
        seats_per_aircraft (float): The average number of seats on a commercial aircraft.
        flights_per_aircraft_per_day (float): The average number of flights a commercial aircraft makes on
            average per day.
    """
    if not isinstance(passengers_per_day, float):
        message = (
            f"Argument `passengers_per_day` must be an instance of {str(float)}, instead got "
            f"{passengers_per_day}, which is a {type(passengers_per_day)}."
        )
        raise TypeError(message)
    if not isinstance(seats_per_aircraft, float):
        message = (
            f"Argument `seats_per_aircraft` must be an instance of {str(float)}, instead got "
            f"{seats_per_aircraft}, which is a {type(seats_per_aircraft)}."
        )
        raise TypeError(message)
    if not isinstance(flights_per_aircraft_per_day, float):
        message = (
            f"Argument `flights_per_aircraft_per_day` must be an instance of {str(float)}, instead "
            f"got {flights_per_aircraft_per_day}, which is a {type(flights_per_aircraft_per_day)}."
        )
        raise TypeError(message)
    return passengers_per_day / (seats_per_aircraft * flights_per_aircraft_per_day)
