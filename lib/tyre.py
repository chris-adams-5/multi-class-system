class Tyre():
    def __init__(self):
        self.tread_depth = None
        self.pressure = None
        self.date_recorded = None
        self.history = []

    def record_tyre_data(self, tread_depth, pressure, date_recorded):
        self.tread_depth = tread_depth
        self.pressure = pressure
        self.date_recorded = date_recorded

    def get_history(self):
        
        return self.history
