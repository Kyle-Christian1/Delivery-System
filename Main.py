# Kyle Christian 000959459

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import datetime
from datetime import timedelta



address_data = []
distance_data = []
miles_traveled = 0


class Package:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline, weight, special_notes):
        # Initialize variables
        self.package_status = 'string'
        self.departure_time = ''
        self.departure_time2 = ''
        self.time_delivered = 'not delivered'
        self.is_loaded = False
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes


class Truck:
    def __init__(self):
        self.package_list = []

    def __int__(self, package_list):
        self.package_list = package_list

    miles_traveled = 0
    departure_time = ''



# HashTable class using chaining.  - Referenced from Webinars
# Time Complexity O(N)
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.

    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


# Loads each row of CSV file into a variable and adds that variable to the hashtable
# Time Complexity = O(n)
def loadPackageData(package_hashtable):
    with open('WGUPS Package File.csv', 'r') as csv_file:
        package_info = csv.reader(csv_file)
        for i in range(0, 8):
            next(package_info)
        for line in package_info:
            x = Package(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6], line[7])
            package_hashtable.insert(int(line[0]), x)


# Opens the CSV file and reads each row of data and stores them in a list
# Time Complexity = O(n)
def load_distance_data():
    with open('WGUPS Distance Table.csv', 'r') as csv_file:
        distance_info = csv.reader(csv_file)
        for i in range(0, 5):
            next(distance_info)

        for line in distance_info:
            '''x = Distance(line)
            x.list.remove(x.list[0])
            distance_data.append(x.list)'''
            x = line
            x.remove(x[0])
            x.remove(x[0])
            distance_data.append(x)
    #print(float(distance_data[1][1]))


# Opens CSV file and puts the address data into a list
# Time Complexity = O(n)
def load_address_data():
    with open('WGUPS Distance Table.csv', 'r') as csv_file:
        address_info = csv.reader(csv_file)
        # skip to data
        for i in range(0, 5):
            next(address_info)
        for line in address_info:
            address_data.append(line[1])

    # print(address_data)
    # return address_data[]


# This function fills the opposite side of the table so that [1,2] returns the same value as [2,1]
# Time Complexity = O(n^2)
def equalize_distance_data():
    for i in range(0, 27):
        for j in range(0, 27):
            distance_data[i][j] = distance_data[j][i]


# Returns distance between two addresses
# Time Complexity = O(1)
def distance_between(address1, address2):
    return float(distance_data[address1][address2])


# Loads Truck based on checks:
# Check 1: is the package already loaded? if not, check 2
# Check 2: has the truck reached its maximum package capacity? if not, check 3
# Check 3: is the delivery deadline 'EOD'? if not, check 4
# Check 4: is the package delayed because of the flight? if not, load package
# Time Complexity = O(n)
def load_truck_1(package_hash, truck):
    package_count = 0
    package_limit = 16
    for i in range(0, 40):
        if not package_hash.search(i+1).is_loaded:
            if package_count < package_limit:
                if package_hash.search(i+1).delivery_deadline != 'EOD' or package_hash.search(i+1).package_id == 19\
                        or package_hash.search(i+1).package_id == 6:
                    if package_hash.search(i+1).package_id != 25:
                        truck.package_list.append(package_hash.search(i+1))
                        package_hash.search(i+1).departure_time = truck.departure_time
                        package_hash.search(i+1).is_loaded = True
                        package_count += 1
        # print(package_count)
        # for package in truck.package_list:
            # print(package.package_id)

def reload_truck1(package_hash, truck, time):
    package_count = 0
    package_limit = 16
    for i in range(0, 40):
        #if not package_hash.search(i + 1).is_loaded:
        if package_count < package_limit:
            if package_hash.search(i+1).package_id == 6 or package_hash.search(i+1).package_id == 25:
                truck.package_list.append(package_hash.search(i+1))
                package_hash.search(i+1).departure_time = time
                package_hash.search(i+1).is_loaded = True
                package_count += 1


# Loads Truck based on checks:
# Check 1: is the package already loaded?
# Check 2: has the truck reached its maximum package capacity?
# Check 3: is it required the package be on this truck?
# Check 4: is the package delayed because of the flight?
# Time Complexity = O(n)
def load_truck_2(package_hash, truck):
    package_count = 0
    package_limit = 16
    for i in range(0, 40):
        if i != 9:
            if not package_hash.search(i+1).is_loaded:
                if package_count < package_limit:
                    if package_hash.search(i+1).special_notes == 'Can only be on truck 2':
                        truck.package_list.append(package_hash.search(i+1))
                        package_hash.search(i + 1).departure_time = truck.departure_time
                        package_hash.search(i+1).is_loaded = True
                        package_count += 1
                    if not package_hash.search(i+1).is_loaded and package_hash.search(i+1).special_notes != \
                            'Delayed on flight---will not arrive to depot until 9:05 am':
                        truck.package_list.append(package_hash.search(i+1))
                        package_hash.search(i + 1).departure_time = truck.departure_time
                        package_hash.search(i + 1).is_loaded = True
                        package_count += 1


