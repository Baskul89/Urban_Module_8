first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)



def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding="utf-8") as file:
            for arg in data_set:
                file.write(str(arg) + "\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
