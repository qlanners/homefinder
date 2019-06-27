from django.db import models

class Country(models.Model):
	country = models.CharField(max_length=100)
	abbrev = models.CharField(max_length=10)

	def __str__(self):
		return self.abbrev	


class State(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	state = models.CharField(max_length=50)
	abbrev = models.CharField(max_length=10)
	map_link = models.CharField(max_length=500, null=True)

	def __str__(self):
		return self.abbrev	

class County(models.Model):
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	county = models.CharField(max_length=100)

	def __str__(self):
		return self.county

class City(models.Model):
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	county = models.ForeignKey(County, null=True, on_delete=models.CASCADE)
	city = models.CharField(max_length=100)
	lat = models.DecimalField(null=True, decimal_places=4, max_digits=8)
	lon = models.DecimalField(null=True, decimal_places=4, max_digits=8)
	population = models.IntegerField(null=True)
	population_proper = models.IntegerField(null=True)
	population_density = models.IntegerField(null=True)
	timezone = models.CharField(null=True, max_length=100)

class State_Data(models.Model):
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	date = models.DateTimeField('data_month')
	year = models.IntegerField()
	month = models.IntegerField()
	median_studio = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_one_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_two_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_three_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_four_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_sfr = models.DecimalField(null=True, decimal_places=2, max_digits=12)



	def __str__(self):
		return str(self.state.abbrev) + ' ' + str(self.month) + '/' + str(self.year)

class County_Data(models.Model):
	county = models.ForeignKey(County, on_delete=models.CASCADE)
	date = models.DateTimeField('data_month')
	year = models.IntegerField()
	month = models.IntegerField()
	median_studio = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_one_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_two_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_three_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_four_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_sfr = models.DecimalField(null=True, decimal_places=2, max_digits=12)

	def __str__(self):
		return str(self.county.county) + ' ' + str(self.month) + '/' + str(self.year)	


class City_Data(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	date = models.DateTimeField('data_month')
	year = models.IntegerField()
	month = models.IntegerField()
	median_studio = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_one_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_two_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_three_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_four_bed = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_sfr = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_sqft_studio = models.DecimalField(null=True, decimal_places=4, max_digits=12)
	median_sqft_one_bed = models.DecimalField(null=True, decimal_places=4, max_digits=12)
	median_sqft_two_bed = models.DecimalField(null=True, decimal_places=4, max_digits=12)
	median_sqft_three_bed = models.DecimalField(null=True, decimal_places=4, max_digits=12)
	median_sqft_four_bed = models.DecimalField(null=True, decimal_places=4, max_digits=12)
	median_sqft_sfr = models.DecimalField(null=True, decimal_places=4, max_digits=12)
	median_list_price_all = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_list_price_bot = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_list_price_top = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	sales_count = models.IntegerField(null=True)
	foreclosure_resale_perc = models.DecimalField(null=True, decimal_places=10, max_digits=12)
	median_daily_listings_all = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	monthly_listings_all = models.IntegerField(null=True)
	sales_list_ratio = models.DecimalField(null=True, decimal_places=10, max_digits=12)
	days_on_zillow = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_price_reduced_all = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	price_cut_seas_adj_all = models.DecimalField(null=True, decimal_places=2, max_digits=12)
	median_sqft_list_price_all = models.DecimalField(null=True, decimal_places=4, max_digits=12)
	median_sqft_list_price_bot = models.DecimalField(null=True, decimal_places=4, max_digits=12)
	median_sqft_list_price_top = models.DecimalField(null=True, decimal_places=4, max_digits=12)

	def __str__(self):
		return str(self.city.city) + ' ' + str(self.month) + '/' + str(self.year)	
