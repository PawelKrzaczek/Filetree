import os


def print_decorline(chars, length, keep_whole=True):
    decorline = ""
    while True:
        decorline += chars
        if len(decorline) >= length:
            if keep_whole:
                decorline = decorline[1:length]
            break
    print(decorline)


def filetree(root, path="", exep=[".py"]):

    # Stop if this is not a folder:
    if not os.path.isdir(root):
        return

    # Get files in current folder:
    files = sorted(os.listdir(root))
    files_filtered = [item for item in files if (not item.startswith(".") and
                                                 not os.path.splitext(item)[1] in path)]
    nfiles = len(files_filtered)

    # Print the content of the current folder:
    newpath = path + "|   "
    arrow = "|-- "
    for i in range(nfiles):
        if i == nfiles - 1:
            newpath = path + "    "
            arrow = "`---- "
        print("{:s}{:s}{:s}".format(path, arrow, files_filtered[i]))
        # Recursive call to print the content of sub-folders:
        filetree("{:s}/{:s}".format(root, files_filtered[i-1]), newpath, exep)


def main():
    print("The contents of the current folder are:")
    print_decorline("*--*", 30)
    filetree(".")
    print_decorline("*--*", 30)


if __name__ == '__main__':
    main()
