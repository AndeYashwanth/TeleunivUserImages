<ol><li>run teleuniv_images_download.py(require username and password for teleuniv.net) which downloads the images with id's in given range.
Not every image is valid(doesn't contain face in it).</li>
<li><b>Multithreading</b> is used during download of images to max out bandwidth available, otherwise images are downloaded one by one.</li>
<li>run teleuniv_users_opencv_face_detection.py to keep the images containing only faces and remove others using <b>opencv</b> and haarcascade.</li>
</ol>
<br>
<ul><li>teleuniv_user_details is just to create a mapping of user image id(which we used to download images) and actual rollno(some are not valid which will be stored as temprollno) in myslql table.</li>
    <li>This will be created using the html files downloaded manually from the course website.</li>
    <li>There was a get parameter in the url of the downloaded html pages which tells how many users to display.</li>
    <li>Also there was a count of how many users are registered. So I changed the get parameter to the count and got all the users and saved the html file.</li>
</ul>
