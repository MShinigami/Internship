Admin Master Page:

# Using Master Page we can fetch drop down values in form as Services Names, Designations, 
# Financial Years, anything which you want to fetch data in dropdown those values should be fetch from master table

# Now in HTML form we need to add dropdown option for selecting data
# Adding static data in dropdown:
<div class="form-group">
              <select class="form-control">

                <option> --Select Option-- </option>
                
                <option value="Option1"> Option1 </option>
                <option value="Option2"> Option2 </option>
                <option value="Option3"> Option3 </option>
                
              </select>
</div>


# Above dropdown is static data, but we need to fetch data from table, so we need to create one table in models.py for storing locations through admin and these locations only we are going to fetch in .html form:

step 1) In models.py create new table for storing locations as:

class DropdownOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# save file and run py manage.py makemigrations and py manage.py migrate command on terminal

# and don't forget to register this new table in admin.py

admin.site.register(DropdownOption)

# Now you can check new table is created in django administration.

step 2) Now in admin login, add new Menu as Master Page and have some sub menus as add location, add services, add designation etc. (In design already menu sub menu option is available just un-comment and change menu names)

on click to add location sub menu, new page should be open and from where we can add new location which should be insert into this new table DropdownOption (table name)

# so again three things we need to do here, create path() in urls.py, create function() in views.py and have web page in templates/dashboard folder

urls.py:
path('add_location/', views.add_location, name='add_location'),

views.py:
def add_location(request):
    
    if request.method == 'POST':
        a = request.POST.get('name')

        info = DropdownOption(name = a)
        info.save()

    return render(request, 'dashboard/add_location.html')

templates/dashboard - in folder

copy and paste any web page of dashboard folder and just keep one input for taking location and submit.

In add_location.html page:

<form action="{% url 'add_location' %}" method="POST" >
                        
          {% csrf_token %}
  
          <div class="form-group">
            <input type="text" class="form-control" name="name"  placeholder="Enter New Location" required>
          </div>
          
          <div class="form-group">
            <input type="submit" value="Submit" class="btn btn-primary py-3 px-5" name="submit">
          </div>
</form>

# Now you can check in django administration, Locations are storing now.

step 3) Now needs to fetch records which we stores in table then only user will understand which previous records we added.

so on same add_location.html page need to show table records as:          

            




















path('add-location/', views.add_location, name ='add_location'),

# and function in views.py as:

def add_location(request):
    if request.method=='POST':
      location = request.post.get('location')

      data = enquiry_table(location = location)
      data.save()
      messages.success(request, 'New Location added Successfully...')

    return render(request, 'dashboard/form-basic.html')

# Now using tamplates tags we need to fetch .css and .js and .jpg files access
href="{% static "path_of_css_or_js_or_jpg" %}"

# Now once page is showing on browser with css and js then which content you required keep those code only from that form-basic.html file other not required data we can comment.

# Just we need to keep only one input required for adding location input and submit button in this new page.

add name="location" attribute to 

<form action="{% url 'add_location' %}" method="POST" >

 <input type="text" name="location" required> tag if not available.
 <input type="submit" value="Submit" class="btn btn-primary py-3 px-5" name="submit">

</form>






