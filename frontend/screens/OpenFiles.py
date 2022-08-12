from easygui import fileopenbox


class OpenFiles:
    @staticmethod
    def open_file(message, multiple):
        list_files = []

        path_open = fileopenbox(title=message, multiple=multiple)

        if multiple:
            for n in range(len(path_open)):
                list_files.append(path_open[n])

            return list_files

        else:
            return path_open
