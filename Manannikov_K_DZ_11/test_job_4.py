class OfficeEquipmentWarehouse:

    data = dict(company_1={'department1': 0, 'department2': 0},
                company_2={'department1': 0, 'department2': 0, 'department3': 0, 'department4': 0})  # Информация об оборудовании в офисах компаний

    equipment_warehouse_data = {
        'Printer': 400,
        'Copier': 300,
        'Scanner': 200
    }  # изначальное количество оборудования на складе

    def __init__(self, capacity):
        self.capacity = capacity  # вместимость склада

    def list_of_company_names(self):
        return self.data.keys()  # имена компаний

    def list_of_departments_of_this_company(self, company):
        return self.data[company].keys()  # отделы

    def list_of_office_equipment(self):
        return self.equipment_warehouse_data.keys()  # названия оборудования на складе

    def print_office_equipment(self):
        for key, value in self.equipment_warehouse_data.items():
            print(f'{key}: {value}')

    def print_office_equipment_by_department_of_the_company(self):
        for key, value in self.data.items():
            print(f'{key}: {value}')

    @property
    def total_office_equipment(self):
        total = 0
        for key, value in self.equipment_warehouse_data.items():
            total += value
        return total  # всего оборудования

    def is_valid_data(self, name, number, *args):  # проверка ввода
        if args:
            company_name, department_name = args
            if company_name not in self.list_of_company_names() or \
                    department_name not in self.list_of_departments_of_this_company(company_name):
                print('Such company or department is not listed')
                return False
        if name in self.list_of_office_equipment() and type(number) == int:
            return True
        else:
            print('Refine the data. Data is not correct')
            return False

    def receving(self, *args):  # метод передачи на склад
        for office_equipment, number_of_units in args:
            office_equipment_name = office_equipment.__class__.__name__
            if self.is_valid_data(office_equipment_name, number_of_units):
                if (self.total_office_equipment + number_of_units) <= self.capacity:
                    self.equipment_warehouse_data[office_equipment_name] += number_of_units
                else:
                    print(f'Capacity of office equipment warehouse {self.capacity} units.\nThe warehouse '
                          f'is unable to accept additional {number_of_units} units of {office_equipment_name}')
            else:
                print('Unable to perform the operation of receiving office equipment.')

    def transfer(self, company, department, *args):  # метод передачи в отдел
        for office_equipment, number_of_units in args:
            office_equipment_name = office_equipment.__class__.__name__
            if self.is_valid_data(office_equipment_name, number_of_units, company, department):
                self.data[company][department] += number_of_units
                self.equipment_warehouse_data[office_equipment_name] -= number_of_units
            else:
                print('Unable to perform office equipment transfer operation.')


class OfficeEquipment:
    def __init__(self, title):
        self.title = title


class Printer(OfficeEquipment):
    def __init__(self, title, scent):
        OfficeEquipment.__init__(self, title)
        self.scent = scent

    def __str__(self):
        return 'Модель:' + OfficeEquipment.__str__(self) + ' ,а запах: ' + str(self.scent)




class Scanner(OfficeEquipment):
    def __init__(self, title, color):
        OfficeEquipment.__init__(self, title)
        self.color = color

    def __str__(self):
        return 'Модель:' + OfficeEquipment.__str__(self) + ' ,цвет: ' + str(self.color)


class Xerox(OfficeEquipment):
    def __init__(self, title, scent):
        OfficeEquipment.__init__(self, title)
        self.scent = scent

    def __str__(self):
        return 'Модель:' + OfficeEquipment.__str__(self) + ' ,вкуc: ' + str(self.scent)



printer = Printer('Design Jet', 'финская полиграфия')
scanner = Scanner('Plustek', 'такой беленький')
copier = Xerox('Nomen est omen', 'пальчики оближешь')

depot = OfficeEquipmentWarehouse(1200)
depot.print_office_equipment()
print('Total: ', depot.total_office_equipment)
print()
depot.receving((printer, 70), (scanner, 800), (copier, 60))
depot.print_office_equipment()
print('Total: ', depot.total_office_equipment)
print()
depot.receving((printer, 50), (scanner, 20), (copier, 200))
depot.print_office_equipment()
print('Total: ', depot.total_office_equipment)
print()
printer111 = OfficeEquipment("принтер")
depot.receving((printer111, 50))
print()
depot.transfer('company_1', 'department1',
               (printer, 30), (scanner, 20), (copier, 10))
depot.transfer('company_2', 'department1',
               (printer, 30), (scanner, 20), (copier, 10))
depot.transfer('company_2', 'department2',
               (printer, 30), (scanner, 20), (copier, 10))
depot.print_office_equipment_by_department_of_the_company()
depot.print_office_equipment()
print('Total: ', depot.total_office_equipment)
print()
depot.transfer('company_2', 'department3', (printer, '50units'))
print()
depot.transfer('company_3', 'department1', (printer, 20))
print()
depot.transfer('company_2', 'department10', (printer, 60))