#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    school = {}
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            class_name = input("Введите класс ")
            pupils = int(input("Введите кол-во учащихся в данном классе "))
            school[class_name] = pupils

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} |'.format(
                    "No",
                    "Класс",
                    "Количество учеников",
                )
            )
            print(line)
            index = 0
            for class_name, pupils in school.items():
                index += 1
                print(
                    '| {:>4} | {:<30} | {:<20} |'.format(
                        index,
                        class_name,
                        pupils,
                    )
                )
            print(line)

        elif command == 'edit':
            class_name = input("Введите класс, в котором нужно внести "
                               "изменения ")
            pupils = input("Введите новое количество учащихся в классе "
                           f"{class_name} ")
            school[class_name] = pupils
            print("Количество учащихся было успешно изменено!")

        elif command == 'delete':
            class_name = input("Введите класс, который нужно расформировать ")
            del school[class_name]
            print("Класс был успешно расформирован")

        elif command == 'pupils':
            sum_of_pupils = 0
            for class_name in school:
                sum_of_pupils += int(school[class_name])
            print(f"Количество учеников в школе: {sum_of_pupils}")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить класс;")
            print("list - вывести список классов;")
            print("edit - изменить количество учащихся в заданном классе.")
            print("delete - расформировать класс.")
            print("pupils - вывести общее количество учеников во всех "
                  "классах.")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
