class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        # -------- Plan ------#
        """
        1. Pick up first item
        2. Move right
        3. set light on
        4. while light on
            - set light off
            - while robot can move right
                - if item held is greater than item in front of robot:
                    - swap item
                    - move right
                    - set light on
                - otherwise, move right without swapping
            - Robot will eventually get to the far right side
            - begin comparisons while iterating left until you reach the 'none' spot (empty spot)
            - if the item held is greater than the item in front of the robot, 
                -swap
                -move left
                - turn light on
            - otherwise, move left without swapping
            - once you reach the empty spot AND you're not at the far right,
                - swap
                - move right
                - swap
                - move right
            - if light is still on, repeat from step 4
        5. swap with the empty spot in front of you

        Sorted
        """
        # -------- / Plan ------#
        # robot starts at position 0,
        # initial pickup and move to position 1, sets light on to trigger while loop
        self.swap_item()
        self.move_right()
        self.set_light_on()
        while self.light_is_on():
            # set light off to allow while loop to close when complete
            self.set_light_off()
            # while loop to catch when robot hits empty slot on the way back left
            while self.compare_item() is not None:
                #while loop to catch when robot has hit the far right spot
                while self.can_move_right():
                    # if item held is greater than item in spot, swap and move right, light on to stay in outer while loop
                    if self.compare_item() == 1:
                        self.swap_item()
                        self.move_right()
                        self.set_light_on()
                    # otherwise, move right without swapping. light is still off
                    else:
                        self.move_right()
                # while loop to move left until robot hits the empty spot
                while self.can_move_left() and self.compare_item() is not None:
                    # while iterating left, if item held is greater than item in current spot,
                    #  swap, move left, set light on
                    if self.compare_item() == 1:
                        self.swap_item()
                        self.move_left()
                        self.set_light_on()
                    # otherwise, move left without swapping
                    else:
                        self.move_left()
            # once the empty spot is reached, prior while loop is exited
            # if robot is not at the far right, swap with the empty spot, move right, pick up item, move right
            if self.can_move_right():
                self.swap_item()
                self.move_right()
                self.swap_item()
                self.move_right()
            # if the light is still on the list is not sorted yet and the loop will repeat
        # otherwise, you will be at the last empty spot and drop the item held
        self.swap_item()
        # list will be sorted
        return



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [10, 4, 3, 2, 5, 6]
    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)