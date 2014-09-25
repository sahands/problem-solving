import fileinput

def classify(age, salary, marital, car, ):
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
