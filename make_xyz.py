def rewrite(start, end, ind):
    """"Take start .xyz-file and end .xyz-file and index-correlation file to
        rearange end.xyz to match the indexing of start.xyz.

    Arguments:  [start] (string): Name of start .xyz-file
                [end] (string): Name of end .xyz-file
                [ind] (string): Name of index-correlation file

    Returns: Creates file new_[end.xyz] in current directory
            if it doesnt exist.

    Comments: Both .xyz-files should start with data in line 1 and
            have an empty line at the end. new_[end.xyz] can not exist,
            if it exists it will not be overwritten."""

    with open('{}'.format(start), 'r') as begin:
        with open('{}'.format(end), 'r') as stop:

            list_end = []

            for line in stop:
                list_end.append(line)

        list_of_lines = begin.readlines()

        with open('{}'.format(ind), 'r') as index:
            ref_index = []
            current_index = []

            for line in index:
                if line != '\n':
                    split = line.split()
                    ref_index.append(int(split[0]))
                    current_index.append(int(split[1]))

            for i in range(len(list_of_lines)):
                list_of_lines[ref_index[i]-1] = list_end[current_index[i]-1]

        with open('new_{}'.format(end), 'x') as new:
            new.writelines(list_of_lines)
    return


rewrite('{}'.format(input('Starting xyz: ')), '{}'.format(input('End xyz: ')),
        '{}'.format(input('Index-File: ')))
