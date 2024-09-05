name = "CHARLES DICKENS"
dob = "February 7, 1812"
birthplace = "portsmouth, England"
famous_for = "A writer of the Victorian era"
married_to = "Catherine Hogarth"
year_of_marriage = "1836"
number_of_children = "ten"
famous_works = '"A Christmas Carol", "Oliver Twist", "David Copperfield", and "Great Expectations"'
other_talent = "doing DRAMATIC public readings of my work"
death_date = "June 9, 1870"
place_of_death = "Gad's Hill Place, Kent, England"

tamptext = '''Hello. My name is {}.
I am an English novelist. I was born on {}, in {}.
I am most famous as {}.
I married {} in {}. We have {} children.
Some of my most famous works include {}.
Besides being a writer, my other talent was {}.
I died on {}, at my home in {}.'''.format( name.lower().title(), dob, birthplace.title(),
                                           famous_for.lower()[0:15]+famous_for[15:], 
                                           married_to, year_of_marriage, number_of_children, famous_works, 
                                           other_talent.lower(), death_date, place_of_death)

title = "A Brief Profile of {}.{} in {} characters.\n\n".format(name.title().split('harles')[0],name.title().split('harles')[1],len(tamptext))

output_text = '''{}{}'''.format(title, tamptext)

print(output_text)

test_text = f'''A Brief Profile of C. Dickens in 505 characters.

Hello. My name is Charles Dickens.
I am an English novelist. I was born on February 7, 1812, in Portsmouth, England.
I am most famous as a writer of the Victorian era.
I married Catherine Hogarth in 1836. We have ten children.
Some of my most famous works include "A Christmas Carol", "Oliver Twist", "David Copperfield", and "Great Expectations".
Besides being a writer, my other talent was doing dramatic public readings of my work.
I died on June 9, 1870, at my home in Gad's Hill Place, Kent, England.'''

if output_text == test_text:
    print("SUCCESS! Yes, your output text matches the test text.")
else:
    print("OOPS!!! Sorry, your output text does not match the test text.")