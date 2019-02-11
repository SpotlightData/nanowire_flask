Nanowire flask
==============
This library is designed to allow a python developer to easily create a nanowire plugin using the flask APIs structure.

The function you mount for image plugins, using the class ``ImagesAPI``, must have the arguments ``img`` and ``variables`` if you want initialise a model or other variables when the sever starts you may make the function to be mounted into a function of a class which is initiated with the des$
You should expect ``img`` to be a PIL RGB image object and ``variables`` to be a dictionary containing the variables sent to the plugin in the curl request.

The curl requests for images may be formatted 2 ways. The first involves sending the image as a file attached to the curl request. For example:

``curl -F "image=@./1.jpg" -XPOST http://0.0.0.0:5000/model/predict?threshold=0.5``

alternatively the file may be sent as a link using a dictionary eg.

``curl -X POST -H "Content-Type:application/json" -d '{"contentUrl":"http://127.0.0.1:8000/1.jpg", "threshold":0.5}' http://0.0.0.0:5000/model/predict``


At the moment it can only handle images however it will soon be expanded to handle text and eventually video and sound. The currently supported image formats are:

* jpg
* png
* bmp
* tif
* ppm

The process for text is similar except that you should use the class TextAPI and the function should only use the arguments ``text`` and ``variables``. You may either post a document containing the text using the command

``curl -F "doc=@./doc1.txt" -XPOST http://0.0.0.0:5000/model/predict?deactivate_ngrams=True``


or the raw text can be sent using:

``curl -X POST -H "Content-Type:application/json" -d '{"content":"Example text about whichever subject you're interested in", "deactivate_ngrams"="True"}' http://0.0.0.0:5000/model/predict``


Notes for advanced users
------------------------

**mount_Image_function**

*Parameters* 

* *function* :- The function to be mounted on the API. The function must take img and variable as arguments and return a dictionary 
* *host* :sup:`optional`:- default is '0.0.0.0'. Set the IP address to host the API on
* *port* :sup:`optional`:- default 5000. Set the port to host the API on
* *path* :sup:`optional`:- default '/model/predict'. Set the path for the API

*Notes on debug mode*

In order to activate debug mode the environmental variable `PYTHON_DEBUG` must be set to true.

Activating debug mode will return the maximum memory usage in MB and the maximum CPU usage as a percentage along with the data. This data collection may affect the performance of the plugin so debug mode should be deactivated in production code.
Debug mode will also mean that any errors encountered whilst running the function will also return a full traceback in the returned JSON. Debug mode will also result in the docker container ID being returned in the output JSON.

*Notes of taskID*

If the post contains ``taskID`` as an argument the taskID given will also be returned in the output JSON.
