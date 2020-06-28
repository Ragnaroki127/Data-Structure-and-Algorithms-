# python3
import random

def integer_hash_function(x, a, b, p, m):
    return ((a * x + b) % p) % m

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
        

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    '''
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result
    '''
    result = []
    m = 10000
    n = 0
    p = 10002007

    a = random.randint(1, p - 1)
    b = random.randint(0, p - 1)

    contacts = [None] * m
    for cur_query in queries:
        if cur_query.type == 'add':
            ind = integer_hash_function(cur_query.number, a, b, p, m)
            if contacts[ind] == None:
                contacts[ind] = {cur_query.number:cur_query.name}
            else:
                contacts[ind][cur_query.number] = cur_query.name
            n += 1
        elif cur_query.type == 'del':
            ind = integer_hash_function(cur_query.number, a, b, p, m)
            if contacts[ind] == None or cur_query.number not in contacts[ind].keys():
                continue
            else:
                del contacts[ind][cur_query.number]
                n -= 1
        elif cur_query.type == 'find':
            response = 'not found'
            ind = integer_hash_function(cur_query.number, a, b, p, m)
            if contacts[ind] != None and cur_query.number in contacts[ind].keys():
                response = contacts[ind][cur_query.number]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

