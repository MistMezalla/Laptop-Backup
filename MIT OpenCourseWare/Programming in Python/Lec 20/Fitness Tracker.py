from dateutil import parser
class Workout(object):
    cal_per_hr = 200

    def __init__(self, start, end, cal=None):
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.kind = 'Workout'
        self.cal = cal
        self.icon = '😥'

    # Getters
    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_kind(self):
        return self.kind

    def get_icon(self):
        return self.icon
    def get_calories(self):
        if (self.cal):
            return self.cal
        else:
            return (self.end - self.start).total_seconds() / 3600 * Workout.cal_per_hr

    # Setters
    def set_start(self, st):
        self.start = st

    def set_end(self, end):
        self.end = end

    def set_calories(self, cal):
        self.cal = cal

    def __str__(self):
        width = 25
        ret_str = f"|{'-'*width}|\n"
        ret_str += f"|{' '*width}|\n"
        ret_str += f"|{self.icon + (' ' * 4) + self.kind + ' ' * (width - 3 - 4 - len(str(self.kind)))}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|Duration:- {str(self.end - self.start) + ' ' * (width  - len('Duration:- ') - len(str(self.end - self.start)))}|\n"
        # ret_str += f"|Calories:- {self.get_calories()} cal{' ' * (width - len('Calories:- ') - len(' cal') - len(str(self.get_calories())))}|\n"
        ret_str += f"|Calories:- {self.get_calories():.2f} cal{' ' * (width - len('Calories:- ') - len(' cal') - len(f'{self.get_calories():.2f}'))}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|{'-' * width}|\n"

        return ret_str


class Jogging(Workout):
    cal_per_hr = 400
    cal_per_km = 60

    def __init__(self, start, end, cal=None, dist=0):
        super().__init__(start, end, cal)
        self.icon = '🏃'
        self.kind = 'Jogging'
        self.dist = dist

    def get_calories(self):
        if (self.cal):
            return self.cal
        elif (self.dist):
            return Jogging.cal_per_km * self.dist
        else:
            return Jogging.cal_per_hr * ((self.end - self.start).total_seconds() / 3600)

    def get_avg_speed(self):
        if (self.dist):
            return self.dist / ((self.end - self.start).total_seconds() / 3600)
        else:
            return self.get_calories() / Jogging.cal_per_km / ((self.end - self.start).total_seconds() / 3600)

    def get_dist(self):
        if(self.dist):
            return self.dist
        else:
            return Jogging.cal_per_hr * ((self.end - self.start).total_seconds() / 3600) / Jogging.cal_per_km

    def __str__(self):
        width = 25
        ret_str = f"|{'-' * width}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|{self.icon + (' ' * 4) + self.kind + ' ' * (width - 3 - 4 - len(str(self.kind)))}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|Duration:- {str(self.end - self.start) + ' ' * (width - len('Duration:- ') - len(str(self.end - self.start)))}|\n"
        ret_str += f"|Distance:- {self.get_dist():.2f} kms{' ' * (width - len('Distance:- ') - len(' kms') - len(f'{self.get_dist():.2f}'))}|\n"
        ret_str += f"|Avg Speed:- {self.get_avg_speed():.2f} km/hr{' ' * (width - len('Avg Speed:- ') - len(' km/hr') - len(f'{self.get_avg_speed():.2f}'))}|\n"
        # ret_str += f"|Calories:- {self.get_calories()} cal{' ' * (width - len('Calories:- ') - len(' cal') - len(str(self.get_calories())))}|\n"
        ret_str += f"|Calories:- {self.get_calories():.2f} cal{' ' * (width - len('Calories:- ') - len(' cal') - len(f'{self.get_calories():.2f}'))}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|{'-' * width}|\n"

        return ret_str

    def set_dist(self, dist):
        self.dist = dist


class Swimming(Workout):
    cal_per_hr = 500 # For freestyle

    def __init__(self, start, end, Type="Freestyle",cal=None):
        super().__init__(start, end, cal)
        self.icon = '🏊'
        self.kind = 'Swimming'
        self.type = Type

    def get_calories(self):
        if(self.cal):
            return self.cal
        elif(self.type == "Freestyle"):
            return Swimming.cal_per_hr * ((self.end - self.start).total_seconds() / 3600)
        else:
            if (self.type == 'Backstroke'):
                return 550 * ((self.end - self.start).total_seconds() / 3600)
            elif (self.type == 'Breaststroke'):
                return 750 * ((self.end - self.start).total_seconds() / 3600)
            elif (self.type == "Butterfly"):
                return 800 * ((self.end - self.start).total_seconds() / 3600)

    def set_type(self, type):
        self.type = type

    def __str__(self):
        width = 25
        ret_str = f"|{'-' * width}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|{self.icon + (' ' * 4) + self.kind + ' ' * (width - 3 - 4 - len(str(self.kind)))}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|Duration:- {str(self.end - self.start) + ' ' * (width - len('Duration:- ') - len(str(self.end - self.start)))}|\n"
        ret_str += f"|Type:- {self.type + ' ' * (width - len('Type:- ') -  len(f'{self.type}'))}|\n"
        # ret_str += f"|Calories:- {self.get_calories()} cal{' ' * (width - len('Calories:- ') - len(' cal') - len(str(self.get_calories())))}|\n"
        ret_str += f"|Calories:- {self.get_calories():.2f} cal{' ' * (width - len('Calories:- ') - len(' cal') - len(f'{self.get_calories():.2f}'))}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|{'-' * width}|\n"

        return ret_str


class Skipping(Workout):
    def __init__(self, start, end, pace='slow', cal=None):
        super().__init__(start, end, cal)
        self.icon = '🪢'
        self.kind = "Rope Skipping"
        self.pace = pace

    def get_calories(self):
        if(self.cal):
            return self.cal
        else:
            if(self.pace == 'slow'):
                return 500 * ((self.end - self.start).total_seconds() / 3600)
            elif(self.pace == 'moderate'):
                return 700 * ((self.end - self.start).total_seconds() / 3600)
            elif(self.pace == 'fast'):
                return 900 * ((self.end - self.start).total_seconds() / 3600)

    def set_pace(self, pace):
        self.pace = pace

    def __str__(self):
        width = 25
        ret_str = f"|{'-' * width}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|{self.icon + (' ' * 4) + self.kind + ' ' * (width - 3 - 4 - len(str(self.kind)))}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|Duration:- {str(self.end - self.start) + ' ' * (width - len('Duration:- ') - len(str(self.end - self.start)))}|\n"
        ret_str += f"|Pace:- {self.pace + ' ' * (width - len('Pace:- ') - len(f'{self.pace}'))}|\n"
        # ret_str += f"|Calories:- {self.get_calories()} cal{' ' * (width - len('Calories:- ') - len(' cal') - len(str(self.get_calories())))}|\n"
        ret_str += f"|Calories:- {self.get_calories():.2f} cal{' ' * (width - len('Calories:- ') - len(' cal') - len(f'{self.get_calories():.2f}'))}|\n"
        ret_str += f"|{' ' * width}|\n"
        ret_str += f"|{'-' * width}|\n"

        return ret_str


my_workout = Workout("19/05/24 at 18:00", "19/05/24 at 18:50")
print(my_workout)

my_jog = Jogging("19/05/24 at 18:00", "19/05/24 at 18:50")
print(my_jog)

my_swim = Swimming("19/05/24 at 18:00", "19/05/24 at 18:55","Breaststroke")
print(my_swim)

my_skip = Skipping("19/05/24 at 18:00", "19/05/24 at 18:20")
print(my_skip)

