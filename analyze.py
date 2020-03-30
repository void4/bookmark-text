import sys
from json import loads
from collections import defaultdict

bms = defaultdict(list)

with open(sys.argv[1]) as f:
	s = f.read()
	j = loads(s)
	
	for cat in j.get("children", []):
		for b in cat.get("children", []):
			if isinstance(b, dict) and "uri" in b and "dateAdded" in b and "lastModified" in b and "title" in b:
				#print(b)
				bms[b.get("uri", "")].append(b.get("title", ""))
				print(b.get("title", None))



print(len(bms))


from collections import Counter
from urllib.parse import urlparse
from tldextract import extract

allowed_schemes = "http https".split()

bmfile = open("bookmarks.txt", "w+")

uris = []
for uri in bms.keys():
	ext = extract(uri)
	cleaned = ext.registered_domain
	uris.append(cleaned)
	bmfile.write(uri+"\n")

c = Counter(uris)

print(c.most_common(1000))

bmfile.close()
