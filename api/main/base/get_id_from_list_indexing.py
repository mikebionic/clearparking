def get_id_from_list_indexing(id_list, indexing_list, index):
	try:
		id = int(id_list[indexing_list.index(index)])
	except:
		id = None

	return id