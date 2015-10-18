from ImageProcessing import image_functions as img_fun
import includes

def extract_posts_with_large_images(posts, min_width, min_height, number_large_images):
    valid_posts = []
    for post in posts:
        # From each subpost select a big picture and break
        for subposts in post:
            img_data = img_fun.return_image_dimensions(subposts['iurl'])
            if img_data['width'] >= min_width and img_data['height'] >= min_height:
                valid_posts += [subposts]
                break
        # If we have images we want we break
        if len(valid_posts) >= number_large_images:
            break
    return valid_posts

def extract_front_page_images(posts):
    min_width = includes.PARAMETERS["front_page_image"]["width"] - 400
    min_height = includes.PARAMETERS["front_page_image"]["height"] - 300
    number_large_images = includes.PARAMETERS["front_page_image"]["images"]
    return extract_posts_with_large_images(posts, min_width, min_height, number_large_images)

if __name__ == '__main__':
    def test_extract_posts_with_large_images():
        import json, includes
        posts = json.loads(file('../../Assets/posts.json').read())
        min_width = includes.PARAMETERS["front_page_image"]["width"]
        min_height = includes.PARAMETERS["front_page_image"]["height"]
        number_large_images = includes.PARAMETERS["front_page_image"]["images"]
        print extract_posts_with_large_images(posts, min_width, min_height, number_large_images)
    test_extract_posts_with_large_images()