#from Q1_heap import *
#from Q2_heap import *
from Q3_heap import *

def main(file_name):
    a_file = open(file_name)
    names, ratings = [], []
    next(a_file)
    name_score_dict ={}
    for line in a_file:
        temp = line.rstrip().split('; ')
        if len(temp) < 2:
            continue  # skip lines without at least two elements
        names.append(temp[0]) #key: name
        ratings.append(float(temp[1])) #name: rating
        name_score_dict[temp[0]] = float(temp[1])

    sorted_names = sort_movies_batch(names, ratings)
    sorted_names1 = sort_movies_incre(names, ratings)

    sorted, sorted1 = [], []
    for item in sorted_names:
        sorted.append(name_score_dict[item])
    for item in sorted_names1:
        sorted1.append(name_score_dict[item])
    sorted_true = [9.4, 9.3, 9.2, 9.1, 9.0, 9.0, 8.8, 8.8, 8.8, 8.8, 8.7, 8.7,
     8.6, 8.6, 8.5, 8.5, 8.4, 8.4, 8.4, 8.4, 8.4, 8.4, 8.3, 8.2, 8.1, 8.0, 7.8, 7.7, 7.7, 7.5, 7.5, 7.4, 7.4, 7.4, 7.4, 7.3, 7.3, 7.2, 7.2, 7.2, 7.1]
    if sorted == sorted_true and sorted1 == sorted_true:
        print("pass")

if __name__ == "__main__":
    main("movies1000.txt")  
    main("movies10000.txt")  
    main("movies100000.txt")  
