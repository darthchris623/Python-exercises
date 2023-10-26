def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE
    for num in nums:
        if num >= lowest and num <= highest:
            print(num)


in_range([10, 20, 30, 40, 50], 15, 30)         

# for num in range(9):
#     print(num + 1)

# for num in [1,2,3,4,5,6,7,8,9]:
#     print(num)