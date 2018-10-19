from data_structures.linked_list.linked_list import LinkedList


def main():
    linked_list_ = LinkedList()

    i = 0
    while i < 100:
        linked_list_.push_back(i)
        i += 1

    linked_list_.reverse()

    j = 0
    i = 99
    while i >= 0:
        assert j == linked_list_.value_at(i)
        i -= 1
        j += 1


if __name__ == '__main__':
    main()
