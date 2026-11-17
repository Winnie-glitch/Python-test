set1={1,2,3,4,5}
set2={3,4,5,6,7}
def common_numbers(set1:set, set2:set) ->set:
    return set1 & set2

print (common_numbers({1,2,3,4,5},{3,4,5,6,7}))

def multplication_table (n: int) -> None :
    for i in range(1,21):
        print(f"{n} x {i} = {n * i}")
multplication_table(5)