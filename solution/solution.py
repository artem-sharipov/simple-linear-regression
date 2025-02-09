'''Module providing a plot functions'''
from matplotlib import pyplot as plt

DATA_FILEPATH = 'data/data023.txt'  # Fixed input data filepath.
CSV_DATA_FILEPATH = 'data/data023.csv'  # Fixed output .csv data filepath.
COMMENT_START_PATTERN = '(*'        # Comment lines in data file starts with this pattern.
# Position constants for parsing lines.
X_DATA_PART_POS = 0
Y_DATA_PART_POS = 1
VALUE_PART_POS = 1

def read_point_lines(data_filepath, skip_line_pattern):
    '''Read lines from filepath and return point lines and their number.'''
    point_lines = []
    points_number = 0

    with open(data_filepath, mode='r', encoding='utf-8') as file:
        for line in file:
            part = line.split()
            if part[0] == skip_line_pattern:
                continue # Skip comments in data file.
            point_lines.append(line)
            points_number += 1

    return point_lines, points_number

def process_point_lines(point_lines):
    '''Process point lines list to get returned two lists with X and Y coordinates.'''
    x_list = []
    y_list = []

    for line in point_lines:
        line_list = [unit.strip(' []\n')for unit in line.split('***')]
        x_list.append(float(line_list[X_DATA_PART_POS].split('=')[VALUE_PART_POS].strip()))
        y_list.append(float(line_list[Y_DATA_PART_POS].split('=')[VALUE_PART_POS].strip()))

    return zip(x_list, y_list)

def make_csv_data_file(data_filepath, coordinates_zip, points_number):
    '''Make data file with points coordinates and .csv extention'''
    x_list, y_list = zip(*coordinates_zip) # Unzip data.

    with open(data_filepath, mode='w', encoding='utf-8') as file:
        for i in range(points_number):
            file.write(f'{x_list[i]};{y_list[i]}\n')

def calc_slr_func_coefs(coordinates_zip, points_number):
    '''Calculate linear regression function and return a and b values.'''
    x_list, y_list = zip(*coordinates_zip) # Unzip data.
    xy_sum = 0
    xx_sum = 0

    # Preparatory calculations.
    x_sum = sum(x_list)
    y_sum = sum(y_list)
    for i in range(points_number):
        xy_sum += x_list[i]*y_list[i]
        xx_sum += x_list[i]**2

    # Main calculations.
    a = (x_sum*y_sum - points_number*xy_sum)/(x_sum**2 - points_number*xx_sum)
    b = (y_sum - a*x_sum)/points_number

    return a, b

def make_plot(data_filepath, coordinates_zip, lr_coefs):
    '''Make plot with data points and linear regression'''
    x_list, y_list = zip(*coordinates_zip) # Unzip data.
    a, b = lr_coefs
    lr_func = [(a*x + b) for x in x_list]
    legend = [f'{data_filepath}', f'y = {a:.3f}x + {b:.3f} (a = {a:.3f}, b = {b:.3f})']

    plt.figure(label='simple-linear-regression')
    plt.title('Data points and their linear regression')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(x_list, y_list, 'g.')
    plt.plot(x_list, lr_func, 'r')
    plt.grid(which='major')
    plt.grid(which='minor', alpha=0.2)
    plt.minorticks_on()
    plt.legend(legend)
    plt.show()

if __name__ == '__main__':
    points, n = read_point_lines(DATA_FILEPATH, COMMENT_START_PATTERN)
    make_csv_data_file(CSV_DATA_FILEPATH, process_point_lines(points), n)
    lr = calc_slr_func_coefs(process_point_lines(points), n)
    make_plot(DATA_FILEPATH, process_point_lines(points), lr)
