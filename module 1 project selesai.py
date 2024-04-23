from tabulate import tabulate
import datetime

# Chemical list
chem_list = [
    {'product': 'Sodium Chloride', 'hs': 457800, 'dg': 'no', 'kg/bag': 50, 'qty': 12, 'price/kg': 1500,
     'in': datetime.date(2024, 3, 28), 'exp': datetime.date(2027, 9, 28)},
    {'product': 'Potassium Nitrate', 'hs': 275400, 'dg': 'no', 'kg/bag': 45, 'qty': 13, 'price/kg': 1800,
     'in': datetime.date(2024, 2, 12), 'exp': datetime.date(2026, 8, 12)},
    {'product': 'Citric Acid', 'hs': 123400, 'dg': 'no', 'kg/bag': 25, 'qty': 25, 'price/kg': 1200,
     'in': datetime.date(2024, 1, 15), 'exp': datetime.date(2026, 7, 15)},
    {'product': 'Sodium Bicarbonate', 'hs': 987600, 'dg': 'no', 'kg/bag': 25, 'qty': 10, 'price/kg': 2000,
     'in': datetime.date(2023, 12, 5), 'exp': datetime.date(2027, 6, 5)},
    {'product': 'Calcium Carbonate', 'hs': 543200, 'dg': 'no', 'kg/bag': 45, 'qty': 7, 'price/kg': 1500,
     'in': datetime.date(2023, 11, 20), 'exp': datetime.date(2027, 5, 20)},
    {'product': 'Acetic Acid', 'hs': 291521, 'dg': 'yes', 'kg/bag': 50, 'qty': 30, 'price/kg': 3200,
     'in': datetime.date(2024, 7, 12), 'exp': datetime.date(2027, 1, 12)},
    {'product': 'Ammonia', 'hs': 281410, 'dg': 'yes', 'kg/bag': 25, 'qty': 20, 'price/kg': 1800,
     'in': datetime.date(2024, 7, 20), 'exp': datetime.date(2027, 1, 20)}
]

nondg_storage = 3500
dg_storage = 3000
cart = []

header = ['No', 'Product Name', 'HS Code', 'Dangerous Good', 'KG per Bag',
          'Bag Quantity', 'Price/KG', 'Entry Date', 'Expiry Date']

cart_header = ['No', 'Customer Name', 'Product Name', 'Total Price', 'Out Date']

chem_list2 = [[i + 1, item['product'], item['hs'], item['dg'], item['kg/bag'], item['qty'],
              item['price/kg'], item['in'], item['exp']] for i, item in enumerate(chem_list)]

def display_chem():
    print(tabulate(chem_list2, headers=header, tablefmt="pretty"))

    while True:
        display_menu = int(input('''\nDisplay based on:
1. Search Chemical
2. Sort Chemical
3. Back
Input index: '''))

        if display_menu == 1:
            search_chemical()
        elif display_menu == 2:
            sort_chemical()
        elif display_menu == 3:
            break
        else:
            print('Invalid input! Please try again.')

def search_chemical():
    while True:
        search_by = int(input('''\nSearch by:
1. Product Name
2. HS code
3. Exit
Input index: '''))

        if search_by == 1:
            search_list = []
            search_product = input('Product name: ').capitalize()
            for item in chem_list:
                if search_product in item['product']:
                    search_list.append(item)

            if search_list:
                search_list_tabulated = [[value for value in item.values()] for item in search_list]
                print(tabulate(search_list_tabulated, headers=header, tablefmt='pretty'))
            else:
                print('Product unavailable\n')

        elif search_by == 2:
            search_list = []
            search_hs = input('HS code: ')
            for item in chem_list:
                if str(item['hs']).startswith(search_hs):
                    search_list.append(item)

            if search_list:
                search_list_tabulated = [[value for value in item.values()] for item in search_list]
                print(tabulate(search_list_tabulated, headers=header, tablefmt='pretty'))
            else:
                print('Product unavailable\n')

        elif search_by == 3:
            break
        else:
            print('Invalid input! Please try again.')

def sort_chemical():
    while True:
        sort_by = int(input('''\nSort by:
1. Product name
2. HS code
3. DG category
4. KG per Bag
5. Quantity
6. Price per KG
7. Entry time
8. Expiry time
9. Back
Input index: '''))

        if 1 <= sort_by <= 8:
            sorted_chem_list = sorted(chem_list2, key=lambda item: item[sort_by])
            print(tabulate(sorted_chem_list, headers=header, tablefmt='pretty'))
        elif sort_by == 9:
            break
        else:
            print('Please give a correct input!')