# Loads the final truck with delayed and leftover packages
# Time Complexity = O(n)
def load_truck_3(package_hash, truck):
    for i in range(0, 40):
        if not package_hash.search(i+1).is_loaded:
            if package_hash.search(i+1).package_id != 25:
                truck.package_list.append(package_hash.search(i+1))
                package_hash.search(i + 1).is_loaded = True
                package_hash.search(i + 1).departure_time = truck.departure_time
    truck.package_list.append(package_hash.search(9))
    package_hash.search(9).departure_time = truck.departure_time


# KNN (K Nearest Neighbor Algorithm)
# Uses the nearest neighbor algorithm to deliver the packages
# Time Complexity = 0(n^2)
def deliver_packages(package_hashtable, truck):
    time = truck.departure_time
    current_address = 0
    removal_index = 0
    new_address = 0
    shortest_distance = 5000.0
    while truck.package_list:
        for package in truck.package_list:
            dist_between = float(distance_between(current_address, address_data.index(package.address)))
            if dist_between <= float(shortest_distance):
                shortest_distance = dist_between
                removal_index = truck.package_list.index(package)
                new_address = address_data.index(package.address)
        current_address = new_address
        #print('Current Address: ', address_data[current_address])
        removal_id = truck.package_list[removal_index].package_id
        package_hashtable.search(removal_id).package_status = 'Delivered'
        #print('Removing package with id: ', truck.package_list[removal_index].package_id, ' from truck')
        truck.package_list.remove(truck.package_list[removal_index])
        miles_to_minutes = shortest_distance * 60 / 18
        time += timedelta(minutes=miles_to_minutes)
        package_hashtable.search(removal_id).time_delivered = time
        #print('time = ', time)
        truck.miles_traveled += shortest_distance
        #print('current miles travelled: ', truck.miles_traveled)
        shortest_distance = 5000
    final_address = current_address
    truck.miles_traveled += float(distance_between(final_address, 0))
    '''test = timedelta(hours = (10), minutes = (25), seconds = (3))
    package_hashtable.search(25).time_delivered = test'''


# KNN (K Nearest Neighbor Algorithm)
# Uses the nearest neighbor algorithm to deliver the packages
# Time Complexity = 0(n^2)
def redeliver_packages(package_hashtable, truck, departure):
    time = departure
    current_address = 0
    removal_index = 0
    new_address = 0
    shortest_distance = 5000.0
    while truck.package_list:
        for package in truck.package_list:
            dist_between = float(distance_between(current_address, address_data.index(package.address)))
            if dist_between <= float(shortest_distance):
                shortest_distance = dist_between
                removal_index = truck.package_list.index(package)
                new_address = address_data.index(package.address)
        current_address = new_address
        #print('Current Address: ', address_data[current_address])
        removal_id = truck.package_list[removal_index].package_id
        package_hashtable.search(removal_id).package_status = 'Delivered'
        #print('Removing package with id: ', truck.package_list[removal_index].package_id, ' from truck')
        truck.package_list.remove(truck.package_list[removal_index])
        miles_to_minutes = shortest_distance * 60 / 18
        time += timedelta(minutes=miles_to_minutes)
        package_hashtable.search(removal_id).time_delivered = time
        #print('time = ', time)
        truck.miles_traveled += shortest_distance
        #print('current miles travelled: ', truck.miles_traveled)
        shortest_distance = 5000
    final_address = current_address
    truck.miles_traveled += float(distance_between(final_address, 0))
    '''test = timedelta(hours = (10), minutes = (25), seconds = (3))
    package_hashtable.search(25).time_delivered = test'''


# Returns the total miles traveled by all 3 trucks
# Time Complexity 0(1)
def total_miles_traveled(truck1, truck2, truck3):
    total_miles = truck1.miles_traveled + truck2.miles_traveled + truck3.miles_traveled
    return total_miles


# Checks specifically whether each package in the hash table has been delivered
# Time Complexity = O(n)
def loaded_package_check(package_hash):
    count = 0
    for i in range(0, 40):
        if package_hash.search(i+1).is_loaded:
            count += 1
        print(package_hash.search(i+1).package_id, package_hash.search(i+1).is_loaded)
    print('number of packages loaded: ', count)


# Checks current package status (ex. At Hub, Delivered, In-transit)
# Time Complexity = O(n)
def check_package_status(package_hash):
    count = 0
    for i in range(0, 40):
        if package_hash.search(i+1).package_status == 'Delivered':
            count += 1
        print(package_hash.search(i+1).package_id, ' Package Status: ', package_hash.search(i+1).package_status,
              ' Time Delivered: ', package_hash.search(i+1).time_delivered)
    print('number of packages delivered: ', count)


# Prints the packages that are on each truck
# Time Complexity = O(n)
def check_trucks(truck_1, truck_2, truck_3):
    for package in truck_1.package_list:
        print('Truck 1: ', package.package_id, ' ', 'address: ', package.address)
    for package in truck_2.package_list:
        print('Truck 2: ', package.package_id, ' ', 'address: ', package.address)
    for package in truck_3.package_list:
        print('Truck 3: ', package.package_id, ' ', 'address: ', package.address)


