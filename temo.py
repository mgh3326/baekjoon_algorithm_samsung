def sockMerchant(n, ar):

    count = 0
    current_depth = 0
    for current_s in s:
        if current_s == "U":
            current_depth += 1
        else:
            current_depth -= 1
            if current_depth == -1:
                count += 1
    return count


print(
    countingValleys(8, "UDDDUDUU")
)
