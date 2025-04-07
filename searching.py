import os


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
    #file_path = os.path.join(cwd_path, file_name) #spoji dva kousky lomitkama
    import json

    with open(file_name) as f:
        data = json.load(f)
        if key in data:
            return data[key]
        else:
            return None

print(read_data(file_name='sequential.json', key='unordered_numbers'))

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
    return positions, len(positions)  # +1

print(linear_search(numbers=[5, 3, 5, 7, 1], searched_number=5))


def main():
    pass


if __name__ == '__main__':
    main()