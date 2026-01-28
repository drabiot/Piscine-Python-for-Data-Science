# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:02:40 by tchartie          #+#    #+#              #
#    Updated: 2026/01/28 17:30:11 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
	objType = type(object)
	returnVal = 0

	if object == None:
		print(object, objType)
	elif isinstance(object, float) and object != object:
		print("Cheese:", object, objType)
	elif isinstance(object, int) and object == 0:
		print("Zero:", object, objType)
	elif isinstance(object, str) and len(object) == 0:
		print("Empty:", object, objType)
	elif isinstance(object, bool) and object == False:
		print("Fake:", object, objType)
	else:
		print("Type not found")
		returnVal = 1

	return (returnVal)