def add_chem():
    while True:
        new_product = input('Input new product name: ').capitalize()
        new_hs = input('Input new HS code: ')
        if not new_hs.isdigit():
            print('Invalid HS code! Please enter a numeric value.')
            continue
        new_dg = input('Dangerous good? (yes/no): ').lower()
        if new_dg not in ['yes', 'no']:
            print('Invalid input! Please enter "yes" or "no".')
            continue
        new_kgbag = input('Kilos per bag: ')
        if not new_kgbag.isdigit():
            print('Invalid input! Please enter a numeric value.')
            continue
        new_qty = input('Quantity of bag: ')
        if not new_qty.isdigit():
            print('Invalid input! Please enter a numeric value.')
            continue
        new_pricekg = input('Price per bag: ')
        if not new_pricekg.isdigit():
            print('Invalid input! Please enter a numeric value.')
            continue
        while True:
            new_in = input('Entry date (Format: YYYY-MM-DD): ')
            try:
                new_in_date = datetime.datetime.strptime(new_in, '%Y-%m-%d').date()
                break
            except ValueError:
                print('Invalid date format! Please enter in the format YYYY-MM-DD.')
        while True:
            new_exp = input('Expiry date (Format: YYYY-MM-DD): ')
            try:
                new_exp_date = datetime.datetime.strptime(new_exp, '%Y-%m-%d').date()
                break
            except ValueError:
                print('Invalid date format! Please enter in the format YYYY-MM-DD.')

        new_item = {'product': new_product, 'hs': int(new_hs), 'dg': new_dg, 'kg/bag': int(new_kgbag),
                    'price/kg': int(new_pricekg), 'in': new_in_date, 'exp': new_exp_date}

        # Check if the item already exists, except for the quantity
        item_exists = False
        for item in chem_list:
            if item['product'] == new_product and item['hs'] == int(new_hs) and item['dg'] == new_dg and item['kg/bag'] == int(new_kgbag) and item['price/kg'] == int(new_pricekg) and item['in'] == new_in_date and item['exp'] == new_exp_date:
                item['qty'] += int(new_qty)
                item_exists = True
                print(f"Quantity of {new_product} updated successfully!")
                break

        if not item_exists:
            # Check storage capacity
            total_kg = int(new_kgbag) * int(new_qty)
            if new_dg == 'yes' and total_kg > dg_storage:
                print(f"Error: Cannot add {new_product}. Insufficient DG storage capacity.")
                continue
            elif new_dg == 'no' and total_kg > nondg_storage:
                print(f"Error: Cannot add {new_product}. Insufficient non-DG storage capacity.")
                continue

            new_item['qty'] = int(new_qty)
            chem_list.append(new_item)
            chem_list2.append([len(chem_list), new_product, int(new_hs), new_dg, int(new_kgbag), int(new_qty),
                               int(new_pricekg), new_in_date, new_exp_date])
            print('New product added successfully!')

        break

