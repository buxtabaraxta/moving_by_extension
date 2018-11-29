import os
import glob
import tqdm
from shutil import move


class MovingFiles:
    """Moves files from folder tree structure by their extension to one folder.
        src_dir - main directory where files and other inner folders are located.
        to_dir - folder where files will be moved.
        done.txt - file where stores information about moved files.
        """

    def __init__(self, src, dst, extension):
        self.src_dir = os.getcwd() + src
        self.dst_dir = dst
        self.extension = extension
        self.done = 'done.txt'

    def path_files(self):
        """Defined located path."""
        directorys_list = []
        for (p, d, f) in os.walk(self.src_dir):
            for i in glob.glob(p + '/*.' + self.extension):
                directorys_list.append(i)

        directorys_list.sort()
        return directorys_list

    def find_path_to_files(self):
        """Finds files in the folder tree, and write information in done.txt file
         as well as displays information in console.
         """
        f = open(self.dst_dir + '/' + self.done, 'a')
        for p in self.path_files():
            print(os.path.basename(p), '->', os.path.dirname(p), file=f, flush=True)
            print(os.path.basename(p), '->', os.path.dirname(p))
        f.close()

    def move_files(self):
        """Moves files, and creates done.txt file, which stored information about moved files."""
        done = open(self.dst_dir + '/' + self.done, 'a')
        files = self.path_files()
        # Progress bar
        progressbar = tqdm.trange(len(files))
        for bar in progressbar:
            try:
                for f in files:
                    move(f, self.dst_dir)
                    print(os.path.basename(f), '->', os.path.dirname(f), file=done, flush=True)
                    # print(os.path.basename(f), '->', os.path.dirname(f)) #Displayes information on console
            except:
                pass
        done.close()