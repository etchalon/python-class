def remove_next_character(foo):
	if len(foo) > 0:
		foo = foo[1:]
		return remove_next_character(foo)
	return foo

text_1 = "Lorem ipsum 6 dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin interdum augue et hendrerit. Proin vel lacus a velit dignissim laoreet at quis urna. Curabitur nec nulla diam. Nulla eget vestibulum mauris, vel gravida sapien. Duis laoreet pharetra auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam fermentum orci eu nunc accumsan, ut convallis velit sodales. Suspendisse eget nisi tristique, tempor lacus ut, porta nulla. Etiam eu sapien semper, mattis ligula id, egestas nulla. Curabitur ut justo placerat, sagittis mauris ut, hendrerit sapien. In tincidunt leo sem, non iaculis lectus tempus a. Vestibulum 4 mattis enim quis 3 ex pharetra, sed 1 faucibus magna gravida."

print 'One character less is: %s' % remove_next_character(text_1)
