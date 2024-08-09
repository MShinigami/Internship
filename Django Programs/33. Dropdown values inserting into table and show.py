
On HTML form suppose we want to add one Dropdown for select location, or select gender, etc. for we need to add one new field in <form> using <select> <option value> as:

 <div class="form-group">
              
              <select class="form-control" name="dropdown">
                  <option >-- Select Location --</option>
                
                  <option value="Wakad"> Wakad </option>
                  <option value="Baner"> Baner </option>
                  <option value="Pashan"> Pashan </option>
                
              </select>
</div>

# Now we want to add one more new field in table that is dropdown so we need to create column for dropdown value store,

In models.py create new column for dropdown as:


# Note: already many fields we inserted, so to previous records we need to submit default entries else it will give error.

dropdown = models.CharField(default=None, max_length=100)

Using we are asign none value to previous records, to implement this change we need to run py manage.py makemigrations and py manage.py migrate command

Once column added in table with previous None value then again come to models.py file and remove default=None as:

class enquiry_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    message = models.TextField()
    dropdown = models.CharField(max_length=100)
    date_field = models.DateField(default=date.today)

Now again run makemigrations and migrate command to implement new changes.


# Till now we added one field on <form> and one new column added in table, now on click to submit button new field selection should be inserted into table.

as under name="dropdown" we are taking dropdown value, that we need to insert into table:

def reg(request):
    
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('message')
        e = request.POST.get('dropdown')
        enquiry = enquiry_table(name = a, email = b, phone = c, message = d, dropdown = e)
        enquiry.save()

        messages.success(request, 'Enquiry Form Submitted Successfully...')


    return render(request, 'contact.html')


# Now you can check dropdown selected values storing in table.

Now it's time to fetch selected values where we are showing records, in this example we are fetching records on tables.html page

# add new <th>Location</th>
# and fetch record as:

                    <thead>
                        <tr>
                          <th>Sr. No.</th>
                          <th>Name</th>
                          <th>E-mail Id</th>
                          <th>Mobile</th>
                          <th>Message</th>
                          <th>Location</th>
                          <th>Enquiry Date</th>
                          <th>Edit</th>
                          <th>Delete</th>
                        </tr>
                      </thead>
                      <tbody>
                        
                        {% for x in abc %}
                        <tr>
                        <th scope="row">{{ forloop.counter }}</th>
                        <td>{{ x.name }} </td>
                        <td>{{ x.email }}</td>
                        <td>{{ x.phone }}</td>
                        <td>{{ x.message }}</td>
                        <td>{{ x.dropdown }}</td>
                        <td>{{ x.date_field|date:"d-M-Y" }}</td>


# Now this is what we are storing values in table statically, dropdown values should be dynamic from admin master page, where admin can add values and those values should be shown to front end user through <form>

# So now we see next topic how we can create master page for admin login.

