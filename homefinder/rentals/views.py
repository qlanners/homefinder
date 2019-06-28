from django.http import HttpResponse

from django.shortcuts import render, render_to_response

import json

from .models import *

def index(request):	
	states = list(State.objects.values_list('abbrev','id'))
	states = {x:y for x,y in states}
	current_rent = list(State_Data.objects.select_related('state').filter(month=5).values_list('year','state__abbrev','median_studio','median_one_bed','median_two_bed','median_three_bed','median_four_bed','median_sfr'))
	years = list(State_Data.objects.values_list('year').distinct().order_by('-year'))
	years = [y[0] for y in years]
	current_rent_dict = {}
	for y in years:
		current_rent_dict[y] = {}
		for s in current_rent:
			if s[0] == y:
				current_rent_dict[y][s[1]] = (s[2],s[3],s[4],s[5],s[6],s[7])

	return render_to_response('index.html', {'current_rent':json.dumps(current_rent_dict), 'years':years, 'states': json.dumps(states)})

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

	return render_to_response('state.html', {'current_rent':json.dumps(current_rent_dict), 'years':years, 'map_link':json.dumps(map_link)})	

