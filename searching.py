import os
import time
import matplotlib.pyplot as plt

# get current working directory path
        #chceme dostat cestu k aktualnimu pracovnimu adresari
cwd_path = os.getcwd()


def read_data(file_name, key):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    #sestavime uplnou cestu k souboru:
    file_path = os.path.join(cwd_path, file_name) #spoji dva kousky lomitkama
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if key in data:
            return data[key]
        else:
            return None


#print(read_data(file_name='sequential.json', key='unordered_numbers'))

# n = len(numbers)
def linear_search(numbers, searched_number):
    positions = []  # +1
    for index, number in enumerate(numbers):  # +n
        if number == searched_number:  # +n
            positions.append(index)  # +n
        else:
            continue
    # d["positions"] = list_idx
    # d["count"] = count
    return {
        "positions": positions,
        "count": len(positions)
    }# +1
#print(linear_search(numbers=[5, 3, 5, 7, 1], searched_number=5))


def binary_search(numbers, searched_number):
    """
        Binární vyhledávání. Půlí interval, dokud nenajde shodu.
        Složitost: O(log n) - extrémně rychlé i pro velké seznamy.
        POZOR: Vyžaduje seřazený seznam! - gemini
        """
    left = 0
    right = len(numbers) -1

    while left <= right:
        mid = (left + right) // 2
        mid_value = numbers[mid]

        if mid_value == searched_number:
            return mid  # cislo mame, vracime index
        elif mid_value < searched_number:
            left = mid + 1  # hladame na prave strane
        else:
            right = mid - 1  # hledame na leve strane

    return None  # kdyz cislo v seznamu neni





def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    target = 5
    result = linear_search(sequential_data, target)
    print(f"vysledky pro hledane cislo {target}:")
    print(f"pozice: {result['positions']}")
    print(f"cetnost: {result['count']}")

    cisla = read_data("sequential.json", "ordered_numbers")
    if cisla is not None: # pokud neni seznam prazdny
        target = 23 #zadefinuju target
        index = binary_search(cisla, target) # zadefinuju index a tam BS se seznamem cvisel a targetem
        if index is not None:
            print(f"cislo {target} nalezeno na indexu: {index}")
        else:
            print(f"císlo {target} se v seznamu nenachazi.")
    else:
        print("data se nepodarilo nacist.")

    sizes = [100, 500, 1000, 5000, 10000]
    linear_times = []
    binary_times = []
    target = 2000
    for size in sizes:
        data_unordered = unordered_sequence(max_len=size)
        data_ordered = sorted(data_unordered)

# NEJDE STAHNOUT matplotlib

if __name__ == '__main__':
    main()