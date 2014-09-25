import fileinput


def car_classifier(age, salary, marital, car, ):
	age = float(age)
	salary = float(salary)
	if salary <= 80.0:
		if salary <= 30.0:
			return 'mini'
		else:
			if age <= 50.0:
				return 'van'
			else:
				return 'sports'
	else:
		if age <= 55.0:
			if age <= 35.0:
				return 'sports'
			else:
				if age <= 45.0:
					return 'luxury'
				else:
					return 'sports'
		else:
			return 'luxury'


if __name__ == '__main__':
    lines = fileinput.input()
    lines.next()  # Skip the first line, which are the column names
    for line in lines:
        cols = line.strip().split("\t")
        print '\t'.join(cols) + ' - ' + car_classifier(*cols)

