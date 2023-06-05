#Priority list

#describe your situation widget
#Social media link icons are also being replaced
# find better templates
#error handling, images not found


# make sure you delete the lib and


"""

Better email templates : https://unlayer.com/templates

Initially do around 10 repeating email templates then gradually expand

1)https://dashboard.unlayer.com/create/subscription-is-expiring-soon?_gl=1*9hz7j5*_ga*ODk5OTkxNjUzLjE2ODQ1OTg3NzM.*_ga_VMP9QH8KW8*MTY4NDY4NTAyOC4yLjEuMTY4NDY4NzY0OC40Mi4wLjA.
2)https://dashboard.unlayer.com/create/simple-offer?_gl=1*1etqsw6*_ga*ODk5OTkxNjUzLjE2ODQ1OTg3NzM.*_ga_VMP9QH8KW8*MTY4NDY4NTAyOC4yLjEuMTY4NDY4Nzc5NS42MC4wLjA.
3)https://dashboard.unlayer.com/create/online-healthcare?_gl=1*1wtwh93*_ga*ODk5OTkxNjUzLjE2ODQ1OTg3NzM.*_ga_VMP9QH8KW8*MTY4NDY4NTAyOC4yLjEuMTY4NDY4Nzg0NS4xMC4wLjA.
4)https://dashboard.unlayer.com/create/fitness-communication?_gl=1*2esirk*_ga*ODk5OTkxNjUzLjE2ODQ1OTg3NzM.*_ga_VMP9QH8KW8*MTY4NDY4NTAyOC4yLjEuMTY4NDY4Nzg5MS4yNS4wLjA.
5)https://dashboard.unlayer.com/create/furniture-single?_gl=1*30tv8*_ga*ODk5OTkxNjUzLjE2ODQ1OTg3NzM.*_ga_VMP9QH8KW8*MTY4NDY4NTAyOC4yLjEuMTY4NDY4NzkzNi41OS4wLjA.
6)https://dashboard.unlayer.com/create/industry-conference?_gl=1*14f9hmp*_ga*ODk5OTkxNjUzLjE2ODQ1OTg3NzM.*_ga_VMP9QH8KW8*MTY4NDY4NTAyOC4yLjEuMTY4NDY4Nzk0MS41NC4wLjA.
7)https://dashboard.unlayer.com/create/reward-free-giveaway?_gl=1*bs0086*_ga*ODk5OTkxNjUzLjE2ODQ1OTg3NzM.*_ga_VMP9QH8KW8*MTY4NDY4NTAyOC4yLjEuMTY4NDY4ODAxMy41OC4wLjA.
8)https://dashboard.unlayer.com/create/green-sale?_gl=1*xoyrny*_ga*ODk5OTkxNjUzLjE2ODQ1OTg3NzM.*_ga_VMP9QH8KW8*MTY4NDY4NTAyOC4yLjEuMTY4NDY4ODAxNS41Ni4wLjA.
9)https://dashboard.unlayer.com/create/cyber-monday-sale?_gl=1*4ckeyw*_ga*ODk5OTkxNjUzLjE2ODQ1OTg3NzM.*_ga_VMP9QH8KW8*MTY4NDY4NTAyOC4yLjEuMTY4NDY4ODEzOS4xMS4wLjA.
10)https://dashboard.unlayer.com/create/free-shipping-offer?_gl=1*ot3gth*_ga*ODk5OTkxNjUzLjE2ODQ1OTg3NzM.*_ga_VMP9QH8KW8*MTY4NDY4NTAyOC4yLjEuMTY4NDY4ODE0MS45LjAuMA..
"""

import os
import random
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup, Comment
import openai
import subprocess
import json
import unicodedata
from mangum import Mangum
from fastapi.responses import FileResponse

openai.api_key =
os.environ["OPENAI_API_KEY"] = 

app = FastAPI()
handler = Mangum(app)

"""
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost/",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""
# Your remaining code goes here...



def retreive_data_format(path):
    with open(path, 'r') as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    # List of tags to exclude
    blacklist = [
        '[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script', 'style'
    ]

    # Find all tags in the HTML that contain text
    tags = soup.find_all(string=True)

    # Join all text together with the name of the tag and class attributes in between each piece of text,
    # excluding the tags in the blacklist and comments
    result = "".join(
        f'<{tag.parent.name} class="{ " ".join(tag.parent.get("class", [])) }">{tag.strip()}</{tag.parent.name}>'
        for tag in tags
        if tag.parent.name not in blacklist and not isinstance(tag, Comment) and tag.strip()
    )

    return result

#change the text content:



def change_text_content(content,theme,context_of_user):
    # Note: you need to be using OpenAI Python v0.27.0 for the code below to work

    completion = openai.ChatCompletion.create(
     model = "gpt-4",
     temperature = 0.5,
     max_tokens = 2000,

        messages=[
            { "role": "user", "content":   "Revise HTML content within tags to match the theme:"+ theme+". Consider this user story:"+context_of_user + "consider this the html context:"+content }
        ]
    )
    return completion.choices[0].message.content



def replace_html_content(modified_representation, html_file_path):
    # Parse the modified representation into individual tags
    soup_modified = BeautifulSoup(modified_representation, 'html.parser')
    tags_modified = soup_modified.find_all()

    # Open the original HTML file and parse it
    with open(html_file_path, 'r') as f:
        html_doc = f.read()

    soup_original = BeautifulSoup(html_doc, 'html.parser')

    # Initialize a counter
    counter = 0

    # List of tags to exclude, to match the retreive_data_format function
    blacklist = [
        '[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script', 'style'
    ]

    # Replace the text content of the tags in the original HTML with the new text
    for tag in soup_original.find_all(string=True):
        if tag.parent.name not in blacklist and not isinstance(tag, Comment) and tag.strip():
            tag.replace_with(tags_modified[counter].string)
            counter += 1

    # Save the changes to a new HTML file
    with open(html_file_path, 'w') as f:
        f.write(str(soup_original.prettify()))

    print(f"New file saved as {html_file_path}")

"""
path_website = '/Users/macos/PycharmProjects/Botify/holi/(85).htm' #actual website
text_representation = retreive_data_format(path_website)
new_representation = change_text_content(text_representation,'dragons')

