# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [None] * self.bucket_count

    def _hash_func(self, s):
        ans = 0
        for i in range(len(s)):
            ans += ord(s[i]) * self._multiplier ** i
        return (ans % self._prime) % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        '''
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)
        '''
        if query.type == 'check':
            if self.elems[query.ind] == None:
                print()
            else:
                self.write_chain(reversed(self.elems[query.ind]))
        else:
            if query.type == 'add':
                ind  = self._hash_func(query.s)
                if self.elems[ind] == None:
                    self.elems[ind] = [query.s]
                else:
                    if query.s in self.elems[ind]:
                        return
                    else:
                        self.elems[ind].append(query.s)
            elif query.type == 'del':
                ind = self._hash_func(query.s)
                if self.elems[ind] == None or query.s not in self.elems[ind]:
                    return
                else:
                    del self.elems[ind][self.elems[ind].index(query.s)]
            else:
                ind = self._hash_func(query.s)
                self.write_search_result(self.elems[ind] is not None and query.s in self.elems[ind])


    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
