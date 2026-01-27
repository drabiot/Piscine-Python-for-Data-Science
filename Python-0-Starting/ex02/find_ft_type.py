# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 15:34:10 by tchartie          #+#    #+#              #
#    Updated: 2026/01/27 15:59:41 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
	objType = type(object)

	if isinstance(object, list): 
		print("List :", objType)
	elif isinstance(object, tuple): 
		print("Tuple :", objType)
	elif isinstance(object, set): 
		print("Set :", objType)
	elif isinstance(object, dict): 
		print("Dict :", objType)
	elif isinstance(object, str): 
		print(object, "is in the kitchen :", objType)
	else:
		print("Type not found")

	return (42)
