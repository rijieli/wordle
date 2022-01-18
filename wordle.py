from functools import reduce
import sqlite3
import random

conn = sqlite3.connect('wordle.db')
c = conn.cursor()
cursor = c.execute("SELECT word from entries")
samples = cursor.fetchall()
conn.close()

samples = filter(lambda w: len(set(w.lower())) == 5, map(lambda x: x[0], samples))
samples = list(samples)

def oneTrial():

    result = []
    result.append(random.choice(samples).lower())

    def noIntersec(w):
        for existWord in result:
            if len(set(existWord).intersection(set(w))) != 0:
                return False
        return True
    
    for _ in range(3):
        foundOne = False
        count = 0
        while not foundOne and count < 10000:
            count += 1
            wp = random.choice(samples).lower()
            if noIntersec(wp):
                result.append(wp)
                foundOne = True
    
    if len(result) > 3:
        return str(reduce(lambda x, y: x + "\t\t" + y, result)) + "\n"
    else:
        return ""

computedResult = ""
for i in range(1000):
    computedResult += oneTrial()

print(computedResult)