"""Restaurant rating lister."""


# put your code here
retaurant_file = open("scores.txt")


# print(retaurant_lst)

def turn_file_into_list(file):


	# lst_of_restaurant_and_rating = []


	
	ratings_by_restaurant = {}

	for line in file:
		line = line.rstrip().split(":")
		# lst_of_restaurant_and_rating.append(line)
		restaurant_name, rating = line
		ratings_by_restaurant[restaurant_name] = rating
	# print(dictionary)

	restaurants = []
	for item in ratings_by_restaurant:
		
		restaurants.append(item)


	sorted_restaurants = sorted(restaurants)
	# print(sorted_dictionary)

	for key in sorted_restaurants:
		print("{} is rated at {}".format(key, ratings_by_restaurant[key]))

	# sorted_lst_of_restaurant_and_rating = sorted(lst_of_restaurant_and_rating)

	# print(sorted_lst_of_restaurant_and_rating)

	# for item in sorted_lst_of_restaurant_and_rating:
	# 	restaurant_name, rating = item
	# 	print("{} is rate at {}".format(restaurant_name, rating))
	



turn_file_into_list(retaurant_file)

# def turn_list_into_dictionary(lst):