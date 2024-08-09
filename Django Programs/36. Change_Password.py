
Change Password In Project:

As in every project using change password page system user can change password, so in our project add one new menu as Change Password and on click to change password menu open new web page, using will change current password to new password as:

            <li class="sidebar-item">
                <a
                  class="sidebar-link waves-effect waves-dark sidebar-link"
                  href="{% url 'change_password' %}"
                  aria-expanded="false"
                  ><i class="mdi mdi-border-inside"></i
                  ><span class="hide-menu">Change Password</span></a
                >
              </li>

# as on click to change password menu, we are expecting new web page so again new path, new function and new web page we required.

# In urls.py
path('change_password/', views.change_password, name='change_password'),

# In views.py
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        
        
        user = User.objects.get(username=request.user.username)
        if not user.check_password(current_password):
            messages.error(request, "Current password is incorrect.")
            return redirect('/change_password/')
        
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Your password was successfully updated!')
        return redirect('/change_password/')
    
    return render(request, 'dashboard/change_password.html')

# and In change_password.html web page:

   <section class="ftco-section ftco-no-pt ftco-no-pb contact-section">
                <div class="container">
                  <div class="row d-flex align-items-stretch no-gutters">
                    
                    <center>

                      {% for x in messages %}
        
                      <h5> 
                          
                        <div id="myAlert" class="alert alert-warning alert-dismissible fade show" role="alert">
                          <strong style="color:green;">{{x}}</strong>
                          <button type="button" class="close" data-bs-dismiss="alert" aria-label="Close">
                              <span aria-hidden="true">&times;</span>
                          </button>
                      </div>
                      
                      <script>
                          // Function to dismiss the alert after a specified duration
                          function dismissAlert() {
                              var alertDiv = document.getElementById('myAlert');
                              if (alertDiv) {
                                  alertDiv.classList.add('fade');
                                  setTimeout(function() {
                                      alertDiv.style.display = 'none';
                                  }, 1000); // Change 1000 to the desired duration in milliseconds (e.g., 3000 for 3 seconds)
                              }
                          }
                      
                          // Automatically dismiss the alert after 3 seconds (adjust the time as needed)
                          setTimeout(dismissAlert, 3000); // 3000 milliseconds = 3 seconds
                      </script>
                      
                                          
                      </h5>
        
                      {% endfor %}
        
                    </center>
                    
                    <div class="col-md-6 p-4 p-md-5 order-md-last bg-light">
                      
                     
                      <form action="{% url 'change_password' %}" method="POST" >
                        
                        {% csrf_token %}
              
                        <div class="form-group">
                          <input type="text" class="form-control" name="current_password"  placeholder="Enter Current Password" required>
                        </div>

                        <div class="form-group">
                          <input type="text" class="form-control" name="new_password"  placeholder="Enter New Password" required>
                        </div>

                        <div class="form-group">
                          <input type="text" class="form-control" name="confirm_password"  placeholder="Enter Confirm Password" required>
                        </div>
                       
                        <div class="form-group">
                          <input type="submit" value="Submit" class="btn btn-primary py-3 px-5" name="submit">
                        </div>
                      </form>

                      
                    </div>
                  
                  </div>

                </div>
              </section>