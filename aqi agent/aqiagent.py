import requests


class AQIAgent:

    def __init__(self, city):
        self.city = city.strip()
        self.api_key = "9dc6499a387416abd3f553a0833e61397c6f5bbf"

        # India AQI Breakpoints (Simplified)
        self.breakpoints = {
            "pm25": [
                (0, 30, 0, 50),
                (31, 60, 51, 100),
                (61, 90, 101, 200),
                (91, 120, 201, 300),
                (121, 250, 301, 400),
                (251, 1000, 401, 500),
            ],
            "pm10": [
                (0, 50, 0, 50),
                (51, 100, 51, 100),
                (101, 250, 101, 200),
                (251, 350, 201, 300),
                (351, 430, 301, 400),
                (431, 1000, 401, 500),
            ],
            "no2": [
                (0, 40, 0, 50),
                (41, 80, 51, 100),
                (81, 180, 101, 200),
                (181, 280, 201, 300),
                (281, 400, 301, 400),
                (401, 1000, 401, 500),
            ]
        }

    # ==============================
    # SENSOR: Collect pollutant data
    # ==============================
    def get_sensor_data(self):

        url = f"https://api.waqi.info/feed/{self.city}/?token={self.api_key}"
        response = requests.get(url)
        data = response.json()

        if data["status"] != "ok":
            return None

        iaqi_data = data["data"]["iaqi"]

        pollutants = {}

        for key in self.breakpoints.keys():
            if key in iaqi_data:
                pollutants[key] = iaqi_data[key]["v"]

        return pollutants

    # ==============================
    # AQI FORMULA
    # ==============================
    def calculate_sub_index(self, pollutant, concentration):

        for (C_low, C_high, I_low, I_high) in self.breakpoints[pollutant]:
            if C_low <= concentration <= C_high:
                return round(((I_high - I_low) / (C_high - C_low)) *
                             (concentration - C_low) + I_low)

        return None

    # ==============================
    # CATEGORY RULES
    # ==============================
    def determine_category(self, aqi):

        if aqi <= 50:
            return "Good"
        elif aqi <= 100:
            return "Satisfactory"
        elif aqi <= 200:
            return "Moderate"
        elif aqi <= 300:
            return "Poor"
        elif aqi <= 400:
            return "Very Poor"
        else:
            return "Severe"

    # ==============================
    # ACTUATOR
    # ==============================
    def act(self):

        print(f"\nFetching pollutant data for {self.city}...\n")

        sensor_data = self.get_sensor_data()

        if not sensor_data:
            print("Unable to retrieve pollutant data.")
            return

        sub_indices = {}

        for pollutant, value in sensor_data.items():
            sub_indices[pollutant] = self.calculate_sub_index(pollutant, value)

        overall_aqi = max(sub_indices.values())
        dominant = max(sub_indices, key=sub_indices.get)

        print("Pollutant Values:", sensor_data)
        print("Sub Indices:", sub_indices)
        print("Final AQI (Calculated by Code):", overall_aqi)
        print("Dominant Pollutant:", dominant)
        print("Category:", self.determine_category(overall_aqi))


# ==============================
# MAIN
# ==============================

city = input("Enter city name: ")
agent = AQIAgent(city)
agent.act()
