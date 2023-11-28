import json

# Load animal data from JSON file
def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

# Generate HTML with animal data
output = ''
for animal in animals_data:
    # create a div to hold the animal title
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
    output += f'      <strong>Type:</strong> {animal["characteristics"].get("type", "Unknown")}<br/>\n'
    output += f'      <strong>Diet:</strong> {animal["characteristics"].get("diet", "Unknown")}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'

# Load HTML template from file and replace placeholder with animal data
with open('animals_template.html', 'r') as file:
    html_template = file.read()

html_output = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

# Write the new HTML content to a new file
with open('animals.html', 'w') as file:
    file.write(html_output)
