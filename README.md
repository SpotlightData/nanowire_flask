Nanowire flask
==============
This library is designed to allow a python developer to easily create a nanowire plugin using the flask APIs structure.

The function you mount for image plugins, using the function ``mount_Image_function``  must have the arguments ``img`` and ``variables`` if you want initialise a model or other variables when the sever starts you may make the function to be mounted into a function of a 
class which is initiated with the function ``mount_Image_function``. You should expect ``img`` to be a PIL RGB image object and ``variables`` to be a dictionary containing the variables sent to the plugin in the curl request.

The function for mounting a text based plugin is similar however it is called ``mount_text_function`` and expects the arguments ``text`` (a string) and ``variables``.

The curl requests for images may be formatted 2 ways. The first involves sending the image as a file attached to the curl request. For example:

``curl -F "image=@./1.jpg" -XPOST http://0.0.0.0:5000/model/predict?threshold=0.5``

alternatively the file may be sent as a link using a dictionary eg.

``curl -X POST -H "Content-Type:application/json" -d '{"contentUrl":"http://127.0.0.1:8000/1.jpg", "threshold":0.5}' http://0.0.0.0:5000/model/predict``

The currently supported image formats are:

* jpg
* png
* bmp
* tif
* ppm

The curl request for text is similar to that used for images except that it may take either raw text or a file containing raw text. You may either post a document containing the raw text using the command

``curl -F "doc=@./doc1.txt" -XPOST http://0.0.0.0:5000/model/predict?deactivate_ngrams=True``

or the raw text can be sent using:

``curl -X POST -H "Content-Type:application/json" -d '{"text":"Example text about whichever subject you're interested in", "deactivate_ngrams"="True"}' http://0.0.0.0:5000/model/predict``

The library may also accept CSV objects using command like

``curl -F "csv=@./example.csv" -XPOST http://0.0.0.0:5000/model/predict?ignore_col=text``

a xlsx file may be sent in the same way:

``curl -F "xlsx=@./example.xlsx" -XPOST http://0.0.0.0:5000/model/predict?ignore_col=text``

alternativly a link to a csv or xlsx file may be sent such as:

``curl -X POST -H "Content-Type:application/json" -d '{"contentUrl":"http://localhost:8000/example.csv", "ignore_col":"dates"}' http://0.0.0.0:5000/model/predict``

The library may also accept JSON objects using commands such as

``curl -X POST -H "Content-Type:application/json" -d '{"this":"is", "an":"example"}' http://0.0.0.0:5000/model/predict``

alternativly a csv file may be sent from a server

``curl -X POST -H "Content-Type:application/json" -d '{"contentUrl":"http://localhost:8000/example.json"}' http://0.0.0.0:5000/model/predict``

This library will eventually be expanded to be able to handle video, sound and arbitary files however for now it is limited to text, images, csv files and json files.

The API you create will also return maximum memory usage (in MB), maximum cpu usage (in %) and time taken (in seconds) when processing a given API call.

Notes for advanced users
------------------------

**image_tools.mount_Image_function**

*Parameters* 

* *function* :- The function to be mounted on the API. The function must take img and variables as arguments when processing images. The function must return a dictionary. 
* *host* :sup:`optional`:- default is '0.0.0.0'. Set the IP address to host the API on.
* *port* :sup:`optional`:- default 5000. Set the port to host the API on.
* *path* :sup:`optional`:- default '/model/predict'. Set the path for the API.

**text_tools.mount_text_function**

*Parameters*
* *function* :- The function to be mounted on the API. The function must take text and variables as arguments when processing text. The function must return a dictionary. 
* *host* :sup:`optional`:- default is '0.0.0.0'. Set the IP address to host the API on.
* *port* :sup:`optional`:- default 5000. Set the port to host the API on.
* *path* :sup:`optional`:- default '/model/predict'. Set the path for the API.

**csv_tools.mount_csv_function**

*Parameters*
* *function* :- The function to be mounted on the API. The function must take df (a pandas dataframe) and variables (a dictionary) as arguments when processing a csv. The function must return a dictionary. 
* *host* :sup:`optional`:- default is '0.0.0.0'. Set the IP address to host the API on.
* *port* :sup:`optional`:- default 5000. Set the port to host the API on.
* *path* :sup:`optional`:- default '/model/predict'. Set the path for the API.


**json_tools.mount_json_function**

*Parameters*
* *function* :- The function to be mounted on the API. The function must take inputJSON as an argument. The function must return a dictionary. 
* *host* :sup:`optional`:- default is '0.0.0.0'. Set the IP address to host the API on.
* *port* :sup:`optional`:- default 5000. Set the port to host the API on.
* *path* :sup:`optional`:- default '/model/predict'. Set the path for the API.


**Notes on debug mode**

In order to activate debug mode the environmental variable `PYTHON_DEBUG` must be set to true.

Debug mode will mean that any errors encountered whilst running the function will also give a full traceback of the error in the returned JSON.

**Notes on taskID**

If the post contains ``taskID`` as an argument the taskID given will also be returned in the output JSON.
