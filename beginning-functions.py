vowels = ['a', 'e', 'i', 'o', 'u', 'y']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

text_1 = "Lorem ipsum 6 dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin interdum augue et hendrerit. Proin vel lacus a velit dignissim laoreet at quis urna. Curabitur nec nulla diam. Nulla eget vestibulum mauris, vel gravida sapien. Duis laoreet pharetra auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam fermentum orci eu nunc accumsan, ut convallis velit sodales. Suspendisse eget nisi tristique, tempor lacus ut, porta nulla. Etiam eu sapien semper, mattis ligula id, egestas nulla. Curabitur ut justo placerat, sagittis mauris ut, hendrerit sapien. In tincidunt leo sem, non iaculis lectus tempus a. Vestibulum 4 mattis enim quis 3 ex pharetra, sed 1 faucibus magna gravida."
text_2 = "Lorem ipsum 6 dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin interdum augue et hendrerit. Proin vel lacus a velit dignissim laoreet at quis urna. Curabitur nec nulla diam. Nulla eget vestibulum mauris, vel gravida sapien. Duis laoreet pharetra auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam fermentum orci eu nunc accumsan, ut convallis velit sodales. Suspendisse eget nisi tristique, tempor lacus ut, porta nulla. Etiam eu sapien semper, mattis ligula id, egestas nulla. Curabitur ut justo placerat, sagittis mauris ut, hendrerit sapien. In tincidunt leo sem, non iaculis lectus tempus a. Vestibulum 4 mattis enim quis 3 ex pharetra, sed 1 faucibus magna gravida."
text_3 = "Lorem ipsum 6 dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin interdum augue et hendrerit. Proin vel lacus a velit dignissim laoreet at quis urna. Curabitur nec nulla diam. Nulla eget vestibulum mauris, vel gravida sapien. Duis laoreet pharetra auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam fermentum orci eu nunc accumsan, ut convallis velit sodales. Suspendisse eget nisi tristique, tempor lacus ut, porta nulla. Etiam eu sapien semper, mattis ligula id, egestas nulla. Curabitur ut justo placerat, sagittis mauris ut, hendrerit sapien. In tincidunt leo sem, non iaculis lectus tempus a. Vestibulum 4 mattis enim quis 3 ex pharetra, sed 1 faucibus magna gravida."
text_4 = "Lorem ipsum 6 dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin interdum augue et hendrerit. Proin vel lacus a velit dignissim laoreet at quis urna. Curabitur nec nulla diam. Nulla eget vestibulum mauris, vel gravida sapien. Duis laoreet pharetra auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam fermentum orci eu nunc accumsan, ut convallis velit sodales. Suspendisse eget nisi tristique, tempor lacus ut, porta nulla. Etiam eu sapien semper, mattis ligula id, egestas nulla. Curabitur ut justo placerat, sagittis mauris ut, hendrerit sapien. In tincidunt leo sem, non iaculis lectus tempus a. Vestibulum 4 mattis enim quis 3 ex pharetra, sed 1 faucibus magna gravida."
text_5 = "Lorem ipsum 6 dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin interdum augue et hendrerit. Proin vel lacus a velit dignissim laoreet at quis urna. Curabitur nec nulla diam. Nulla eget vestibulum mauris, vel gravida sapien. Duis laoreet pharetra auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam fermentum orci eu nunc accumsan, ut convallis velit sodales. Suspendisse eget nisi tristique, tempor lacus ut, porta nulla. Etiam eu sapien semper, mattis ligula id, egestas nulla. Curabitur ut justo placerat, sagittis mauris ut, hendrerit sapien. In tincidunt leo sem, non iaculis lectus tempus a. Vestibulum 4 mattis enim quis 3 ex pharetra, sed 1 faucibus magna gravida."
text_6 = "Lorem ipsum 6 dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin interdum augue et hendrerit. Proin vel lacus a velit dignissim laoreet at quis urna. Curabitur nec nulla diam. Nulla eget vestibulum mauris, vel gravida sapien. Duis laoreet pharetra auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam fermentum orci eu nunc accumsan, ut convallis velit sodales. Suspendisse eget nisi tristique, tempor lacus ut, porta nulla. Etiam eu sapien semper, mattis ligula id, egestas nulla. Curabitur ut justo placerat, sagittis mauris ut, hendrerit sapien. In tincidunt leo sem, non iaculis lectus tempus a. Vestibulum 4 mattis enim quis 3 ex pharetra, sed 1 faucibus magna gravida."
text_7 = "Lorem ipsum 6 dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin interdum augue et hendrerit. Proin vel lacus a velit dignissim laoreet at quis urna. Curabitur nec nulla diam. Nulla eget vestibulum mauris, vel gravida sapien. Duis laoreet pharetra auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam fermentum orci eu nunc accumsan, ut convallis velit sodales. Suspendisse eget nisi tristique, tempor lacus ut, porta nulla. Etiam eu sapien semper, mattis ligula id, egestas nulla. Curabitur ut justo placerat, sagittis mauris ut, hendrerit sapien. In tincidunt leo sem, non iaculis lectus tempus a. Vestibulum 4 mattis enim quis 3 ex pharetra, sed 1 faucibus magna gravida."
text_9 = '1212312391823120938190283091820938'

def count_vowels (foo):
	vowel_count = 0
	for character in foo:
		if character in ['a', 'e', 'i', 'o', 'u', 'y']:
			vowel_count += 1
	return vowel_count

vowel_count = count_vowels(text_1)


if count_vowels(text_9):
	print "We have vowels!"

print 'Text 1 has %s vowels' % vowel_count
print 'Text 2 has %s vowels' % count_vowels(text_2)
print 'Text 3 has %s vowels' % count_vowels(text_3)

vowel_count = 0
number_count = 0

for character in text_1:
	if character in ['a', 'e', 'i', 'o', 'u', 'y']:
		vowel_count += 1
	if character in ['%s' % num for num in numbers]:
		number_count += 1

print '%d vowels' % vowel_count
print '%d numbers' % number_count


vowel_count = 0
number_count = 0

for character in text_2:
	if character in ['a', 'e', 'i', 'o', 'u', 'y']:
		vowel_count += 1
	if character in ['%s' % num for num in numbers]:
		number_count += 1
vowel_count = vowel_count * 2

print '%d vowels' % vowel_count
print '%d numbers' % number_count
