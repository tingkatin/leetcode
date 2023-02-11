def removeElement(nums, val):
    length = len(nums)
    index = 0
    head = nums[index]

    while head is not None:
        if head is val:
            nums.pop(index)
            nums.append(None)
            length -= 1
            # Make the next head the same index
            head = nums[index]
        else:
            # Move the next head to the next index
            index += 1
            head = nums[index]

    print(nums)
    return length


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(removeElement(nums, 2))


if __name__ == "__main__":
    main()
