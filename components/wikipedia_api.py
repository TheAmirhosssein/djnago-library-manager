import wikipedia


def find_jpg(image_list: list):
    selected_image = ""
    for image in image_list:
        if not "svg" in image:
            selected_image = image
            break
    return selected_image


def get_wikipedia_page(name, lang="fa"):
    wikipedia.set_lang(lang)
    page = wikipedia.page(name)
    page_info = {
        "title": page.title,
        "summery": page.summary,
        "picture": find_jpg(page.images),
    }
    return page_info
