from pydantic import BaseModel

class WeatherVariables(BaseModel):
                        temp_c: float 
                        humidity: float 
                        wind_speed_kmph: float 
                        wind_bearing_degree: float
                        visibility_km: float 
                        pressure_millibars: float 
                        current_weather_condition: float




                        