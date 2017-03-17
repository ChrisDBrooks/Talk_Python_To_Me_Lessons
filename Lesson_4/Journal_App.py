import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------------')
    print('   PERSONAL JOURNAL APP')
    print('----------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name) # x.load is a namespace

    while cmd != 'x':  # While the command from user isn't exit
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()  # This allows us to check against upper and lowercase entries and entries with spaces
        if cmd == 'l':
            list_enties(journal_data)  # We will need to work with the data here

        elif cmd == 'a':
            add_entry(journal_data)  # We will need to work with the data here

        elif cmd != 'x':
            print("Sorry we don't understand '{}'".format(cmd))

    print('Done, goodbye')
    journal.save(journal_name, journal_data)


def list_enties(data):
    print('Your Journal Entries (Most Recent First):')
    entries = reversed(data)
    for index, entry in enumerate(entries):  # enemurate(entries) provides a tuple (0, 'entry 3') and allows to get item and index of item
        print('> {}) {}'.format(index + 1, entry))  # + 1 gets rid of the list starting at 0


# is data the same as journal_entry yes because it is positional?
def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text)
    #data.append(text)


main()
