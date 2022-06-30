from concurrent.futures import thread
import sys
import csv
import os
from pathlib import Path
import tkinter

front_end = tkinter.Tk()

# Check if files exists, if not create them.S
header = ['Thread Color', 'ID', 'Number in Stock']

def check_file(file):
    file_exists = os.path.exists(file)
    print(file_exists)
    if file_exists == False:
        with open(file, 'w', encoding = 'UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)

check_file('files/janome.csv')
check_file('files/madeira.csv')
check_file('files/robinson-anton.csv')

def print_thread(file):
    with open(file, 'r') as read_obj:
                            csv_reader = csv.reader(read_obj)

                            for row in csv_reader:
                                row = ",".join(row)
                                print(row)


def add_thread(file):
    with open(file, 'a+', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        while (1):
            thread_color = input("Enter Color of Thread: ")
            thread_id = input("Enter Thread's Manufacturer ID: ")
            stock_num = int(input("Enter Number in Possession: "))
            while stock_num == 0 or stock_num < 0:
                print("Must have at least 1 in possession")
                stock_num = int(input("Enter Number in Possession: "))

            writer.writerow([thread_color, thread_id, stock_num])
            break




# Menu functions
def print_startup_menu():
    print("\nSewing Thread Organizer Menu")
    print("----------------------------")
    print("1.) Select Brand")
    print("2.) Show All Threads")
    print("0.) Exit\n")

def print_brand_menu():
    print("\nSelect Thread Brand")
    print("-------------------")
    print("1.) Janome")
    print("2.) Madeira")
    print("3.) Robinson-Anton")
    print("0.) Go Back")

def print_choice_brand():
    print("\nSelect Action")
    print("-------------")
    print("1.) Show Thread")
    print("2.) Add Thread")
    print("3.) Remove Thread")


def menu():
    while True:
        try:
            print_startup_menu()
            choice = input('Select Option: ').lower()[0]
            if choice == '1':
                print_brand_menu()
                choice = input('Select Option: ').lower()[0]
                try:
                    if choice == '1':
                        try:
                            print_choice_brand()
                            choice = input('Select Action: ').lower()[0]
                            if choice == '1':
                                print('\n')
                                print_thread('files/janome.csv')
                                print('\n')
                                input("Press any key to continue...")
                            elif choice == '2':
                                add_thread('files/janome.csv')
                            elif choice == '3':
                                '''REMOVE THREAD'''
                        except ValueError:
                            print(f'Not a valid selection')
                                                
                    
                    elif choice == '2':
                        try:
                            print_choice_brand()
                            choice = input('Select Action: ').lower()[0]
                            if choice == '1':
                                print('\n')
                                print_thread('files/madeira.csv')
                                print('\n')
                                input("Press any key to continue...")
                            elif choice == '2':
                                add_thread('files/madeira.csv')
                            elif choice == '3':
                                '''REMOVE THREAD'''
                        except ValueError:
                            print(f'Not a valid selection')


                    elif choice == '3':
                        try:
                            print_choice_brand()
                            choice = input('Select Action: ').lower()[0]
                            if choice == '1':
                                print('\n')
                                print_thread('files/robinson-anton.csv')
                                print('\n')
                                input("Press any key to continue...")
                            elif choice == '2':
                                add_thread('files/robinson-anton.csv')
                            elif choice == '3':
                                '''REMOVE THREAD'''
                        except ValueError:
                            print(f'Not a valid selection')
                            
                    elif choice == '0':
                        continue

                    elif choice < '0' or choice > '3':
                        raise ValueError

                except ValueError:
                    print(f'Not a valid selection')

            elif choice == '2':
                '''
                show all Thread
                '''
            elif choice == '0':
                return
            
            elif choice < '0' or choice > '2':
                raise ValueError

        except ValueError:
            print(f'Not a valid selection: Select 1, 2, 3, or 0')


def main():
    menu()



if __name__ == "__main__":
    main()