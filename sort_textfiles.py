def sort_file_contents(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        lines = file.readlines()
    lines.sort()
    with open(output_filename, 'w') as file:
        file.writelines(lines)

sort_file_contents('input.txt', 'sorted_output.txt')
