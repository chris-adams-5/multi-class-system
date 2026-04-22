class Tyre():
    def __init__(self):
    
        self.history = []
        self.tyre_info = {
            "tread_depth": None,
            "pressure": None,
            "date_recorded": None
        }
    def record_tyre_data(self, tread_depth, pressure, date_recorded):
        self.tyre_info = {
            "tread_depth": tread_depth,
            "pressure": pressure,
            "date_recorded": date_recorded
        }

        self.history.append(self.tyre_info)


    def get_history(self):
        return self.history
