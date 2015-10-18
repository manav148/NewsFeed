import urllib2, json
import includes, tldextract
key = includes.PARAMETERS["FAROO_KEY"]
faroo_sort_rules = dict(
        has_image_url = True,
        has_url = True,
        no_videos = True,
    )

def get_url_block(block = 1):
    url = "http://www.faroo.com/api?q=&start="+str(1 + 10*(block-1))+"&length="+str(block*10)+"&l=en&src=topics&f=json&key=" + key
    return url

def is_url_header_an_image(url):
    if not url.strip():
        return False
    try:
        resource = urllib2.urlopen(url)
        header = resource.info()
    except Exception:
        return False
    return True if header.subtype.lower() in ["jpeg","png", "gif", "pjpeg", "tiff", "jpg", "svg+xml"] else False

def get_domain_name(url):
    ext = tldextract.extract(url)
    return ext.domain

def faroo_sort_key(article_attributes):
    # sort by weight but also consider faroo sort rules
    weight = int(article_attributes['votes'])
    # Getting all rules which are true in a list comprehension
    for rule in [rule for rule in faroo_sort_rules.keys() if faroo_sort_rules[rule]]:
        if rule == "has_image_url":
            weight *= (1 if article_attributes['iurl'] else 0)
        if rule == "has_url":
            weight *= (1 if article_attributes['url'] else 0)
        if rule == "no_videos":
            weight *= (1 if is_url_header_an_image(article_attributes['iurl']) else 0)
    return weight

def add_domain_names(relavant_topics):
    for topics in relavant_topics:
        for topic in topics:
            topic["domain_name"] = get_domain_name(topic['url'])


def get_faroo_data(no_of_trends = 10, no_of_related_articles=4):
    relavant_topics = []
    blocks = no_of_trends/10
    for block in range(1,blocks+1):
        url = get_url_block(block)
        get_data = urllib2.urlopen(url).read()
        data = json.loads(get_data)
        for topic in data["topics"]:
            # Sort related articles
            topic["related"].sort(key = faroo_sort_key, reverse =True)
            relavant_topics += [topic["related"][:no_of_related_articles]]
        add_domain_names(relavant_topics)
    return relavant_topics

if __name__ == '__main__':
    data = json.dumps(get_faroo_data(20), indent = 4)
    print data
    file('../../Assets/posts.json','w').write(data)