Nanowire flask
==============

This library is designed to allow a python developer to easily create a Nanowire plugin using the Flask APIs structure.

The library contains a number of functions for mounting processing tools for text, images, spreadsheets and data stored in JSON format onto an API running from a Docker container. 

Each of these functions will validate the format of the data sent by the user, convert it into a 'pythonic' formated object and feed it to the developer's mounted function. Once the developer's function has run the library will validate that a JSON object has been returned and then forward the returned JSON object to the user along with a series of usage statistics, time taken, API version info, memory usage, CPU usage, status and the container ID and image name of the Docker container the API is running from.

We will start by discussing the function for mounting a text based plugin, ``mount_text_function``. This function expects the arguments ``text`` (a string) and ``variables`` a dictionary which defines the optional variables to send to the function. 

A full description of how to develop Nanowire plugins can be found on the [Spotlight Data Confluence pages](https://spotlightdata.atlassian.net/wiki/spaces/NDA/pages/1078951937/Nanowire+flask) complite with worked examples however this page will focus on using Nanowire plugins as a user, starting with a description of how a user may send a piece of text to a Nanowire flask plugin.

### Text ###

The curl request for text is shown below. In this example a txt file containing the text to be processed is being sent to a Nanowire flask API at `http:/0.0.0.0:5000`. The path `model/predict` is the default path for Nanowire flask APIs.

``curl -F "doc=@./doc1.txt" -XPOST http://0.0.0.0:5000/model/predict``

In the next example we have again sent text in a file however we have also defined the `deactivate_ngrams` variable as `True`. This will be fed to the user defined function in the `variables` object.

``curl -F "doc=@./doc1.txt" -XPOST http://0.0.0.0:5000/model/predict?deactivate_ngrams=True``

The user may also send raw text with the variables in a json using a command formatted as follows:

``curl -X POST -H "Content-Type:application/json" -d '{"text":"Example text about whichever subject you're interested in", "deactivate_ngrams"="True"}' http://0.0.0.0:5000/model/predict``

This may help a user who wishes to send text with variables as it is easier to generate these requests programatically.

### Images ###

The Nanowire flask library may also accept image objects.

The function you mount for image plugins, using the function ``mount_Image_function``,  must have the arguments ``img`` and ``variables``. The developer should expect ``img`` to be a PIL RGB image object and ``variables`` to be a dictionary containing the variables sent to the plugin in the curl request.

The currently supported image formats are:

* jpg
* png
* bmp
* tif
* ppm

The curl requests for images may be formatted 2 ways. The first involves sending the image as a file attached to the curl request. For example:

``curl -F "image=@./1.jpg" -XPOST http://0.0.0.0:5000/model/predict?threshold=0.5``

alternatively the file may be sent as a link using a dictionary eg.

``curl -X POST -H "Content-Type:application/json" -d '{"contentUrl":"http://127.0.0.1:8000/1.jpg", "threshold":0.5}' http://0.0.0.0:5000/model/predict``

### Spreadsheets ###

The Nanowire flask library may be made to accept spreadsheets using `mount_csv_function`. This function will provide the user defined tool with the variables `df`, the spreadsheet as a Pandas dataframe and `variables` a variables JSON. This function may be used to create APIs designed to process corpuses of documents or else time series data.

The user may send the library CSV objects using a command like

``curl -F "csv=@./example.csv" -XPOST http://0.0.0.0:5000/model/predict?ignore_col=text``

a xlsx file may be sent in the same way:

``curl -F "xlsx=@./example.xlsx" -XPOST 'http://0.0.0.0:5000/model/predict?ignore_col=text&customStops=horse,course&indexCol=uuid'``

alternatively a link to a csv or xlsx file may be sent such as:

``curl -X POST -H "Content-Type:application/json" -d '{"contentUrl":"http://localhost:8000/example.csv", "ignore_col":"dates"}' http://0.0.0.0:5000/model/predict``

### JSON data objects ###

The Nanowire flask library may also accept generic data stored in JSON format using `mount_json_function`. This function will only accept the one function, `inputJSON` and is designed to allow developers to produce tools for data formats which could not have been imagined by the creators of Nanowire flask. 

A JSON object may be sent to a Nanowire flask JSON tool using commands such as

``curl -X POST -H "Content-Type:application/json" -d '{"inputJSON": {"this":"is", "an":"example"}, "variables":{"customStops":["horse", "course"]}' http://0.0.0.0:5000/model/predict``

alternatively a JSON file may be sent from a server

``curl -X POST -H "Content-Type:application/json" -d '{"contentUrl":"http://localhost:8000/example.json"}' http://0.0.0.0:5000/model/predict``

an old version of this command would accept:

``curl -X POST -H "Content-Type:application/json" -d '{"this":"is", "an":"example"}' http://0.0.0.0:5000/model/predict``

however this is deprecated and will no longer be accepted in future versions of this library.

This library will eventually be expanded to be able to handle video, sound and arbitrary files however for now it is limited to text, images, csv files and json files.

The API you create will also return maximum memory usage (in MB), maximum cpu usage (in %) and time taken (in seconds) when processing a given API call.

Notes for developers
--------------------

This section contains a series of quick references for Nanowire flask developers. The first reference for developers should be the [Confluence pages](https://spotlightdata.atlassian.net/wiki/spaces/NDA/pages/1078951937/Nanowire+flask) however a 'cheat sheet' is shown below.


**text_tools.mount_text_function**

*Parameters*
* *function* :- The function to be mounted on the API. The function must take text and variables as arguments when processing text. The function must return a dictionary. 
* *host* :sup:`optional`:- default is '0.0.0.0'. Set the IP address to host the API on.
* *port* :sup:`optional`:- default 5000. Set the port to host the API on.
* *path* :sup:`optional`:- default '/model/predict'. Set the path for the API.

**image_tools.mount_Image_function**

*Parameters* 

* *function* :- The function to be mounted on the API. The function must take img and variables as arguments when processing images. The function must return a dictionary. 
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

If the post contains ``taskID`` as an argument the taskID given will also be returned in the output JSON. This is a legacy feature which may be removed in future versions.