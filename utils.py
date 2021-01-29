def slugify_title(title: str) -> str:
    '''returns a sluggified version of the given `title`'''
    slugged_title = ""
    for c in title:
        if c.isalnum():
            slugged_title += c.lower()
        if c.isspace():
            slugged_title += '-'

    return slugged_title