array1 = []
x = 0
for i in range(5):
    question = 'how many copies of book '
    book = i+1
    print(question + str(book))
    x = (int(input()))
    array1.append(x)

check = any(j > 0 for j in array1)

total = 0.0
book_price = 8
while(check):     #"check" doesnt seem to be accurate after the first iteration
    array2 = []
    for n in range(len(array1)):
        if array1[n] < 1:
            None
        else:
            array2.append(1)
            array1[n] = array1[n] - 1

    if len(array2) == 1:
        total = total + len(array2)*book_price
    elif len(array2) == 2:
        total = total + ((len(array2)*book_price)-(len(array2)*book_price*.05))
    elif len(array2) == 3:
        total = total + ((len(array2)*book_price)-(len(array2)*book_price*.1))
    elif len(array2) == 4:
        total = total + ((len(array2)*book_price)-(len(array2)*book_price*.2))
    elif len(array2) == 5:
        total = total + ((len(array2)*book_price)-(len(array2)*book_price*.25))


print(total)



