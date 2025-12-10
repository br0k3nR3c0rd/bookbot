def get_book_text(book):
    with open(book) as b:
        book_contents = b.read()
    print(f"Book successfully loaded from filepath: {book}")
    return (book_contents)

def get_word_count(book):
    print("----------- Word Count ----------")
    words = book.split()
    count = 0
    for w in words:
        count += 1
        
    print(f"Found {count} total words")

def get_character_total(text):
    print("--------- Character Count -------")
    lower_text = text.lower()
    totals = {}
    for ch in lower_text:
        if ch not in lower_text:
            return("No text given, returning")
        else:
            totals[ch] = totals.get(ch, 0) + 1
    return totals

def get_report(chars_dict):
    # Dict.sorted() method (iterable, key=?, reverse=True/False)
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    # Check to make sure the key is an alpha character
    for i in sorted_dict:
        # If it is: print it on the report
        if i.isalpha():
            print(f"{i}: {sorted_dict[i]}")