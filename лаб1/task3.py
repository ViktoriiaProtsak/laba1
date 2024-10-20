# TODO Найдите количество книг, которое можно разместить на дискете

v = 1.44
v_byte = v * 1024*1024

pages = 100
st = 50
sym = 25
book_byte = 4
v_book = pages*st*sym*book_byte
book = v_byte//v_book

print("Количество книг, помещающихся на дискету:", round(book))
