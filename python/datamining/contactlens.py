def classify(age, spectacle_prescription, astigmatism, tear_product_rate, contact_lens):
	if tear_product_rate == 'reduced':
		return 'none'
	if tear_product_rate == 'normal':
		if astigmatism == 'yes':
			if spectacle_prescription == 'hypermetrope':
				if age == 'pre-presbyopic':
					return 'none'
				if age == 'presbyopic':
					return 'none'
				if age == 'young':
					return 'hard'
			if spectacle_prescription == 'myope':
				return 'hard'
		if astigmatism == 'no':
			if age == 'pre-presbyopic':
				return 'soft'
			if age == 'presbyopic':
				if spectacle_prescription == 'hypermetrope':
					return 'soft'
				if spectacle_prescription == 'myope':
					return 'none'
			if age == 'young':
				return 'soft'
