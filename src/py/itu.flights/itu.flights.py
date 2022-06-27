from itu.algs4.searching.red_black_bst import RedBlackBST
from datetime import datetime, timedelta


class Flights:

    def __init__(self, n):
        self.n = n
        self.time_format = "%H:%M:%S"
        self.flights = self.getFlights()

    def strToTime(self, t):
        d = datetime.strptime(t, self.time_format)
        return d

    def timeToStr(self, t):
        s = t.strftime(self.time_format)
        return s

    def addSecondsToTime(self, t, seconds):

        # Built time delta object
        d = timedelta(seconds=seconds)

        # Increase the time
        new_time = t + d

        return new_time

    def getFlights(self):

        flights = RedBlackBST()

        for _ in range(self.n):

            # Get time and city
            t, city = input().split(" ")

            # Parse time into a datetime object which provides a better API to manage time
            t = self.strToTime(t)

            # Insert it to the symbol table
            flights.put(t, city)

        return flights

    def cancel(self, s):

        t = self.strToTime(s)
        self.flights.delete(t)

    def delay(self, s, d):

        # Get the destination of the flight to be delayed
        old_time = self.strToTime(s)
        destination = self.flights.get(old_time)

        # Delete the flight wild old time
        self.cancel(s)

        # Get updated time
        updated_time = self.addSecondsToTime(old_time, int(d))

        # Insert the new updated time
        self.flights.put(updated_time, destination)

    def reroute(self, s, c):

        t = self.strToTime(s)
        self.flights.put(t, c)

    def whichDestination(self, t):

        t = self.strToTime(t)
        destination = self.flights.get(t)
        if destination:
            return destination
        else:
            return "-"

    def nextDeparture(self, t):

        # Get the results
        t = self.strToTime(t)
        next_departure_time = self.flights.ceiling(t)
        destination = self.flights.get(next_departure_time)

        # Return the result in a proper format
        result = f"{self.timeToStr(next_departure_time)} {destination}"
        return result

    def countFlights(self, t1, t2):

        t1 = self.strToTime(t1)
        t2 = self.strToTime(t2)
        count = self.flights.size_range(t1, t2)
        return count


def main():

    # Read the first line (n - number of flights, m - number of operations)
    n, m = [int(value) for value in input().split(" ")]

    # Build the ST from the N flights
    flights = Flights(n)

    # Loop over the operations and make the appropriate action
    for _ in range(m):

        # Get the instructions
        instructions = input().split(" ")

        # Take the action based on the given instruction
        if instructions[0] == "cancel":
            s = instructions[1]
            flights.cancel(s)
        elif instructions[0] == "delay":
            s, d = instructions[1:]
            flights.delay(s, d)
        elif instructions[0] == "reroute":
            s, c = instructions[1:]
            flights.reroute(s, c)
        elif instructions[0] == "destination":
            t = instructions[1]
            print(flights.whichDestination(t))
        elif instructions[0] == "next":
            t = instructions[1]
            print(flights.nextDeparture(t))
        elif instructions[0] == "count":
            t1, t2 = instructions[1:]
            print(flights.countFlights(t1, t2))


if __name__ == "__main__":
    main()
