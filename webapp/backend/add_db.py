from backend.app import db, Authors, Affiliations, PaperAuthorAffiliations, PaperReferences

"""
a
"""
f = open("data/Authors.txt", "r")
#for i in range(10000):
while True:
    line = f.readline()
    if line:
        line = line.strip('\n')
        line = line.split('\t')
        if line[4] == '':  # handle missing value
            line[4] = -1
        # print(line[4])
        a = Authors(
            id=line[0],
            rank=line[1],
            normalized_name=line[2],
            display_name=line[3],
            last_know_affiliation_id=line[4],
            paper_count=line[5],
            paper_family_count=line[6],
            citation_count=line[7],
            created_date=line[8]
        )
        db.session.add(a)
    else:
        break
f.close()
db.session.commit()
print("Import Authors Completed")


"""
Import Affiliations
"""
f = open("data/Affiliations.txt", "r")
#for i in range(10000):
while True:
    line = f.readline()
    if line:
        line = line.strip('\n')
        line = line.split('\t')
        if line[11] == '':  # handle missing value
            line[11] = -1
        if line[12] == '':  # handle missing value
            line[12] = -1
        a = Affiliations(
            id=line[0],
            rank=line[1],
            normalized_name=line[2],
            display_name=line[3],
            grid_id=line[4],
            official_page=line[5],
            wiki_page=line[6],
            paper_count=line[7],
            paper_family_count=line[8],
            citation_count=line[9],
            iso_3166_code=line[10],
            latitude=line[11],
            longitude=line[12],
            created_date=line[13]
        )
        db.session.add(a)
    else:
        break
f.close()
db.session.commit()
print("Import Affiliations Completed")
'''
"""
Import Papers
"""
f = open("data/Papers.txt", "r")
count = 0
for i in range(1000000):
    count += 1
#while True:
    line = f.readline()
    if line:
        line = line.strip('\n')
        line = line.split('\t')
        # print(len(line))
        # print(line)
        # if line[11] == '':  # handle missing value
        #     line[11] = -1
        # if line[12] == '':  # handle missing value
        #     line[12] = -1
        a = Papers(
            id=line[0],
            rank=line[1],
            doi=line[2],
            doc_type=line[3],
            paper_title=line[4],
            original_title=line[5],
            # book_title=line[6],
            # year=line[7],
            # date=line[8],
            # online_date=line[9],
            # publisher=line[10],
            # journal_id=line[11],
            # conference_series_id=line[12],
            # conference_instance_id=line[13],
            # volume=line[14],
            # issue=line[15],
            # first_page=line[16],
            # lase_page=line[17],
            # reference_count=line[18],
            # citation_count=line[19],
            # estimated_citation=line[20],
            # original_venue=line[21],
            # family_id=line[22],
            # family_rank=line[23],
            # doc_sub_types=line[24],
            # created_date=line[25]
        )
        db.session.add(a)
    else:
        break
f.close()
db.session.commit()
print("Import Paper Completed")
print(count)
'''
"""
Import Paper Author Affiliations
"""
f = open("data/PaperAuthorAffiliations.txt", "r")
for i in range(1000000):
#while True:
    line = f.readline()
    if line:
        line = line.strip('\n')
        line = line.split('\t')
        if line[2] == '':  # handle missing value
            line[2] = -1
        a = PaperAuthorAffiliations(
            paper_id=line[0],
            author_id=line[1],
            affiliation_id=line[2],
            author_sequence_number=line[3],
            original_author=line[4],
            origunal_affiliation=line[5]
        )
        db.session.add(a)
    else:
        break
f.close()
db.session.commit()
print("Import Paper Author Affiliations Completed")


"""
Import Paper References
"""
f = open("data/PaperReferences.txt", "r")
for i in range(1000000):
#while True:
    line = f.readline()
    if line:
        line = line.strip('\n')
        line = line.split('\t')
        a = PaperReferences(
            paper_id=line[0],
            paper_reference_id=line[1]
        )
        db.session.add(a)
    else:
        break
f.close()
db.session.commit()
print("Import Paper References Completed")
