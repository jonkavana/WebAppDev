def reverse(str):
    if str == "" or len(str) == 1:
        return str
    else:
        return reverse(str[1:3]) + str[0]

print(reverse("johnka"))