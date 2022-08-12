class Organize:
    @staticmethod
    def Organize(listreceive):
        string_list = " ".join(listreceive)
        string_list = string_list.replace("'", "").replace(",", "").replace("[", "").replace("]", "").replace("-", "")

        list_use = string_list.split(" ")

        list_final = [list_use[1], list_use[-5], list_use[-4], list_use[-3], list_use[-2], list_use[-1]]

        return list_final
