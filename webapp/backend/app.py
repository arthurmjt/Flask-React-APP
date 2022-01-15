from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ABCabc123!@localhost/mag'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
db = SQLAlchemy(app)

"""
Create DB Tables
"""


class Authors(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.BigInteger, primary_key=True)
    rank = db.Column(db.BigInteger, nullable=False)
    normalized_name = db.Column(db.Text, nullable=False)
    display_name = db.Column(db.Text, nullable=False)
    last_know_affiliation_id = db.Column(db.BigInteger, nullable=False)
    # last_know_affiliation_id = db.Column(db.BigInteger, db.ForeignKey("affiliations.id"), nullable=False)
    paper_count = db.Column(db.BigInteger, nullable=False)
    paper_family_count = db.Column(db.BigInteger, nullable=False)
    citation_count = db.Column(db.BigInteger, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    # papers = db.relationship("Papers", secondary="paper_author_affiliations", backref="author")


class Affiliations(db.Model):
    __tablename__ = "affiliations"

    id = db.Column(db.BigInteger, primary_key=True)
    rank = db.Column(db.BigInteger, nullable=False)
    normalized_name = db.Column(db.Text, nullable=False)
    display_name = db.Column(db.Text, nullable=False)
    grid_id = db.Column(db.Text, nullable=False)
    official_page = db.Column(db.Text, nullable=False)
    wiki_page = db.Column(db.Text, nullable=False)
    paper_count = db.Column(db.BigInteger, nullable=False)
    paper_family_count = db.Column(db.BigInteger, nullable=False)
    citation_count = db.Column(db.BigInteger, nullable=False)
    iso_3166_code = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    # authors = db.relationship("Authors", backref="affiliation")


class Papers(db.Model):
    __tablename__ = "papers"

    id = db.Column(db.BigInteger, primary_key=True)
    rank = db.Column(db.BigInteger, nullable=False)
    doi = db.Column(db.Text, nullable=False)
    doc_type = db.Column(db.Text, nullable=False)
    paper_title = db.Column(db.Text, nullable=False)
    original_title = db.Column(db.Text, nullable=False)
    # book_title = db.Column(db.Text, nullable=False)
    # year = db.Column(db.Integer, nullable=False)
    # date = db.Column(db.DateTime, nullable=False)
    # online_date = db.Column(db.DateTime, nullable=False)
    # publisher = db.Column(db.Text, nullable=False)
    # journal_id = db.Column(db.Text, nullable=False)
    # conference_series_id = db.Column(db.Text, nullable=False)
    # conference_instance_id = db.Column(db.Text, nullable=False)
    # volume = db.Column(db.Text, nullable=False)
    # issue = db.Column(db.Text, nullable=False)
    # first_page = db.Column(db.Text, nullable=False)
    # lase_page = db.Column(db.Text, nullable=False)
    # reference_count = db.Column(db.BigInteger, nullable=False)
    # citation_count = db.Column(db.BigInteger, nullable=False)
    # estimated_citation = db.Column(db.BigInteger, nullable=False)
    # original_venue = db.Column(db.Text, nullable=False)
    # family_id = db.Column(db.BigInteger, nullable=False)
    # family_rank = db.Column(db.BigInteger, nullable=False)
    # doc_sub_types = db.Column(db.Text, nullable=False)
    # created_date = db.Column(db.DateTime, nullable=False)

    # authors = db.relationship("Authors", secondary="paper_author_affiliations", backref="paper")


class PaperAuthorAffiliations(db.Model):
    __titlename__ = "paper_author_affiliations"

    id = db.Column(db.Integer, primary_key=True)
    paper_id = db.Column(db.BigInteger, nullable=False)
    author_id = db.Column(db.BigInteger, nullable=False)
    # paper_id = db.Column(db.BigInteger, db.ForeignKey("papers.id"))
    # author_id = db.Column(db.BigInteger, db.ForeignKey("authors.id"))
    affiliation_id = db.Column(db.BigInteger, nullable=False)
    author_sequence_number = db.Column(db.BigInteger, nullable=False)
    original_author = db.Column(db.Text, nullable=False)
    origunal_affiliation = db.Column(db.Text, nullable=False)


class PaperReferences(db.Model):
    __titlename__ = "paper_references"

    paper_id = db.Column(db.BigInteger, primary_key=True)
    paper_reference_id = db.Column(db.BigInteger, primary_key=True)

    # paper_id = db.Column(db.BigInteger, db.ForeignKey("papers.id"), primary_key=True)
    # paper_reference_id = db.Column(db.BigInteger, db.ForeignKey("papers.id"), primary_key=True)


class UserInputs(db.Model):
    __titlename = "user_inputs"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)


class UserInputss(db.Model):
    __titlename = "user_inputss"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)


# db.drop_all()
# db.create_all()
# print("DB created successfully")


"""
Backend
"""


def todo_serializer(serializer):
    return {
        'id': serializer[0],
        'paper_id': serializer[0],
        'paper_num': serializer[1]
    }


