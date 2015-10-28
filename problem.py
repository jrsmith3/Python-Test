# -*- coding: utf-8 -*-
"""
`main.py`: Solution to Idea Evolver's python challenge
======================================================

This file contains all of the code needed to address the python
challenge. All code is stored in this single file for the sake of
simplicity. The functions can be split into two categories: library
functions and  command-line interface functions. These categories are
noted in the source.

Usage
-----
From the command-line, execute `main.py` and follow the prompts.

```
$ python main.py
```


Tests
-----
Tests for the functions in this module can be found in the `test`
directory. Simply run `nosetests` from the root of the project repo.


License
-------
The MIT License (MIT)

Copyright (c) 2015 Joshua Ryan Smith

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
"""
# =====================
# Library functionality
# =====================
def unit_elements(matrix):
    """
    Return list of indices of unit elements of matrix

    Note that the order of the elements in the returned list 
    should be considered to be arbitrary.
    """
    unit_elems = []
    for row_indx, row in enumerate(matrix):
        for col_indx, elem in enumerate(row):
            if elem:
                unit_elems.append((row_indx, col_indx))

    return unit_elems


def neighbors(element, matrix):
    """
    Return list of given matrix element's neighbors

    This method gives a simple list of all the element's neighbors.
    It *does not* check the values of those neighbors, but it does
    account for the edge of the matrix.

    element : 2-tuple
        (row, column)
    """
    row_min = max(element[0] - 1, 0)
    row_max = min(element[0] + 2, len(matrix))

    col_min = max(element[1] - 1, 0)
    col_max = min(element[1] + 2, len(matrix[0]))

    row_indices = range(row_min, row_max)
    col_indices = range(col_min, col_max)

    nbors = [(row_index, col_index) for row_index in row_indices for col_index in col_indices]
    nbors.remove(element)

    return nbors


def unit_neighbors(element, matrix):
    """
    Return list of given matrix element's nonzero neighbors
    """
    nbors = neighbors(element, matrix)

    unit_nbors = [(row, col) for row, col in nbors if matrix[row][col]]

    return unit_nbors


def map_to_graph(matrix):
    """
    Map matrix data structure to dict representing graph
    """
    graph = {element: unit_neighbors(element, matrix) for element in unit_elements(matrix)}

    return graph


def find_areas(matrix):
    """
    Return a list of lists of points comprising an area
    """
    graph = map_to_graph(matrix)

    areas = []
    while graph:
        area = set()

        node, neighbor_nodes = graph.popitem()        
        area.add(node)

        while neighbor_nodes:
            next_neighbor_nodes = set()

            for neighbor_node in neighbor_nodes:
                nodes = graph.pop(neighbor_node)
                next_neighbor_nodes.update(nodes)

            area.update(neighbor_nodes)

            neighbor_nodes = next_neighbor_nodes.difference(area)

        areas.append(list(area))

    return areas


def max_area_size(matrix):
    """
    Return the area of maximum size
    """
    areas = find_areas(matrix)
    sizes = [len(area) for area in areas]
    return max(sizes)


# ==========================
# Command-line functionality
# ==========================
def cli():
    """
    Command-line interface
    """
    # print "Please input the matrix rows when prompted."
    # print "The elements of each row should be separated by whitespace"
    # print "and contain only 0 or 1.\n"

    num_rows = prompt_dimension_size("row")
    num_cols = prompt_dimension_size("column")
    matrix = prompt_matrix(num_rows, num_cols)

    return matrix


def prompt_dimension_size(dimension="row"):
    """
    Prompt for the size of matrix dimension and handle bad input

    dimension : str
        Dimension of matrix (either 'row' or 'column')
    """
    prompt = "Input number of {}s: "
    while 1:
        # raw_dim_size = raw_input(prompt.format(dimension))
        raw_dim_size = raw_input()
        try:
            dim_size = int(raw_dim_size)
        except:
            print "Please input integer value."
        else:
            break

    return dim_size


def prompt_row(num_row, num_cols):
    """
    Prompt for a matrix row and handle bad input

    num_row : int
        Index of current row (using python indexing convention)
    num_cols : int
        Number of columns in the matrix.
    """
    prompt = "Input matrix row {}: "
    while 1:
        # raw_row = raw_input(prompt.format(num_row + 1))
        raw_row = raw_input()
        try:
            row = rowify(raw_row, num_cols)
        except ValueError:
            print "Elements can only be 0 or 1; please retry."
        except IndexError:
            print "Please enter the proper number of columns."
        else:
            break

    return row


def rowify(raw_row, num_cols):
    """
    Convert user row input to actual row

    Arguments
    ---------
    raw_row : str
        Row taken from prompt
    num_cols : int
        Number of columns in matrix

    Returns
    -------
    row : list
    """
    strip_row = raw_row.strip()
    split_row = strip_row.split()
    # Attempt to convert everything to ints; will raise ValueError
    # otherwise and trigger re-prompt.
    ints_row = [int(element) for element in split_row]

    # Check if data is 0 or 1, raise ValueError if not and trigger
    # re-prompt.
    for element in ints_row:
        if element not in [0, 1]:
            raise ValueError("Matrix elements must be only 0 or 1.")

    if len(split_row) != num_cols:
        # Abuse of IndexError, but I don't want to write my own exception.
        raise IndexError()

    return ints_row


def prompt_matrix(num_rows, num_cols):
    """
    Prompt for the matrix and handle bad input

    num_rows : int
        Number of rows in matrix
    num_cols : int
        Number of columns in matrix
    """
    matrix = []
    for num_row in range(num_rows):
        row = prompt_row(num_row, num_cols)
        matrix.append(row)

    return matrix

if __name__ == "__main__":
    matrix = cli()
    print max_area_size(matrix)    
