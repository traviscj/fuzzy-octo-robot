#!/usr/bin/python
# created_at: 2017-12-04 08:07:08 -0800
# remove w/: rm $HOME/scratch/python/Scratch_IDeWEs.py

# assignments: students * 10 = 54*10
# books: 125

import random
from collections import Counter

def main():
    BOOKS = list(range(1, 125+1))
    STUDENTS = range(54)

    book_readings = Counter()
    for s in STUDENTS:
        sample = random.sample(BOOKS, 10)
        sample.sort()
        print("student: ", s, "books: ", sample)
        for book in sample:
            book_readings[book] += 1
    
    
    print(book_readings)
        

if __name__ == "__main__":
    print("book reports")
    main()
