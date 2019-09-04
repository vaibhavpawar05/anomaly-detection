### email subject

Mining categories for emails via clustering and pattern discovery
http://ccc.inaoep.mx/~villasen/bib/Mining%20categories%20for%20emails%20via%20clustering.pdf
Section - 5. Updating clusters talks about creating and maintaining clusters

**pre-processing**
- do NER
- replace date mentions with DATE
- <>

**topic model based approach**
- create topic model
- take topics with a contribution greater than a threshold
- score new emails
- monitor quality
- if quality drop reaches a threshold
  - rerun the topic modeling - this will require rebuilding a part of the graph

**bag of words type**
- identify key-words and key-phrases
  - client names, DATE, info type
  - cluster similar key-words and key-phrases
- create nodes for the above information
- does not require rebuilding of the graph

Idea: Date and Time Parsing · Issue #513 · explosion/spaCy · GitHub
https://github.com/explosion/spaCy/issues/513

Natty Date Parser
http://natty.joestelmach.com/doc.jsp

dateutils
datefinder
