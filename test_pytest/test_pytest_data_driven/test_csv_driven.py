import csv


# path = '../data/test_add.csv'
def test_get_csv_data():
    with open('../../data/test_add.csv') as file:
        raw = csv.reader(file)
        req_list = []
        for line in raw:
            req_list.append(line)
        print(req_list)
    return req_list

# if __name__ == '__main__':
#
#     print(get_csv_data("../data/test_add.csv"))



# class TestExcelDrivenDemo():
#     @pytest.mark.parametrize("x,y,req",get_csv_data("../data/test_add.csv"))
#     def test_my_add_by_excel(self,x,y,req):
#         assert my_add(x,y) == req
