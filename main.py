import pathlib

download_dir = pathlib.Path('C:\\Users\\ch379\\Downloads')
file = 'dataset_198_3.txt'

with open(download_dir.joinpath(file), 'r') as f:
    input_text = f.read().splitlines()

from algorithms.stringReconstruction import construct_string

output = construct_string(input_text=input_text)

with open('output.txt', 'w') as f:
    f.write(output)
