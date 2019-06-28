from django.http import HttpResponse

from django.shortcuts import render, render_to_response

import json
import simplejson

from .models import *

def index(request):	
	states = list(State.objects.values_list('abbrev','id'))
	states = {x:y for x,y in states}
	cities = list(City.objects.filter(population__gte=500000).values('id','lat','lon','city'))
	current_states = list(State_Data.objects.select_related('state').filter(month=5).values_list('year','state__abbrev','median_studio','median_one_bed','median_two_bed','median_three_bed','median_four_bed','median_sfr'))
	years = list(State_Data.objects.values_list('year').distinct().order_by('-year'))
	current_cities = list(City_Data.objects.select_related('city').filter(month=5).filter(city__population__gte=500000).values_list('year','city','median_studio','median_one_bed','median_two_bed','median_three_bed','median_four_bed','median_sfr'))
	years = [y[0] for y in years]
	current_states_dict = {}
	current_cities_dict = {}
	for y in years:
		current_states_dict[y] = {}
		current_cities_dict[y] = {}
		larger_dict = max(len(current_states),len(current_cities))
		for l in range(larger_dict-1):
			if l < len(current_states):
				if current_states[l][0] == y:
					current_states_dict[y][current_states[l][1]] = [current_states[l][i] for i in range(2,len(current_states[l]))]
			if l < len(current_cities):
				if current_cities[l][0] == y:
					current_cities_dict[y][current_cities[l][1]] = [current_cities[l][i] for i in range(2,len(current_cities[l]))]

	return render_to_response('index.html', {'current_states':simplejson.dumps(current_states_dict, use_decimal=True), 'current_cities':simplejson.dumps(current_cities_dict, use_decimal=True), 'years':years, 'states': simplejson.dumps(states, use_decimal=True), 'cities': simplejson.dumps(cities, use_decimal=True)})

def state(request, state_id):
	current_rent = list(County_Data.objects.select_related('state').filter(month=5).filter(county__state__id=state_id).values_list('year','county__county','median_studio','median_one_bed','median_two_bed','median_three_bed','median_four_bed','median_sfr'))
	years = list(County_Data.objects.filter(county__state__id=state_id).values_list('year').distinct().order_by('-year'))
	years = [y[0] for y in years]
	current_rent_dict = {}
	for y in years:
		current_rent_dict[y] = {}
		for s in current_rent:
			if s[0] == y:
				current_rent_dict[y][s[1]] = (s[2],s[3],s[4],s[5],s[6],s[7])

	map_link = State.objects.filter(id=state_id).values_list('map_link')[0]

	return render_to_response('state.html', {'current_rent':simplejson.dumps(current_rent_dict, use_decimal=True), 'years':years, 'map_link':json.dumps(map_link)})	

