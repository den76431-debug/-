# Исходные данные
DISKETTE_SIZE = 1.44
PAGES = 100
LINES = 50
CHARS_PER_LINE = 25
BYTES_PER_CHAR = 4

# Колво символов
total_chars = PAGES * LINES * CHARS_PER_LINE

# Размер книги в байтах:
book_size_bytes = total_chars * BYTES_PER_CHAR

# Объем дискеты в байтах
diskette_size_bytes = DISKETTE_SIZE * 1024 * 1024

# Колво книг на дискете
books_on_diskette = int(diskette_size_bytes // book_size_bytes)

# Вывод
print(f"Количество книг, помещающихся на дискету: {books_on_diskette}")
