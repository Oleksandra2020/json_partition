import json


def read_file(file):
    """
    () -> list
    Reads the given json file
    """
    with open(file) as f:
        return json.load(f)


def print_keys(dct):
    """
    dict -> list
    Prints the keys of the dict and returns the list of them
    """
    for key in dct:
        print(key, end='; ')


def is_dict(l):
    """
    str -> ()
    Prints the keys that are available to the user and
    navigates them through the file
    """
    verbose = True
    try:
        while verbose:
            if isinstance(l, dict):
                print('Keys available:', end=' ')
                print_keys(l.keys())
                print()
                user = input()
                l = l[user]
            elif isinstance(l[0], dict):
                print('Keys available:', end=' ')
                print_keys(l[0].keys())
                print()
                user = input()
                l = l[0][user]
            else:
                verbose = False
                print(l)
    except IndexError:
        print(l)
    except TypeError:
        print(l)


if __name__ == "__main__":
    file = read_file('results_trump.json')
    ids = file['users']
    length = len(ids)
    user_input = int(input("There are {} ids. Choose the number from 0 to {}: "
                           .format(length, length-1)))
    id = ids[user_input]
    len_id = len(id)
    print("There are {} keys available. Choose the key you want to see."
          .format(len_id))
    print_keys(id)
    print()
    user_input_key = input()
    l = id[user_input_key]
    is_dict(l)
