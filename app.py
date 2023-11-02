#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Srikanth Bashaboina
# Created Date: Fri Oct 27 16:57:59 +07 2023
# =============================================================================

from fastapi import FastAPI, File, Form, UploadFile
from typing import List
from model import imagetotext
import json
import os

folder_name = "files"
app = FastAPI() # create fastapi instance

@app.get("/model/status")
def model_info():
    """
    This is a test function where the application has been started from the fastapi to check the status.
    """
    return {"status": "running"}

@app.post("/model/upload_image")
def model_upload_image(file: UploadFile):
    """
    This function accepts the image as a file and parse it to the model to predict the caption
    and returns as the response.
    """

    # create the uploads folder
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
       
    file_location = f"{folder_name}/{file.filename}"

    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    # parsing file to model function
    load_image = imagetotext(file_location)

    response = {
        "filename": file.filename,
        "Image Caption": load_image
    }
    
    os.remove(f"{folder_name}/{file.filename}")
    return response

