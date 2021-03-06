db.election.title.default = 'Election title'

db.election.ballot_model.default = """
<h2>Election Title</h2>

<p>This is a ballot!</p>

<table>
<tr><td>Candidate 1</td><td>{{0}}</td></tr>
<tr><td>Candidate 2</td><td>{{0}}</td></tr>
<tr><td>Candidate 3</td><td>{{0}}</td></tr>
</table>

<p>or</p>

<table>
<tr><td>Candidate 1</td><td>{{1}} yes</td><td>{{1}} no</td><td>{{1!}} abstain</td></tr>
<tr><td>Candidate 2</td><td>{{2}} yes</td><td>{{2}} no</td><td>{{2!}} abstain</td></tr>
<tr><td>Candidate 3</td><td>{{3}} yes</td><td>{{3}} no</td><td>{{3!}} abstain</td></tr>
</table>
"""

db.election.vote_email.default = """
{{=title}}

Link to vote: {{=link}}

"""

db.election.voted_email.default = """
{{=title}}

Your ballot: {{=link}}

{{=signature}}
(your voted was recorded, your ballot is also attached)

"""

db.election.not_voted_email.default = """
{{=title}}

Your ballot: {{=link}}

{{=signature}}
(you did not vote, your BLANK ballot is also attached)
"""

def message_replace(message,**vars):
    for key in vars:
        message = message.replace('{{=%s}}' %key,vars[key])
    return message
