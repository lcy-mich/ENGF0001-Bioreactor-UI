from settings import Stat

class DataParser:
    sim_statToName = {
            Stat.Acidity : "pH",
            Stat.Temperature : "temperature_C",
            Stat.Stirring : "rpm"
        }
    
    def __init__(self, is_simulated, data):
        self.raw_data = data
        self.is_simulated = is_simulated
    
    def get_setpoints(self):
        raw_setpoints = self.raw_data["setpoints"]
        ph = raw_setpoints["pH"]
        rpm = raw_setpoints["rpm"]
        temp = raw_setpoints["temperature_C"]

        return {Stat.Acidity : ph, Stat.Temperature : temp, Stat.Stirring : rpm}
    
    def get_stat_mean(self, stat):
        if not self.is_simulated: return

        stat_name = self.sim_statToName[stat]
        return self.raw_data[stat_name]["mean"]
    
    def get_start_time(self):
        return self.raw_data["window"]["start"]
    
    def get_end_time(self):
        return self.raw_data["window"]["end"]