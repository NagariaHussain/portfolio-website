# For creating a slug string
def slugify_title(title: str) -> str:
    '''returns a sluggified version of the given `title`'''
    slugged_title = ""
    for c in title:
        if c.isalnum():
            slugged_title += c.lower()
        if c.isspace():
            slugged_title += '-'

    return slugged_title

# For sorting blogs by creation date
sort_blog_by_cd_lambda = lambda x:x["meta_data"]["creation_date"]