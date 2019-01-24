# Nanowire flask

This library is designed to allow a python developer to easily create a nanowire plugin using the flask APIs structure.

The function you mount, using the class ImagesAPI, must have the arguments <code>img</code> and <code>variables</code> if you want initialise a model or other variables when the sever starts you may make the function to be mounted into a function of a class which is initiated with the desired variables. In this case your variables will be <code>self</code>, <code>img</code> and <code>variables</code>.
You should expect <code>img</code> to be a PIL RGB image object and <code>variables</code> to be a dictionary containing the variables sent to the plugin in the curl request.

The curl requests for images may be formatted 2 ways. The first involves sending the image as a file attached to the curl request. For example:

<code>curl -F "image=@./1.jpg" -XPOST http://0.0.0.0:5000/model/predict?threshold=0.5</code>

alternativly the file may be sent as a link using a dictionary eg.

<code>curl -X POST -H "Content-Type:application/json" -d '{"contentURL":"http://127.0.0.1:8000/1.jpg", "threshold":0.5}' http://0.0.0.0:5000/model/predict</code>


At the moment it can only handle images however it will soon be expanded to handle text and eventually video and sound. The currently supported image formats are:

* jpg
* png
* bmp
* tif
* ppm
