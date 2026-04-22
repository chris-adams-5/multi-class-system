from lib.tyre import Tyre
from datetime import datetime

"""
Initially tyre tread depth and pressure
Result = None
"""

def test_tyre_depth_pressure_initially_returns_none():
    tyre_1 = Tyre()
    result1 = tyre_1.tyre_info['tread_depth']
    assert result1 == None
    result2 = tyre_1.tyre_info['pressure']
    assert result2 == None
    result3 = tyre_1.tyre_info['date_recorded']
    assert result3 == None


"""
Initially tyre tread depth and pressure
Result = Add tread depth and pressure to Tyre instance 
"""

def test_add_tread_depth_and_pressure():
    tyre_1 = Tyre()
    tyre_1.record_tyre_data(12, 40, datetime(2026,3,27))
    result1 = tyre_1.tyre_info['tread_depth']
    assert result1 == 12
    result2 = tyre_1.tyre_info['pressure']
    assert result2 == 40
    result3 = tyre_1.tyre_info['date_recorded']
    assert result3 == datetime(2026,3,27)


"""
Adding another tyre pressure
"""

def test_add_mulitple():
    tyre_1 = Tyre()
    tyre_1.record_tyre_data(12, 40, datetime(2026,3,27))
    tyre_1.record_tyre_data(18, 35, datetime(2026,4,18))
    result1 = tyre_1.tyre_info['tread_depth']
    assert result1 == 18
    result2 = tyre_1.tyre_info['pressure']
    assert result2 == 35
    result3 = tyre_1.tyre_info['date_recorded']
    assert result3 == datetime(2026,4,18)
    

"""
Adding another tyre tread depth and pressure
Result = the history of the tyre
"""

def test_history_of_tyre_tread_depth_and_pressure():
    tyre_1 = Tyre()
    tyre_1.record_tyre_data(12, 40, datetime(2026,3,27))
    tyre_1.record_tyre_data(18, 35, datetime(2026,4,18))
    result = tyre_1.get_history()
    assert result == [
        {
            "tread_depth": 12,
            "pressure": 40,
            "date_recorded": datetime(2026,3,27)
        },
        {
            "tread_depth": 18,
            "pressure": 35,
            "date_recorded": datetime(2026,4,18)
        }
    ]
