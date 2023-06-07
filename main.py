import random
import time
import matplotlib.pyplot as plt

def input_file(count):
    with open("graph.txt", "w") as file:
        for i in range(count):
            a = random.randint(0, 20)
            b = random.randint(0, 20)
            str1 = str(a) + ' ' + str(b) + "\n"
            file.write(str1)

def read_file():
    with open("graph.txt", "r") as file:
        lines = file.readlines()

    graph = []
    for line in lines:
        x, y = map(int, line.strip().split())
        graph.append((x, y))
    return graph

def quick_sort(temp):
    if len(temp) <= 1:
        return temp

    pivot = temp[len(temp)//2]
    left = [x for x in temp if x < pivot]
    middle = [x for x in temp if x == pivot]
    right = [x for x in temp if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def vert_degree(graph_array):
    degrees = {}
    for edge in graph_array:
        for vertex in edge:
            if vertex not in degrees:
                degrees[vertex] = 1
            else:
                degrees[vertex] += 1
    return degrees


def programm():
    edges = read_file()
    degrees = vert_degree(edges)

    temp = [x for x in degrees.values()]
    sorted_degrees = quick_sort(temp)


    for item in set(sorted_degrees):
        for key, value in degrees.items():
            if item == value:
                print("Vertex:", key, "degree: ", item)



if __name__ == "__main__":
    programm()






