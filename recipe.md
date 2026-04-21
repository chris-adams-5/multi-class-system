## User Stories

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were

## Classes


Car
- position_one = tyre_1
- position_two = tyre_2
- position_three = tyre_3
- position_four = tyre_4

__init__(self, tyre1,tyre2 ....)

get_details() -> str 


Tyre
- tread_depth = integer
- pressure = integer
- date_recorded = date_recorded.now()

- history = [
    {
        tread_depth: int
        pressure: int
        date_recorded : date_recorded
    },
    {
        tread_depth: int,
        pressure,
        date_recorded
    }
]

def record_tyre_data(tread_depth, pressure):
    pass




```python
import dateti


tyre_1 = Tyre(pressure = 2, tread_depth = 20)
tyre_2 = Tyre(pressure = 3, tread_depth = 40)

tyre_2.tread_depth

car_1 = Car(position_1 = tyre_1, position_2 = tyre_2)


```