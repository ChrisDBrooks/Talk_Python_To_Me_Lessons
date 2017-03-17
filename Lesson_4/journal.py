import os

def load(name):
    # todo: populate from file if it exists
    return []


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('./journals/', name + '.txt'))
    print('Would save to {}'.format(filename))

    file_out = open(filename, 'w')

    # write entries to files
    for entry in journal_data:
        file_out.write((entry))

    file_out.close()

def add_entry(text, journal_data):
    journal_data.append(text)