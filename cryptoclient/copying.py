alphabet = "abcdefghiklmnopqrstuvwxyz"

#no j

# Initialize a 5 by 5 table of stars
table = []

def print_table():
    for row in range(5):
        for col in range(5):
            print(table[row][col],end="")
        print("")

def clear_table():
    global table
    table = []
    for row in range(5):
        table.append([])
        for col in range(5):
            table[row].append("*")

# This was added by
def find_letter(letter):
        for row in range(5):
            for col in range(5):
                if table[row][col] == letter:
                    return row, col
        return -1, -1

def table_has_letter(letter):
    return find_letter(letter)[0] != -1
    # Write code here to search the table for the given letter
    # and return True or False depending on if the letter exists

def table_next_opening():
    return find_letter("*")

def table_insert_letter(letter):
    letter=letter.upper()
    letter= "I" if letter == "J" else letter
    if letter in alphabet and not table_has_letter(letter):
        open_pos= table_next_opening()
        table[open_pos[0]][open_pos[1]] = letter
        ww = open_pos
        return (ww)

def create_table(secret):
    clear_table()
    for letter in secret:
        table_insert_letter(letter)
    for ex_letter in  alphabet:
        table_insert_letter(ex_letter)

create_table("Mathematics")
print_table()

print("")

create_table("Playfair example")
print_table()  # Should match wikipedia