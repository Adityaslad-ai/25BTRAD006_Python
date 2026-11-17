import csv

try:
    total_gross = 0
    total_deductions = 0
    total_net = 0
    count = 0

    with open("employees.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        print("Employee Payroll Summary")
        print("-" * 65)

        for employee in reader:
            try:
                name = employee["Name"]
                basic = float(employee["Basic"])
                hra_rate = float(employee["HRA"])
                da_rate = float(employee["DA"])
                deduction_rate = float(employee["Deduction"])

                if (not name.strip() or
                    min(basic, hra_rate, da_rate,
                        deduction_rate) < 0 or
                    max(hra_rate, da_rate, deduction_rate) > 100):
                    print("Invalid record:", employee)
                    continue

                hra = basic * hra_rate / 100
                da = basic * da_rate / 100

                gross = basic + hra + da
                deductions = gross * deduction_rate / 100
                net = gross - deductions

                print("\nEmployee:", name)
                print("Gross Salary: Rs.", round(gross, 2))
                print("Deductions: Rs.", round(deductions, 2))
                print("Net Salary: Rs.", round(net, 2))

                total_gross += gross
                total_deductions += deductions
                total_net += net
                count += 1

            except (ValueError, KeyError):
                print("Invalid employee data:", employee)

    print("\n" + "-" * 65)
    print("Total Employees:", count)
    print("Total Gross Salary: Rs.", round(total_gross, 2))
    print("Total Deductions: Rs.", round(total_deductions, 2))
    print("Total Net Salary: Rs.", round(total_net, 2))

    if count > 0:
        print("Average Net Salary: Rs.", round(total_net / count, 2))

except FileNotFoundError:
    print("Employee CSV file not found.")
