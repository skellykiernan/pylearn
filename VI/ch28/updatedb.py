import shelve
with shelve.open('persondb') as db:
    for key in db.keys():
        print(key, ' ', db[key])

    sue = db['Sue Jones']
    sue.giveRaise(0.1)
    db['Sue Jones'] = sue
    db.close()
