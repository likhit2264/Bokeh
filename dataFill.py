# This script is written for the purpose of organiing and creating an artificial database that can be referenced my the main script in its graphing endeavors.

# This class is created to set a format in which each fictional device will be constructed
class Device:
    def __init__ (self, id, color, age, script, weight, owner_age, percent, vibe, mode):
        # The different types of data for each ficitonal device are initialized here
        self.id = id
        self.color = color
        self.age = age
        self.script = script
        self.weight = weight
        self.owner_age = owner_age
        self.percent = percent
        self.vibe = vibe
        self.mode = mode

# Each of the devices is initialized with its own unique data, determined by random variables
id1 = Device('0000000000', 'black', 3, 'at auctor urna nunc id cursus metus aliquam eleifend mi', 8, 26, 99, 0, 1)
id2 = Device('0000000001', 'red', 4, 'integer sed ultrices sem vestibulum varius lectus non efficitur tincidunt', 8, 28, 97, 1, 2)
id3 = Device('0000000002', 'black', 6, 'nisl purus in mollis nunc sed id semper risus in', 12, 30, 96, 0, 3)
id4 = Device('0000000003', 'black', 4, 'nisi quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus', 8, 32, 95, 1, 1)
id5 = Device('0000000004', 'purple', 1, 'odio ut sem nulla pharetra diam sit amet nisl suscipit', 7, 34, 93, 0, 2)
id6 = Device('0000000005', 'maroon', 2, 'rhoncus mattis rhoncus urna neque viverra justo nec ultrices dui', 7, 36, 91, 1, 3)
id7 = Device('0000000006', 'black', 1, 'felis eget nunc lobortis mattis aliquam faucibus purus in massa', 7, 40, 87, 0, 1)
id8 = Device('0000000007', 'red', 1, 'nullam ac tortor vitae purus faucibus ornare suspendisse sed nisi', 7, 42, 86, 1, 2)
id9 = Device('0000000008', 'purple', 1, 'ivitae purus faucibus ornare suspendisse sed nisi lacus sed viverra', 44, 28, 85, 0, 3)
id10 = Device('0000000009', 'red', 2, 'tortor id aliquet lectus proin nibh nisl condimentum id venenatis', 7, 46, 83, 1, 1)
id11 = Device('0000000010', 'yellow', 1, 'mattis rhoncus urna neque viverra justo nec ultrices dui sapien', 7, 50, 81, 0, 2)
id12 = Device('0000000011', 'yellow', 10, 'eu augue ut lectus arcu bibendum at varius vel pharetra', 20, 79, 24, 0, 3)
id13 = Device('0000000012', 'black', 9, 'volutpat sed cras ornare arcu dui vivamus arcu felis bibendum', 16, 22, 78, 1, 1)
id14 = Device('0000000013', 'black', 7, 'nullam non nisi est sit amet facilisis magna etiam tempor', 12, 24, 77, 0, 3)
id15 = Device('0000000014', 'red', 2, 'in nisl nisi scelerisque eu ultrices vitae auctor eu augue', 7, 21, 76, 0, 2)
id16 = Device('0000000015', 'red', 6, 'sodales neque sodales ut etiam sit amet nisl purus in', 12, 20, 75, 0, 1)
id17 = Device('0000000016', 'purple', 13, 'eget nulla facilisi etiam dignissim diam quis enim lobortis scelerisque', 20, 19, 74, 0, 2)
id18 = Device('0000000017', 'black', 9, 'mi sit amet mauris commodo quis imperdiet massa tincidunt nunc', 16, 16, 73, 0, 3)
id19 = Device('0000000018', 'red', 3, 'laoreet suspendisse interdum consectetur libero id faucibus nisl tincidunt eget', 8, 18, 72, 0, 2)
id20 = Device('0000000019', 'red', 4, 'scelerisque felis imperdiet proin fermentum leo vel orci porta non', 8, 14, 71, 0, 1)
id21 = Device('0000000020', 'black', 1, 'volutpat blandit aliquam etiam erat velit scelerisque in dictum non', 7, 17, 70, 1, 2)
id22 = Device('0000000021', 'yellow', 1, 'integer sed ultrices sem vestibulum varius lectus non efficitur tincidunt', 7, 31, 69, 1, 3)
id23 = Device('0000000022', 'red', 1, 'mauris rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque', 7, 11, 67, 0, 2)
id24 = Device('0000000023', 'black', 4, 'integer sed ultrices sem vestibulum varius lectus non efficitur tincidunt', 8, 20, 65, 1, 1)
id25 = Device('0000000024', 'black', 6, 'sit amet tellus cras adipiscing enim eu turpis egestas pretium', 12, 19, 64, 0, 2)
id26 = Device('0000000025', 'yellow', 9, 'mauris rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque', 16, 62, 63, 1, 3)

# This is created to keep an organized list of each Object of the Device Class
Device_List = [id1, id2, id3, id4, id5, id6, id7, id8, id9, id10, id11, id12, id13, id14, id15, id16, id17, id18, id19, id20, id21, id22, id23, id24, id25, id26]
