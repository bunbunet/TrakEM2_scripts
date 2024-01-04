from ini.trakem2.display import Display
  
def sortNodesByTags(tree):
  table = {}
  root = tree.getRoot()
  if root is None:
    return table # empty
  #
  for nd in tree.getRoot().getSubtreeNodes():
    tags = nd.getTags()
    if tags is None:
      continue
    for tag in tags:
      tagged = None
      if table.has_key(tag):
        tagged = table[tag]
      else:
        tagged = []  
        table[tag] = tagged
      tagged.append(nd)
  #
  return table
  
# Obtain the currently selected Tree in the canvas:
tree = Display.getFront().getActive()
  
# Print the number of nodes that have any given tag:
for tag, tagged in sortNodesByTags(tree).iteritems():
  print "Nodes for tag '" + str(tag) + "':", len(tagged)