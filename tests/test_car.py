from datetime import datetime
import pytest
from lib.car import Car
from lib.tyre import Tyre

"""
Record of details of car tyres
Result is position of tyres
"""

def test_car_on_initialisation_takes_four_tyres():
    tyre_1 = Tyre()
    tyre_1.record_tyre_data(40, 14, datetime(2026,3,27))
    tyre_2 = Tyre()
    tyre_2.record_tyre_data(35, 18, datetime(2026,2,15))
    tyre_3 = Tyre()
    tyre_3.record_tyre_data(26, 17, datetime(2026,2,11))
    tyre_4 = Tyre()
    tyre_4.record_tyre_data(45, 10, datetime(2026,1,14))
    car = Car(tyre_1, tyre_2, tyre_3, tyre_4)
    assert car.tyres[0] is tyre_1
    assert car.tyres[1] is tyre_2
    assert car.tyres[2] is tyre_3
    assert car.tyres[3] is tyre_4

"""
Record of details of car tyres 
Raises error if not a tyre
"""

def test_car_raises_if_not_tyre():
    tyre_1 = Tyre()
    tyre_1.record_tyre_data(40, 14, datetime(2026,3,27))
    tyre_2 = Tyre()
    tyre_2.record_tyre_data(35, 18, datetime(2026,2,15))
    tyre_3 = Tyre()
    tyre_3.record_tyre_data(26, 17, datetime(2026,2,11))
    tyre_4 = "I am a tyre"
    with pytest.raises(Exception) as err:
        car = Car(tyre_1, tyre_2, tyre_3, tyre_4)
    assert str(err.value) == "Error! Tyre not found."


"""
Get car tyre details
Return a str of car tyre details
"""

def test_return_a_string_car_tyre_details():
    tyre_1 = Tyre()
    tyre_1.record_tyre_data(40, 14, datetime(2026,3,27))
    tyre_2 = Tyre()
    tyre_2.record_tyre_data(35, 18, datetime(2026,2,15))
    tyre_3 = Tyre()
    tyre_3.record_tyre_data(26, 17, datetime(2026,2,11))
    tyre_4 = Tyre()
    tyre_4.record_tyre_data(45, 10, datetime(2026,1,14))
    car = Car(tyre_1, tyre_2, tyre_3, tyre_4)
    result = car.get_details()
    assert result == "Tyre 1 is in position 1, has a tread depth of 40 and tyre pressure of 14, latest readings 27/3/26. \n Tyre 2 is in position 2, has a tread depth of 35 and tyre pressure of 18, latest readings 15/2/26. \n Tyre 3 is in position 3, has a tread depth of 26 and tyre pressure of 17, latest readings 11/2/26. \n Tyre 4 is in position 4, has a tread depth of 45 and tyre pressure of 10, latest readings 14/1/26."