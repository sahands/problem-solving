def classify(age, salary, marital, car, ):
	age = float(age)
	salary = float(salary)
	if salary <= 30.0:
		return 'mini'
	else:
		if salary <= 90.0:
			if age <= 30.0:
				return 'sports'
			else:
				if age <= 50.0:
					return 'van'
				else:
					return 'sports'
		else:
			if age <= 35.0:
				return 'sports'
			else:
				return 'luxury'