def update_chem():
    while True:
        update_menu = int(input('''\nUPDATE MENU:
1. Display Chemical
2. Update Chemical
3. Exit
\nPlease input menu index: '''))

        if update_menu == 1:
            display_chem()
        elif update_menu == 2:
            while True:
                i_update = int(input('Please input the index number of the product: '))
                if 1 <= i_update <= len(chem_list2):
                    i_update -= 1
                    print(tabulate([chem_list2[i_update]], headers=header))
                    while True:
                        update_value = int(input('''\nUpdate list:
1. Product Name
2. HS Code
3. Dangerous Good
4. KG per Bag
5. Bag Quantity
6. Price/KG
7. Entry Date
8. Expiry Date
9. Back
\nPlease input index: '''))

                        if update_value == 1:
                            update_product = input('Update product name: ').capitalize()
                            chem_list[i_update]['product'] = update_product
                            chem_list2[i_update][1] = update_product
                            print('Product name updated successfully!')
                        elif update_value == 2:
                            update_hs = input('Update HS code: ')
                            if update_hs.isdigit():
                                chem_list[i_update]['hs'] = int(update_hs)
                                chem_list2[i_update][2] = int(update_hs)
                                print('HS code updated successfully!')
                            else:
                                print('Invalid input! HS code must be a number.')
                        elif update_value == 3:
                            update_dg = input('Update DG category (yes/no): ').lower()
                            if update_dg == 'yes' or update_dg == 'no':
                                total_kg = chem_list[i_update]['kg/bag'] * chem_list[i_update]['qty']
                                if update_dg == 'yes' and total_kg > dg_storage:
                                    print(f"Error: Cannot update {chem_list[i_update]['product']}. Insufficient DG storage capacity.")
                                    continue
                                elif update_dg == 'no' and total_kg > nondg_storage:
                                    print(f"Error: Cannot update {chem_list[i_update]['product']}. Insufficient non-DG storage capacity.")
                                    continue
                                chem_list[i_update]['dg'] = update_dg
                                chem_list2[i_update][3] = update_dg
                                print('DG category updated successfully!')
                            else:
                                print('Invalid input! DG category must be "yes" or "no".')
                        elif update_value == 4:
                            update_kgbag = input('Update Kilos per bag: ')
                            if update_kgbag.isdigit():
                                new_total_kg = int(update_kgbag) * chem_list[i_update]['qty']
                                if chem_list[i_update]['dg'] == 'yes' and new_total_kg > dg_storage:
                                    print(f"Error: Cannot update {chem_list[i_update]['product']}. Insufficient DG storage capacity.")
                                    continue
                                elif chem_list[i_update]['dg'] == 'no' and new_total_kg > nondg_storage:
                                    print(f"Error: Cannot update {chem_list[i_update]['product']}. Insufficient non-DG storage capacity.")
                                    continue
                                chem_list[i_update]['kg/bag'] = int(update_kgbag)
                                chem_list2[i_update][4] = int(update_kgbag)
                                print('Kilos per bag updated successfully!')
                            else:
                                print('Invalid input! Kilos per bag must be a number.')
                        elif update_value == 5:
                            update_qty = input('Update bag quantity: ')
                            if update_qty.isdigit():
                                new_total_kg = int(update_qty) * chem_list[i_update]['kg/bag']
                                if chem_list[i_update]['dg'] == 'yes' and new_total_kg > dg_storage:
                                    print(f"Error: Cannot update {chem_list[i_update]['product']}. Insufficient DG storage capacity.")
                                    continue
                                elif chem_list[i_update]['dg'] == 'no' and new_total_kg > nondg_storage:
                                    print(f"Error: Cannot update {chem_list[i_update]['product']}. Insufficient non-DG storage capacity.")
                                    continue
                                chem_list[i_update]['qty'] = int(update_qty)
                                chem_list2[i_update][5] = int(update_qty)
                                print('Bag quantity updated successfully!')
                            else:
                                print('Invalid input! Bag quantity must be a number.')
                        elif update_value == 6:
                            update_pricekg = input('Update price per kg: ')
                            if update_pricekg.isdigit():
                                chem_list[i_update]['price/kg'] = int(update_pricekg)
                                chem_list2[i_update][6] = int(update_pricekg)
                                print('Price per kg updated successfully!')
                            else:
                                print('Invalid input! Price per kg must be a number.')
                        elif update_value == 7:
                            update_in = input('Update entry date (YYYY-MM-DD): ')
                            try:
                                update_in_date = datetime.datetime.strptime(update_in, '%Y-%m-%d').date()
                                new_total_kg = chem_list[i_update]['kg/bag'] * chem_list[i_update]['qty']
                                if chem_list[i_update]['dg'] == 'yes' and new_total_kg > dg_storage:
                                    print(f"Error: Cannot update {chem_list[i_update]['product']}. Insufficient DG storage capacity on {update_in_date}.")
                                    continue
                                elif chem_list[i_update]['dg'] == 'no' and new_total_kg > nondg_storage:
                                    print(f"Error: Cannot update {chem_list[i_update]['product']}. Insufficient non-DG storage capacity on {update_in_date}.")
                                    continue
                                chem_list[i_update]['in'] = update_in_date
                                chem_list2[i_update][7] = update_in_date
                                print('Entry date updated successfully!')
                            except ValueError:
                                print('Invalid date format! Please enter in the format YYYY-MM-DD.')
                        elif update_value == 8:
                            update_exp = input('Update expiry date (YYYY-MM-DD): ')
                            try:
                                update_exp_date = datetime.datetime.strptime(update_exp, '%Y-%m-%d').date()
                                chem_list[i_update]['exp'] = update_exp_date
                                chem_list2[i_update][8] = update_exp_date
                                print('Expiry date updated successfully!')
                            except ValueError:
                                print('Invalid date format! Please enter in the format YYYY-MM-DD.')
                        elif update_value == 9:
                            break
                        else:
                            print('Invalid input! Please try again.')
                else:
                    print('Invalid index number! Please try again.')
        elif update_menu == 3:
            break
        else:
            print('Invalid input! Please try again.')