@app.route('/paper', methods=['GET'])
def get_top_cited_papers():
    input_db = UserInputs.query.all()
    for i in input_db:
        author = int(i.content)
    print("author:", author)
    # author = 332443050
    # author = 44880
    # author = 222893
    # db.session.delete(UserInputs.query.get(1))
    # db.session.commit()

    papers_id_ls = []
    references_dict = {}
    reference_id_top = []
    res = []
    papers_db = PaperAuthorAffiliations.query.filter_by(author_id=author).all()
    # print(papers_db)
    """Get all papers that wrote by the author"""
    for i in papers_db:
        paper_id = i.paper_id
        papers_id_ls.append(paper_id)
        # print(paper_id)

    """Get all references that the author used, saved them to a dictionary by frequency"""
    for i in papers_id_ls:
        paper_references_db = PaperReferences.query.filter_by(paper_id=i).all()
        # print(paper_references_db)
        for j in paper_references_db:
            reference_id = j.paper_reference_id
            # print(reference_id)
            if reference_id in references_dict:
                references_dict[reference_id] += 1
            else:
                references_dict[reference_id] = 1
    # print(references_dict)

    references_dict_sorted = sorted(references_dict.items(), key=lambda x: x[1], reverse=True)
    print("references_dict_sorted", references_dict_sorted)
    """Output TOP 5"""
    count = 0
    for i in range(len(references_dict_sorted)):
        if count == 5:
            break
        reference_id_top.append(references_dict_sorted[i])
        count += 1
        # print(references_dict_sorted[i][0])
    print("reference_id_top", reference_id_top)
    if len(references_dict_sorted) >= 1:
        return jsonify(*map(todo_serializer, reference_id_top))
    else:
        return jsonify(*map(todo_serializer, ["NN", "NN"]))


@app.route('/paper/submit', methods=['POST'])
def submit():
    request_data = json.loads(request.data)
    try:
        id = int(request_data["content"])
    except:
        print("Type Error")
    op = False
    check_db = Authors.query.filter_by(id=id).all()
    for i in check_db:
        if i.id == id:
            op = True
            break
    if op:
        print("submitted correctly")
        db.session.add(UserInputs(content=request_data['content']))
        db.session.commit()

    print(id)
    return jsonify(request_data)


def todo_serializer2(serializer):
    return {
        'id': serializer[0],
        'affiliation_id': serializer[0],
        'affiliation_amount': serializer[1]
    }


@app.route('/affiliation', methods=['GET'])
def get_top_affiliation():
    print("search start")
    # affiliation = 6902469 81365321
    input_db = UserInputss.query.all()
    for i in input_db:
        affiliation = int(i.content)
    print("affiliation:", affiliation)

    authors_db = Authors.query.filter_by(last_know_affiliation_id=affiliation).all()
    authors_ls = []
    papers_ls = []
    coauthors_ls = []
    affiliation_ls = []
    affiliation_dict = {}
    topaffiliation_ls = []

    """get authors which is associated with the input affiliation"""
    for i in authors_db:
        authors_ls.append(i.id)
    print(authors_ls)

    """get papers which is written by these authors"""
    count1 = 0
    for i in authors_ls:
        if count1 >= 10:
            break
        papers_db = PaperAuthorAffiliations.query.filter_by(author_id=i).all()
        for j in papers_db:
            papers_ls.append(j.paper_id)
        count1 += 1
    print(papers_ls)

    """get co authors which is associated with the these papers"""
    count2 = 0
    for i in papers_ls:
        if count2 >= 10:
            break
        coauthors_db = PaperAuthorAffiliations.query.filter_by(paper_id=i).all()
        for j in coauthors_db:
            coauthors_ls.append(j.author_id)
        count2 += 1
    print(coauthors_ls)

    """get affiliations which contain these co authors"""
    for i in coauthors_ls:
        affiliations_db = Authors.query.filter_by(id=i).all()
        for j in affiliations_db:
            affiliation_ls.append(j.last_know_affiliation_id)
    # print(affiliation_ls)

    """get a dictionary of the affiliations, count frequency"""
    for i in affiliation_ls:
        if i in affiliation_dict:
            affiliation_dict[i] += 1
        else:
            affiliation_dict[i] = 1
    affiliation_dict.pop(-1, None)  # remove the affiliations which are not recorded
    affiliation_dict_sorted = sorted(affiliation_dict.items(), key=lambda x: x[1], reverse=True)
    print(affiliation_dict_sorted)
    print("search completed")

    return jsonify(*map(todo_serializer2, affiliation_dict_sorted))


@app.route('/affiliation/submit', methods=['POST'])
def submitt():
    request_data = json.loads(request.data)
    try:
        id = int(request_data["content"])
    except:
        print("Type Error")
    op = False
    check_db = Authors.query.filter_by(last_know_affiliation_id=id).all()
    for i in check_db:
        if i.last_know_affiliation_id == id:
            op = True
            break
    if op:
        print("submitted correctly")
        db.session.add(UserInputss(content=request_data['content']))
        db.session.commit()

    print(id)
    return jsonify(request_data)


if __name__ == '__main__':
    app.run(debug=True)
