from lib.tyre import Tyre

class Car():
    def __init__(self, *tyres):
        for tyre in tyres:
            if not isinstance(tyre, Tyre):
                raise Exception("Error! Tyre not found.")
        self.tyres = list(tyres)
        
    
    def get_details(self):
        list_of_strings = []
        i = 1
        for tyre in self.tyres:
            tyre_string = f"Tyre {i} is in position {i}, has a tread depth of {tyre.tyre_info["tread_depth"]} and tyre pressure of {tyre.tyre_info["pressure"]}, latest readings {tyre.tyre_info["date_recorded"].strftime("%-d/%-m/%y")}."
            list_of_strings.append(tyre_string)
            i += 1
        return " \n ".join(list_of_strings)
        
        
