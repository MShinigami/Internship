

# info = table_name.objects.all()

# data = {'information':info}

# return render(request, 'dashboard/display.html', data)

import json

python_data = {'name': 'ramesh','degree':'Engineering'}

json_data = json.dumps(python_data)

print(json_data)