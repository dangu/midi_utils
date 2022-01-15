import mido

default_input = mido.open_input()
default_input.name

output = mido.open_output('SD-20 Part A')

for message in default_input:
    output.send(message)

get_input_names()
