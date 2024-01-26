from main import session
from tables import Comment

def retrive_comment(data):
    comments = session.query(Comment).filter_by(dishes_id=data['dishes_id']).all()
    comment_json={}
    for comment in comments:
        if comment.author.username not in comment_json:
            comment_json[comment.author.id] = {}
            comment_json[comment.author.id]["comments"] = comment.comment
            comment_json[comment.author.id]["rating"] = comment.rating
            comment_json[comment.author.id]["username"] = comment.author.username
        
    return comment_json