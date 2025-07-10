import os


def get_path_depth(path):
    path = os.path.normpath(path)
    return len(path.split(os.sep))


# TODO: Place your code here
def generate_dir_report(path, report_file_path, show_files=True, num_files=False, file_size=False, hl=None):
    
    with open(report_file_path, 'w') as out:

        for root, dirs, files in sorted(os.walk(path)):

            files_out = ""
            if num_files: 
                files_num = len(files)
                files_out = " (" + str(files_num) + " files)"

            if root == path:
                out.write("+ " + os.path.basename(root) + files_out + "\n")
            else:
                out.write((get_path_depth(root) - 3) * "  " + "|-+ " + os.path.basename(root) + files_out + "\n")
            
            if show_files:
                for file in sorted(files):

                    file_size_out = ""
                    if file_size:
                        file_size_out = " (" + str(os.path.getsize(os.path.join(root, file))) + " bytes)"

                    highlight = ""
                    if hl is not None and file.endswith("." + hl):
                        highlight = " <--"

                    out.write((get_path_depth(root) - 2) * "  " + "|-- " + file + file_size_out + highlight + "\n")
                
    

if __name__ == '__main__':
    generate_dir_report('data/dir-top', 'dir-report.txt',
                        show_files=True,
                        num_files=True,
                        file_size=True,
                        hl='txt')
