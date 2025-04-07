sequence='ATGACGGAATATAAGCTAGGTGGTGGCTGGGCAGTCCGCGCTGATAGGGCAAGAGTGCGCGTACCATACCACGCTAAGCCATATAGGGCATCAGTCAGCCTGGCA'
pattern='AT'

#def pattern_search(sequence, pattern):

n = len(sequence)
m = len(pattern)
count = 0
position = set()
for index in range(n - (m - 1)):
    # if sequence[index : index + m] == pattern:
    #     print(index, sequence[index : index + m])
    is_same = True

    if sequence[index : index + n] == pattern:
        count += 1
    for index_pattern in range(m):
        print(sequence[index + index_pattern])
        if sequence[index + index_pattern] != pattern[index_pattern]:
            is_same = False

    if is_same:
        position.add(index)


    print(position)
    print(count)
    print(is_same)