# Book Image Application

### Main URL(HomePage):

http://django-env.eba-2rgm3iiu.us-west-2.elasticbeanstalk.com/

###Note : 
1) Deployed on AWS EBS
2) Used to upload an image , search an image and delete the image.


### A) Upload Functionality:
1) On the homepage user gets an option of uploading an image along with name. User can browse in his local computer and upload any image. 
2) Upon successful upload user will be able to see the image uploaded on homepage itself.
3) User can upload as much images as he wants.  

### B) Search Functionality:
1) On the homepage there is a search box in which user can enter the book name and then click on search button.
2) The page gets redirected to search url i.e. :

    http://django-env.eba-2rgm3iiu.us-west-2.elasticbeanstalk.com/search

 3) If the book name exist in table it will show the appropriate message and if the book name doesnt exist it will give a message that book doesnt exist in database.
 4) User can choose to go back to homepage as well.
 

### C) Delete Functionaltiy: 
 1) Upon clicking on delete button from search page user is redirected to delete page confirmation i.e.:
 
    http://django-env.eba-2rgm3iiu.us-west-2.elasticbeanstalk.com/delete
    
 2) User have to enter the book name again for confirmation.
 3) After clicking delete the book gets deleted from the database. User can go back and check on the Homepage.
 
 Thank You..