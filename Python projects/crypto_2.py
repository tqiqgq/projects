# Введём данные, полученные от программы
S_blocks = ["3553600644227171", "7165470321654203", "3311331122002200"]
s_1 = [[int(p) for p in S_blocks[0][:8]], [int(p) for p in S_blocks[0][8:]]]

S_1 = [[3, 5, 5, 3, 6, 0, 0, 6], # my variant
        [4, 4, 2, 2, 7, 1, 7, 1]]

S_2 = [ [7, 1, 6, 5, 4, 7, 0, 3],
        [2, 1, 6, 5, 4, 2, 0, 3] ]

S_3 = [ [3, 1, 3, 1],
        [3, 1, 3, 1],
        [2, 0, 2, 0],
        [2, 0, 2, 0] ]
# Введём данные, полученные от программы

# S_1 = [ [6, 1, 3, 1, 4, 6, 4, 3],
#         [5, 2, 0, 7, 7, 5, 2, 0] ]
#
# S_2 = [ [1, 4, 0, 5, 1, 4, 0, 5],
#         [2, 7, 7, 6, 2, 3, 3, 6] ]
#
# S_3 = [ [0, 3, 3, 0],
#         [0, 3, 3, 0],
#         [2, 1, 1, 2],
#         [2, 1, 1, 2] ]
#
P = [ 8, 7, 3, 2, 5, 4, 1, 6 ]
# E_P = [ 5, 3, 1, 7, 4 ,2, 8, 6, 5, 1, 3, 4 ]
E_P = [ 2, 7, 4, 3, 5 ,8, 6, 1, 5, 1, 6, 2 ]
# S_1 = [[1, 1, 2, 2, 0, 0, 3, 3],
#        [6, 5, 5, 6, 4, 4, 7, 7]]
#
# S_2 = [[6, 5, 4, 7, 7, 4, 6, 5],
#        [1, 1, 0, 0, 3, 3, 2, 2]]
#
# S_3 = [[0, 0, 3, 3],
#        [0, 0, 3, 3],
#        [1, 1, 2, 2],
#        [1, 1, 2, 2]]
#
# P = [8, 7, 3, 2, 5, 4, 1, 6]
#
# E_P = [6, 5, 8, 2, 3, 4, 7, 1, 2, 3, 6, 5]

####################################################################################################

# Импортируем функцию для создания таблиц
from prettytable import PrettyTable

# Функция для первода из 10-ой системы в 2-ую
dec_to_bin = lambda x: bin(x)[2:]

# Функция для перевода из 2-ой системы в 10-ую
bin_to_dec = lambda x: int(x, 2)

# Функция для добавления нужного кол-ва незначащих нулей
correct_size = lambda x, size: '0'*(size-len(x))+x

####################################################################################################

# Функция для получения всевозможных значений двоичного числа
def range_of_values(number_of_bits):

    # Создаём список для хранения возможных значений
    data = []

    # ** - это возведение в степень
    for element in range(2**number_of_bits):

        # Преобразуем element к нужному виду с длиной number_of_bits
        element = correct_size(dec_to_bin(element), number_of_bits)

        # Добавляем полученное значение element в список data
        data.append(element)

    # Возвращаем список всевозможных значений двоичного числа
    return data

####################################################################################################

# Функция для поиска выходных значений в S-блоках по входным значениям
def Input_and_Output(S_block, number_of_S_block, Input):

    # Преобразуем Input к нужному виду с длиной 4 бита
    Input = correct_size(dec_to_bin(Input), 4)

    # Составляем координаты нужного Output в таблице S-блока
    # x - это индекс строки в S-блоке
    # y - это индекс столбца в S-блоке
    if number_of_S_block == 3:
        # Координата строки состоит из 2-ух битов
        x = Input[0] + Input[3]
        # Координата столбца состоит из 2-ух битов
        y = Input[1] + Input[2]
    else:
        # Координата строки состоит из 1-го бита
        x = Input[0]
        # Координата столбца состоит из 3-ех битов
        y = Input[1] + Input[2] + Input[3]

    # При помощи Input получаем Output из S_block
    Output = S_block [ bin_to_dec(x) ] [ bin_to_dec(y) ]

    # Определяем количество бит для значения Output
    number_of_bits = 2 + 1 * (number_of_S_block < 3)

    # Преобразуем Output к нужному виду с нужной длиной (2 или 3 бита)
    Output = correct_size(dec_to_bin(Output), number_of_bits)

    # Возврашаем список, включающий в себя Input и Output
    return [Input, Output]