# Prints all the packages
# Time Complexity = 0(n)
def print_packages(package_hashtable):
    for i in range(0, 40):
        print('Package ID: ', package_hashtable.search(i + 1).package_id, ' Package Address: ',
              package_hashtable.search(i + 1).address, ' City: ', package_hashtable.search(i + 1).city,
              ' Zipcode: ', package_hashtable.search(i + 1).zipcode, ' Delivery Deadline: ',
              package_hashtable.search(i + 1).delivery_deadline, ' Special Instructions: ',
              package_hashtable.search(i + 1).special_notes)


# Takes input from the user in the form of 01:00:00 and prints out packages and their delivery status
# Based on the time the user input
# Time Complexity = O(n)
def status_by_time(package_hashtable, user_input_time):
    (h, m, s) = user_input_time.split(':')
    user_time = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    for i in range(0, 40):
        if user_time <= package_hashtable.search(i+1).departure_time:
            print('Package #', package_hashtable.search(i + 1).package_id, ' address: ',
                  package_hashtable.search(i + 1).address, ' city: ', package_hashtable.search(i + 1).city,
                  ' zipcode: ', package_hashtable.search(i + 1).zipcode, "\033[91m {}\033[00m" .format(' Delivery Status: At HUB '),
                  ' Delivery Deadline: ', package_hashtable.search(i + 1).delivery_deadline)
        if package_hashtable.search(i+1).time_delivered > user_time and user_time > package_hashtable.search(i+1).departure_time:
            print('Package #', package_hashtable.search(i+1).package_id, ' address: ',
                  package_hashtable.search(i+1).address, ' city: ', package_hashtable.search(i+1).city,
                  ' zipcode: ', package_hashtable.search(i+1).zipcode, "\033[93m {}\033[00m" .format(' Delivery Status: In Transit '),
                  ' Delivery Deadline: ', package_hashtable.search(i + 1).delivery_deadline)
        if package_hashtable.search(i+1).time_delivered <= user_time:
            print('Package #', package_hashtable.search(i+1).package_id, ' address: ',
                  package_hashtable.search(i+1).address, ' city: ', package_hashtable.search(i+1).city,
                  ' zipcode: ', package_hashtable.search(i+1).zipcode,
                  "\033[92m {}\033[00m" .format(' Delivery Status: Delivered '),
                  package_hashtable.search(i+1).time_delivered, ' Delivery Deadline: ', package_hashtable.search(i + 1).delivery_deadline)


# This function runs the actual program by calling the necessary functions to create the trucks
# Load the trucks and deliver what is inside the trucks
# Time Complexity: O(1)
def main(user_time, user_menu_choice):
    # create delivery times
    time_obj = datetime.timedelta(hours=int(8), minutes=int(0), seconds=int(0))
    time_obj2 = datetime.timedelta(hours=int(9), minutes=int(5), seconds=int(0))
    time_obj3 = datetime.timedelta(hours=int(11), minutes=int(16), seconds=int(0))
    time_obj4 = datetime.timedelta(hours=int(9), minutes=int(32), seconds=int(0))


    # create truck objects and set delivery times
    truck1 = Truck()
    truck1.departure_time = time_obj

    truck2 = Truck()
    truck2.departure_time = time_obj2

    truck3 = Truck()
    truck3.departure_time = time_obj3


    # create the chaining hash table and load the package data
    package_hashtable = ChainingHashTable()
    loadPackageData(package_hashtable)

    ''' The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20
    a.m. The correct address is “410 S State St., Salt Lake City, UT 84111”'''
    package_hashtable.search(9).address = '410 S State St'

    # load trucks
    load_truck_1(package_hashtable, truck1)
    load_truck_2(package_hashtable, truck2)
    load_truck_3(package_hashtable, truck3)

    # load and fill tables
    load_distance_data() # Load CSV file containing the distances
    load_address_data() # Load CSV file containing the addresses
    equalize_distance_data()  # Fill the other half of the table with equal values (ex. [4][2] = [2][4])
    '''for i in range(0, 40):
        print("Package #: {} and Address: {}".format(i+1, package_hashtable.search(i+1).address))'''

    # run KNN on each truck
    deliver_packages(package_hashtable, truck1) # deliver truck 1
    reload_truck1(package_hashtable, truck1, time_obj4)  # reload truck 1
    redeliver_packages(package_hashtable, truck1, time_obj4) # deliver truck 1

    deliver_packages(package_hashtable, truck2)
    deliver_packages(package_hashtable, truck3)

    if user_menu_choice == '1':
        print_packages(package_hashtable)

    if user_menu_choice == '2':
        # take user entered time and check package statuses
        status_by_time(package_hashtable, user_time)

    #check_package_status(package_hashtable)
    print('Total miles traveled: ', total_miles_traveled(truck1, truck2, truck3)) # Total mileage of all trucks

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
