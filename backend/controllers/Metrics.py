class Metrics:
    @staticmethod
    def Metrics(original, ocr):
        file1 = open(original, "r")
        file2 = open(ocr, "r")
        count1, i, j, k, l, size1, size2 = 0, 0, 0, 0, 0, 0, 0
        # LEITURA DOS ARQUIVOS
        content1 = file1.read()
        content1 = content1.replace("[", "").replace("]", "")
        list1 = content1.split("\n")
        while k < len(list1):
            size1 = len(list1[k]) + size1
            k += 1
        content2 = file2.read()
        content2 = content2.replace("[", "").replace("]", "")
        list2 = content2.split("\n")
        while l < len(list2):
            size2 = len(list2[l]) + size2
            l += 1
        # COMPARAÇÃO
        while i < len(list1):
            while j < len(list1[i]):
                try:
                    if list1[i][j] == list2[i][j]:
                        count1 += 1
                    else:
                        pass
                    j += 1
                except (Exception, ):
                    j += 1
            i += 1
            j = 0
        acuraccy = ((count1 / size1) * 100)
        if len(content2) > len(content1):
            size2 = size1
        precision = ((count1 / size2) * 100)
        return 'Accuracy: ' + str(acuraccy) + ' || Precision: ' + str(precision)