####################################################################################################

# Функция для создания таблицы для конкретных значений alpha и betta
def creating_table_for_alpha_and_betta(S_block, number_of_S_block, alpha, betta):

    # Создаём новый объект для хранения таблицы для фиксированных значениях alpha и betta
    new_table = []

    # Создаём объект для хранения значений аналогов
    values_of_analogues = []

    # Для каждого из 16 возможных значений Input...
    for Input in range(16):

        # Находим Input и Output в двоичном виде
        Input, Output = Input_and_Output(S_block, number_of_S_block, Input)

        # Создаём объект для хранения пар (Input, alpha) и (Output, betta)
        elements = []

        # Для каждой пары (Input, alpha)...
        for i in range(4):
            # Добавляем каждую пару в объект elements
            elements.append([Input[i], alpha[i]])

        # Определяем количество пар (Output, betta)
        number_of_pairs = 2 + 1 * (number_of_S_block < 3)

        # Для каждой пары (Output, betta)...
        for j in range(number_of_pairs):
            # Добавляем каждую пару в объект elements
            elements.append([Output[j], betta[j]])

        # Создаём строку для хранения выражения, рассчитывающего вероятность
        Q = ""

        # Создаём переменную для хранения числового значения вероятности
        Result = 0

        # Для каждой пары в объекте elements...
        for pair in elements:
            # Добавляем произведение элементов пары к строке Q
            Q += "*".join(pair) + " ^ "
            # Преобразуем тип элементов в паре и строкового в числовой
            numbers = list(map(int, pair))
            # Выполняем операцию XOR для переменной Result произведения элементов из новой пары
            Result ^=  numbers[0] * numbers[1]

        # Отрезаем от контца строки Q ненужную строку ' ^ '
        Q = Q[:-3]

        # Добавляем список значений Input, Output, Q, Result в новую таблицу
        new_table.append( [Input, Output, Q, Result] )

        # Добавляем значение аналога (Result) в объект values_of_analogues
        values_of_analogues.append(Result)

    # Вероятность того, что в данной таблице значение аналога равно нулю
    probability = values_of_analogues.count(0) / 16

    # Возвращаем таблицу new_table и вероятность probability
    return [ new_table, probability ]

####################################################################################################

# Функция для получения таблицы для конкретного S_block
def creating_tables_for_S_block(S_block, number_of_S_block):

    # Создаём объект для хранения всех промежуточных таблиц для конкретного S_block
    many_tables = []

    # Определяем количество бит для каждого из значенй Output и betta
    number_of_bits = 2 + 1 * (number_of_S_block < 3)

    # Создадим список значений для alpha
    range_of_alpha = range_of_values(4)[1:]

    # Создадим список значений для betta
    range_of_betta = range_of_values(number_of_bits)[1:]

    # Создаём объект для хранения финальной таблицы (вид: alpha\betta)
    #   c вероятностями для конкретного S_block
    final_table = [ [0 for betta in range( len(range_of_betta) )]
                    for alpha in range( len(range_of_alpha) ) ]

    # Для каждого значения alpha...
    for alpha in range_of_alpha:

        # Для каждого значения betta...
        for betta in range_of_betta:

            # Создаём таблицу для конкретных значений alpha и betta
            #   и рассчитываем вероятность того, что в этой таблице Q=0
            table_alpha_betta, probability_of_Q_zero = \
                creating_table_for_alpha_and_betta(S_block, number_of_S_block, alpha, betta)

            # На 0-ую позицию в таблице для конкретных значений alpha и betta
            #   вставляем сами эти конкретные значения alpha и betta
            table_alpha_betta.insert(0, [alpha, betta, probability_of_Q_zero])

            # Добавляем новую промежуточную таблицу в объект для хранения промежуточных таблиц
            many_tables.append(table_alpha_betta)

            # Добавляем в итоговую таблицу вероятностей вероятность того,
            #   что Q=0 для в таблице для конкретных значений alpha и betta

            # Индекс строки в финальной таблице вероятностей
            i = bin_to_dec(alpha) - 1

            # Индекс столбца в финальной таблице вероятностей
            j = bin_to_dec(betta) - 1

            # В финальной таблице вероятностей устанавливаем значение вероятности для конкретной таблицы
            final_table[i][j] = int(probability_of_Q_zero) \
                if probability_of_Q_zero in [0, 1] else probability_of_Q_zero

    # Возвращаем все промежуточные таблицы для конкретного S_block
    #   и итоговую таблицу вероятностей для конкретного S_block
    return [many_tables, final_table]

