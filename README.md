#Download and Save a pdf file

A pytest project that downloads a pdf file and verifies the download path.
It consists of the following steps-
- Visit the website
- Click on the pdf link to open it on the new tab
- Get the url from the new tab
- Download the pdf and save it locally
- Verify whether the file exists in the said directory

##Installation

Install the requirements from the `requirements.txt` file.

##Run

To run the test, traverse to the `tests` directory. Within `tests` directory run the following command-

`pytest test_pdf_download.py`

##config

To change the pdf download path update the `pdf_path` in the config file. 