def narayana(input_a: list):
    a = input_a.copy()
    k = 0
    l = 0
    a1 = [ind for ind in range(len(a)-1) if a[ind] < a[ind+1]]
    if a1:
        k = max(a1)
    else:
        return a
    l = max(ind for ind in range(len(a)) if a[k] < a[ind]) 
    a[k], a[l] = a[l], a[k]

    ans = a[:k+1]
    rev = list(reversed(a[k+1:]))
    ans.extend(rev)
    
    return ans

def narayana_permutations(n):
    a = list(range(1, n+1))
    prev = narayana(a)
    permutations = [a]
    curr = []
    if n != 1: permutations.append(prev) 

    while prev != curr:
        if len(curr) > 0:
            permutations.append(curr) 
            new_res = narayana(curr)
            prev = curr
        else: 
            new_res = narayana(prev)
        curr = new_res

    return permutations


# 1 3 7
# 1 7 3
# 7 1 3

def johnson_trotter_permutations(n):
    
    def get_largest_mobile(a, directions):
        max_mobile = None
        max_index = -1
        for i in range(len(a)):
            if directions[i] == 'left' and i>0 and a[i]>a[i-1]:
                if max_mobile is None or a[i] > max_mobile:
                    max_mobile, max_index = a[i], i
            elif directions[i] == 'right' and i<len(a)-1 and a[i]>a[i+1]:
                if max_mobile is None or a[i] > max_mobile:
                    max_mobile, max_index = a[i], i
        return max_index
     
    def swap(a, directions, i):
        if directions[i] == 'left':
            a[i], a[i-1] = a[i-1], a[i]
            directions[i], directions[i-1] = directions[i-1], directions[i] 
            return i - 1
        a[i], a[i+1] = a[i+1], a[i]
        directions[i], directions[i+1] = directions[i+1], directions[i] 
        return i + 1
    
    def flip_directions(a, directions, max_mobile):
        for i in range(len(a)):
            if a[i] > max_mobile:
                directions[i] = 'right' if directions[i] == 'left' else 'left'


    a = list(range(1, n+1))
    a.sort()
    directions = ['left'] * n
    permutations = [a.copy()]
    while True:
        max_index = get_largest_mobile(a, directions)
        if max_index == -1:
            break

        max_mobile = a[max_index]
        new_index = swap(a, directions, max_index)
        flip_directions(a, directions, max_mobile)

        permutations.append(a.copy())
    return permutations


def generate_inversion_vectors(n: int):
    '''
    Generate inversion vectors given the dimension
    Parameters:
        n (int): vector dimension
    
    Returns:
        inversion_vectors (list): list of generated inversion vectors
    '''
    # inversion_vectors = []

    def backtrack(current, index):
        if index == n:
            yield list(reversed(current[:]))
            return
        
        for value in range(index + 1):  # Values range from 0 to index
            current[index] = value
            yield from backtrack(current, index + 1)  # Recurse to the next index
    
    # Start with an empty inversion vector
    yield from backtrack([0] * n, 0)
    
    # return inversion_vectors

def generate_permutations(input_inv_vectors: list):
    '''
    Generates n! permutations from inversed vectors given

    Parameters:
        input_inv_vectors (list): inversed vectors

    Returns:
        permutations (list): permutations of initial [1, ... ,n] 
    '''
    # inv_vectors = input_inv_vectors[:]  # Copy the inversion vectors
    n = len(next(iter(input_inv_vectors)))  # Length of the vectors
    initial = list(range(1, n+1))  # Initial sequence [1, 2, ..., n]
    yield initial
    
    permutations = []

    for inv_vector in input_inv_vectors:
        new_vec = []  # Start with an empty permutation
        init = initial[:]  # Copy the initial numbers
        # inv_v = inv_vector[:]  # Copy the inversion vector to avoid modification

        # Process elements from right to left (highest to lowest index)
        for i in range(n-1, -1, -1):
            index = inv_vector[i]  # Get index from inversion vector
            new_vec.insert(index, init.pop())  # Insert element at the correct position
        
        yield new_vec
    
    return permutations    

def inversion_vectors_permutations(n: int) -> list:
    inv_vectors = generate_inversion_vectors(n=n)
    perms = generate_permutations(inv_vectors)
    
    return list(perms)