def delete_chem():
    print(tabulate(chem_list2, headers=header, tablefmt="pretty"))
    while True:
        index_str = input('Please input the index of the chemical you want to delete or enter 0 to cancel: ')
        if index_str.isdigit():
            index = int(index_str)
            if 1 <= index <= len(chem_list):
                index -= 1
                item_to_delete = chem_list2[index]
                print(tabulate([item_to_delete], headers=header, tablefmt='pretty'))
                confirm = input(f'Are you sure you want to delete "{item_to_delete[1]}"? (yes/no): ').lower()
                if confirm == 'yes':
                    del chem_list[index]
                    del chem_list2[index]
                    print('The item has been successfully deleted.')
                    return
                elif confirm == 'no':
                    print('Deletion cancelled.')
                    return
                else:
                    print('Invalid input! Please try again.')
            elif index == 0:
                print('Deletion cancelled.')
                return
            else:
                print('Invalid index! Please try again.')
        else:
            print('Invalid input! Please try again.')

def allocation_chem():
    customer_name = input('Customer name: ')
    while True:
        print(tabulate(chem_list2, headers=header, tablefmt="pretty"))
        customer_chem = input('Please input the index of the chemical: ')
        if customer_chem.isdigit():
            customer_chem = int(customer_chem)
            if 1 <= customer_chem <= len(chem_list):
                customer_chem -= 1
                print(tabulate([chem_list2[customer_chem]], headers=header, tablefmt="pretty"))
                customer_out = input('Date of the chemical going out (YYYY-MM-DD): ')
                try:
                    customer_out_date = datetime.datetime.strptime(customer_out, '%Y-%m-%d').date()
                    if customer_out_date < chem_list[customer_chem]['exp']:
                        customer_qty = input('How many quantity is going out: ')
                        if customer_qty.isdigit() and 0 < int(customer_qty) <= chem_list[customer_chem]['qty']:
                            customer_qty = int(customer_qty)
                            chem_list[customer_chem]['qty'] -= customer_qty
                            new_cart = {'name': customer_name,
                                        'product': chem_list[customer_chem]['product'],
                                        'sum_price': customer_qty * chem_list[customer_chem]['kg/bag'] * chem_list[customer_chem]['price/kg'],
                                        'out': customer_out_date}
                            cart.append(new_cart)
                            print('The item is successfully added to the cart.')
                        else:
                            print('The quantity is outside of the range.')
                    else:
                        print('The out date is after the expiry date. Please choose a different date.')
                except ValueError:
                    print('Invalid date format! Please enter in the format YYYY-MM-DD.')
            else:
                print('Invalid index! Please try again.')
        else:
            print('Invalid input! Please try again.')
        
        display_cart = input('Do you want to display the cart? (yes/no): ').lower()
        if display_cart == 'yes':
            cart2 = [[i + 1, item['name'], item['product'], item['sum_price'], item['out']] for i, item in enumerate(cart)]
            print(tabulate(cart2, headers=cart_header, tablefmt="pretty"))
        
        continue_or_not = input('Do you want to continue allocating chemicals? (yes/no): ').lower()
        if continue_or_not == 'no':
            break

def main_menu():
    while True:
        menu = int(input('''\nWELCOME TO THE WAREHOUSE:
1. Display Table
2. Add Chemical
3. Update Chemical
4. Delete Chemical
5. Allocation Chemical
6. Exit
\nPlease insert index menu: '''))
        if menu == 1:
            display_chem()
        elif menu == 2:
            add_chem()
        elif menu == 3:
            update_chem()
        elif menu == 4:
            delete_chem()
        elif menu == 5:
            allocation_chem()
        elif menu == 6:
            print('Thank you for using the program. Goodbye!')
            break
        else:
            print('Invalid input! Please try again.')

main_menu()