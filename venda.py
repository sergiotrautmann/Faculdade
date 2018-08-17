def file_to_dict(file_name):
    file = open(file_name, 'r')

    dict = {}
    for line in file:
        line = line.strip()
        list = line.split(';')
        product_name = list[0].replace('"', '')
        product_quant = int(list[1])
        product_value = float(list[2])
        dict[product_name] = [product_quant, product_quant]


    file.close()
    return dict

estoque = file_to_dict('estoque.txt')

venda = [["Tomate", 5], ["Batata", 10], ["Feijão", 243]]
for sell in venda:
    product = sell[0]
    quant = sell[1]
    value = sell[2]
