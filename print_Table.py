tableData = [['name', 'mehrdad', 'ali', 'javad'],
             ['family', 'sadafi', 'mohammadi', 'razavi'],
             ['age', '24', '35', '54']]


def print_rigth_justified(table_data: list) -> str:
    # Find the maximum width for each column
    col_widths = [max(len(item) for item in column) for column in tableData]
    