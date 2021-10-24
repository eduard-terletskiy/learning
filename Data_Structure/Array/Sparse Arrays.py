# There is a collection of input strings and a collection of query strings. For
# each query string, determine how many times it occurs in the list of input
# strings. Return an array of the results.

# Example
# strings = ["ab", "ab", "abc"]
# queries = ["ab", "abc", "bc"]
# There are 2 instances of 'ab',1 of 'abc' and 0 of 'bc'. For each query, add
# an element to the return array,results = [2,1,0] .


strings = ["ab", "bc", "ab"]
queries = ["ab", "bc", "cb"]
list = []


def count():
    for x in queries:
        count_queries = strings.count(x)
        list.append(count_queries)
    return list


print(count())
