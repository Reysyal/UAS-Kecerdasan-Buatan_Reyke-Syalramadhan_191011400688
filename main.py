def calculate (x, y, z):
    return (x - z) / (x - y)

class Temperature:
    def get_freezing_value(temp):
        if temp <= 30:
            return 1
        elif temp > 30 and temp < 50:
            return calculate(50, 30, temp)
        return 0

    def get_cool_value(temp):
        if temp > 30 and temp < 50:
            return calculate(50, 30, temp)
        elif temp == 50:
            return 1
        elif temp > 50 and temp < 70:
            return calculate(70, 50, temp)
        elif temp > 70 and temp < 90:
            return calculate(90, 70, temp)
        return 0

    def get_warm_value(temp):
        if temp > 50 and temp < 70:
            return calculate(70, 50, temp)
        elif temp == 70:
            return 1
        elif temp > 70 and temp < 90:
            return calculate(70, 50, temp)
        return 0

    def get_hot_value(temp):
        if temp > 70 and temp < 90:
            return calculate(90, 70, temp)
        elif temp == 90:
            return 1
        return 0
        
class CloudCover:
    def get_sunny_value(cloud):
        if cloud <= 20:
            return 1
        elif cloud > 20 and cloud < 40:
            return calculate(40, 20, cloud)
        return 0

    def get_partly_cloud_value(cloud):
        if cloud > 20 and cloud < 50:
            return calculate(50, 20, cloud)
        elif cloud == 50:
            return 1
        elif cloud > 50 and cloud < 80:
            return calculate(80, 50, cloud)
        return 0

    def get_overcast_value(cloud):
        if cloud > 60 and cloud < 80:
            return calculate(80, 60, cloud)
        elif cloud >= 80:
            return 1
        return 0

class SystemInference:
    temp = 0
    cloud = 0

    def get_output(temp, cloud):
        return min(temp, cloud)

    def inference(self, temperature = Temperature(), cloud_cover = CloudCover()):
        res = []

        a1 = self.get_output(temperature.get_freezing_value(self.temp), cloud_cover.get_sunny_value(self.cloud));
        z1 = 25
        res.append((a1, z1));

        a2 = self.get_output(temperature.get_freezing_value(self.temp), cloud_cover.get_partly_cloud_value(self.cloud));
        z2 = 25
        res.append((a2, z2));

        a3 = self.get_output(temperature.get_freezing_value(self.temp), cloud_cover.get_overcast_value(self.cloud));
        z3 = 25
        res.append((a3, z3));

        a4 = self.get_output(temperature.get_cool_value(self.temp), cloud_cover.get_sunny_value(self.cloud));
        z4 = 25
        res.append((a4, z4));

        a5 = self.get_output(temperature.get_cool_value(self.temp), cloud_cover.get_partly_cloud_value(self.cloud));
        z5 = 25
        res.append((a5, z5));

        a6 = self.get_output(temperature.get_cool_value(self.temp), cloud_cover.get_overcast_value(self.cloud));
        z6 = 25
        res.append((a6, z6));

        a7 = self.get_output(temperature.get_warm_value(self.temp), cloud_cover.get_sunny_value(self.cloud));
        z7 = 75
        res.append((a7, z7));

        a8 = self.get_output(temperature.get_warm_value(self.temp), cloud_cover.get_partly_cloud_value(self.cloud));
        z8 = 75
        res.append((a8, z8));

        a9 = self.get_output(temperature.get_warm_value(self.temp), cloud_cover.get_overcast_value(self.cloud));
        z9 = 75
        res.append((a9, z9));

        a10 = self.get_output(temperature.get_hot_value(self.temp), cloud_cover.get_sunny_value(self.cloud));
        z10 = 75
        res.append((a10, z10));

        a11 = self.get_output(temperature.get_hot_value(self.temp), cloud_cover.get_partly_cloud_value(self.cloud));
        z11 = 75
        res.append((a11, z11));

        a12 = self.get_output(temperature.get_hot_value(self.temp), cloud_cover.get_overcast_value(self.cloud));
        z12 = 75
        res.append((a12, z12));

        return res;

    def defuzzification(self, data_inference):
        return sum(data[0] * data[1] for data in data_inference) / sum(data[0] for data in data_inference)