#!/usr/bin/env python3
# Created by: Melody Berhane
# Created on: Jan 26, 2022
# This program asks the user for the unit, length, height and
# width of the pyramid. It then
# calculates and displays the surface area and
# volume.
import math


# Function for area of a cylinder
def calc_area_cylinder(radius, height):
    area1 = 2 * math.pi
    area2 = radius * height
    area3 = area1 * area2
    area4 = 2 * math.pi
    area5 = radius**2
    area6 = area4 * area5
    area = area3 + area6
    return area


# Function for volume of a cylinder
def calc_vol_cylinder(radius, height):
    vol1 = radius**2
    vol = vol1 * math.pi * height
    return vol


# Function for area of a cone
def calc_area_cone(radius, height):
    area1 = math.sqrt((height**2)+(radius**2))
    area2 = radius + area1
    area = math.pi * radius * area2
    return area


# Function for volume of a cone
def calc_vol_cone(radius, height):
    vol1 = height/3
    vol = math.pi * (radius**2) * vol1
    return vol


def main():
    # input
    print("Welcome! Today we will be finding the surface area"
          "and volume of a cylinder and cone")
    print()
    while True:
        print("------------------------------------------------------"
              "--------------------------------------")
        unit = input("Enter the units: ")
        radius_user = input("Enter the radius: ")
        try:
            radius_user_float = float(radius_user)
            if radius_user_float <= 0:
                print("Please enter a number greater than 0!")
                print()
                print("Please enter a valid height")
                continue
            else:
                # gets second number from user
                height_user = input("Enter the height: ")
                try:
                    height_user_float = float(height_user)
                    if height_user_float <= 0:
                        print("Please enter a number greater than 0!")
                        print()
                        print("Please enter a valid height")
                        # goes back to the top of the while true loop
                        continue
                    else:
                        print()
                        question = input("Would you like to find the surface"
                                         " area and volume"
                                         "of a cylinder or cone?: ")
                        if question.upper() == "CONE":
                            cone_area_user = calc_area_cone(radius_user_float, height_user_float)
                            cone_vol_user = calc_vol_cone(radius_user_float, height_user_float)
                            print()
                            print("The surface of a cone is {:.2f} {}".
                                  format(cone_area_user, unit))
                            print("The volume of a cone is {:.2f} {}".
                                  format(cone_vol_user, unit))
                            print()
                            ask_again = input("Would you like to"
                                              " play again(y/n)?: ")
                            if ask_again.upper() == "YES" or ask_again.upper() == "Y":
                                # goes back to the top of the while true loop
                                continue
                            else:
                                print("Thank you for playing!")
                                # Ends the while true loop
                                break
                        else:
                            # assigns variable to function call that gives return value
                            cylinder_area_user = calc_area_cylinder(radius_user_float, height_user_float)
                            cylinder_vol_user = calc_vol_cylinder(radius_user_float, height_user_float)
                            # display results to user
                            print()
                            print("The surface area of a cylinder is {:.2f} {}".
                                  format(cylinder_area_user, unit))
                            print("The volume of a cylinder is {:.2f} {}".
                                  format(cylinder_vol_user, unit))
                            print()
                            ask_again = input("Would you like to"
                                              "play again(y/n)?: ")
                            if ask_again.upper() == "YES" or ask_again.upper() == "Y":
                                # goes back to the top of the while true loop
                                continue
                            else:
                                print("Thank you for playing!")
                                #Ends the while true loop.
                                break
                # catches any entered strings
                except Exception:
                    print("{} is not a valid number." .format(height_user))
                    print()
                    print("Please enter a valid height")
                    continue
        # catches any entered strings
        except Exception:
            print("{} is not a valid number." .format(radius_user))
            print()
            print("Please enter a valid radius")
            continue


if __name__ == "__main__":
    main()
