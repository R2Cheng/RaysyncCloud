import yaml

#提取data目录下参数
def get_data(file_name, funcname):
    with open("../data/data_%s.yml" % file_name, "r", encoding="utf8") as f:
        data = yaml.load(f)[funcname]

    data_list = list()
    for item in data.values():
        data_list.append(item)

    return data_list

if __name__ == '__main__':
    print(get_data("login","login_success"))