print("Initial Text Representation:"+text_representation)

print('\n')

replace_html_content(new_representation,path_website)
print("Final text representation:"+retreive_data_format('/Users/macos/PycharmProjects/Botify/Email_template_generation/new_'))#modified website
"""

######################### Modifying the text task finished.##############################################


########modifying Images#############
ACCESS_KEY = 

def find_images(prompt, num_images):
    curl_url = 'curl -H "Authorization: tpYdnkkK4BXFoIgCPy7TZrOFazhAF4iUypjyUWPIxUuMXdO6TJAh7kfi" \"https://api.pexels.com/v1/search?query={}&per_page={}"'.format(prompt, num_images)
    status, data = subprocess.getstatusoutput(curl_url)

    start = data.find('{')
    end = data.rfind('}') + 1
    json_data = data[start:end]

    if not json_data:
        print(f"Warning: No data received for prompt: {prompt}")
        return None

    # Remove control characters
    json_data = ''.join(ch for ch in json_data if unicodedata.category(ch)[0] != "C")

    try:
        parsed_data = json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return None

    # Iterate over each photo in the 'photos' list
    all_urls = []
    for photo in parsed_data['photos']:
        # Get the URL of the 'original' version of the photo
        url = photo['src']['original']
        all_urls.append(url)
        print(f"appending {url}")
    return all_urls


def find_and_download_images(prompt):
    image_url = find_images(prompt)
    if not image_url:
        print(f"No image URL found for prompt: {prompt}")
        return

    response = requests.get(image_url, stream=True)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return

    filename = os.path.basename(image_url)

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(8192):
            file.write(chunk)
#array = find_images('china',5)
#print(array)

def count_image_tags(file):
    with open(file, 'r') as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content, 'html.parser')
    return len(soup.find_all('img'))


def replace_image_src(file, new_urls,theme):
    with open(file, 'r') as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content, 'html.parser')
    images = soup.find_all('img')

    if len(images) != len(new_urls):
        print("The number of new URLs doesn't match the number of images in the HTML file.")
        return

    for img, new_url in zip(images, new_urls):
        img['src'] = new_url

    html = soup.prettify("utf-8")

    # Define the new file path. This will create a new HTML file in the current working directory.
    new_file_path = theme+'.html'
    with open(new_file_path, "wb") as file:
        file.write(html)

    return new_file_path

# example usage


#'/Users/macos/PycharmProjects/Botify/holi/(85).htm'

def find_email_template_template(directory_of_email_template_folder):
    # Get a list of all files in the directory
    files = os.listdir(directory_of_email_template_folder)

    # Randomly select a file
    random_file = random.choice(files)

    # Return the full path of the file
    return os.path.join(directory_of_email_template_folder, random_file)




def generate_email_templates(theme,user_story):
    email_template_template = find_email_template_template('Templates')

    print(email_template_template)
    theme_of_user = theme

    count = count_image_tags(email_template_template)
    array = find_images(theme_of_user,count)
    random.shuffle(array)

    path_of_website_replaced_images = replace_image_src(email_template_template, array,theme_of_user)#actual website
    text_representation = retreive_data_format(path_of_website_replaced_images)
    new_representation = change_text_content(text_representation,theme_of_user,user_story)

    print("Initial Text Representation:"+text_representation)

    print('\n')

    replace_html_content(new_representation,path_of_website_replaced_images)
    print("Final text representation:"+retreive_data_format(path_of_website_replaced_images))#modified website
    return path_of_website_replaced_images




@app.get("/")
def read_root():
    return {"answer": "Hello World"}


@app.get("/predict")
def answergen(input_text,context):
    path = generate_email_templates(input_text,context)
    # Parse the html file
    html_read = open(path,'r')
    soup = BeautifulSoup(html_read, 'html.parser')
    final = soup.prettify()
    # Format the parsed html file

    return {"status" : "process successful",
            "html code" : final
            }

#uvicorn /Users/macos/PycharmProjects/Botify/Email_template_generation/API:app --port 8000 --reload
#def replace_images(path_to_html_file,array_of_image_srcs):

