text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin interdum augue et hendrerit. Proin vel lacus a velit dignissim laoreet at quis urna. Curabitur nec nulla diam. Nulla eget vestibulum mauris, vel gravida sapien. Duis laoreet pharetra auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam fermentum orci eu nunc accumsan, ut convallis velit sodales. Suspendisse eget nisi tristique, tempor lacus ut, porta nulla. Etiam eu sapien semper, mattis ligula id, egestas nulla. Curabitur ut justo placerat, sagittis mauris ut, hendrerit sapien. In tincidunt leo sem, non iaculis lectus tempus a. Vestibulum mattis enim quis ex pharetra, sed faucibus magna gravida."
#vowels = ['a', 'e', 'i', 'o', 'u', 'y']
vowels = 'aeiouy'

if "Zack" in text:
	print "Yes, it is!"

count_1, count_0 = 0, 0

for blargh in text:
	if blargh in vowels:
		count_0 = count_0 + 1

print 'There are %s vowels in that text.' % count_0


for blargh in text:
	for foo in vowels:
		if blargh == foo:
			count_1 = count_1 + 1

print 'There are %s vowels in that text.' % count_1


all_vowels = [vowel for vowel in text if vowel in vowels]

print 'There are %s vowels in text.' % len(all_vowels)