####################################################################################################

# Функция для записи полученных таблиц (для конкретного S_block) в файл
def printing_tables_for_S_block(path_to_dir, number_of_S_block, many_tables, final_table):

    # Создаём объект для работы с текстовым файлом
    S_block = open(path_to_dir + "\\" + "Block_S_{}.txt".format(number_of_S_block), "w")

            ###################################
            #   Запись промежуточных таблиц   #
            ###################################

    # Создаём заголовок для каждой таблицы из промежуточных таблиц
    title_for_new_table = ["Input", "Output", \
        "Q = (Input, alpha) XOR (Output, betta)", "value_of_Q"]

    # Для каждой таблицы из промежуточных таблиц...
    for table in many_tables:

        # Определяем значения alpha, betta и вероятности того,
        #   что в данной таблице вероятность того, что Q = 0
        alpha, betta, probability_of_Q_zero = table[0]

        # Записываем полученные значения в файл
        S_block.write( "\t" + "alpha = {}, betta = {}, probability = {}\n".\
                      format(alpha, betta, probability_of_Q_zero) )

        # Из промежуточной таблицы создаём таблицу для печати
        table_for_printing = PrettyTable(title_for_new_table)

        # Для каждой строки в промежуточной таблице...
        for line in table[1:]:
            # Добавляем строку в таблицу для печати
            table_for_printing.add_row(line)

        # Запишем созданную таблицу для печати в файл
        S_block.write( str(table_for_printing) )

        # Запишем в файл отступ между таблицами
        S_block.write("\n\n\n")

            ############################################
            #   Запись итоговой таблицы вероятностей   #
            ############################################

    # Получаем количество бит в числе betta
    number_of_bits = 2 + 1*(number_of_S_block < 3)

    # Получаем объект, хранящий в себе названия столбцов
    #   для итоговой таблицы вероятностей
    columns = [ correct_size( dec_to_bin(betta), number_of_bits)
                for betta in range(2**number_of_bits) ][1:]

    # Создаём заголовок для итоговой таблицы вероятностей
    title_for_super_table = ["alpha & betta"] + columns

    # Из итоговой таблицы создаём таблицу для печати
    super_table = PrettyTable(title_for_super_table)

    # Для значений alpha из диапазона от 1 до 16
    #   и каждой строки в итоговой таблице (всего 15 строк)...
    for alpha, line in zip(range(1,16), final_table):

        # Получаем имя для новой строки в итоговой таблице
        name_of_line = correct_size( dec_to_bin(alpha), 4 )

        # Добавляем новую строку в итоговую таблицу
        super_table.add_row([name_of_line] + line)

    # Записываем заголовок для финальной таблицы вероятностей в файл
    S_block.write("\t" + "Final_table (alpha / betta)\n")

    # Запишем созданную итоговую таблицу в файл
    S_block.write( str(super_table) )

####################################################################################################

# Указываем путь до рабочей папки
path = "C:/laba2KMZI"

# Cоздадим промежуточные таблицы и итоговую таблицу вероятностей для конкретного S-блока
# После этого запишем эти таблицы в текстовый файл для конкретного S-блока

# Для блока S_1
many_tables_for_S_1, final_table_for_S_1 = creating_tables_for_S_block(S_1, 1)
printing_tables_for_S_block(path, 1, many_tables_for_S_1, final_table_for_S_1)

# Для блока S_2
many_tables_for_S_2, final_table_for_S_2 = creating_tables_for_S_block(S_2, 2)
printing_tables_for_S_block(path, 2, many_tables_for_S_2, final_table_for_S_2)

# Для блока S_3
many_tables_for_S_3, final_table_for_S_3 = creating_tables_for_S_block(S_3, 3)
printing_tables_for_S_block(path, 3, many_tables_for_S_3, final_table_for_S_3)



