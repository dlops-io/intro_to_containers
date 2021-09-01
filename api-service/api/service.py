import os
import math
import numpy as np
from fastapi import FastAPI, Path, Query, File
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from glob import glob

dataset_path = "/persistent/dataset"

# Setup FastAPI app
app = FastAPI(
    title="API Server",
    description="API Server",
    version="v1"
)

# Enable CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes


@app.get(
    "/",
    summary="Index",
    description="Root api"
)
async def get_index():
    return {
        "message": "Welcome to the API Service"
    }


@app.get("/get_demo_images")
async def get_demo_images():

    label_names = glob(os.path.join(dataset_path, '*'))
    print("Labels:", label_names)

    # Generate a list of labels and path to images
    data_list = []
    for label in label_names:
        # Images
        image_files = os.listdir(label)
        data_list.extend([(label.split("/")[-1], os.path.join(dataset_path, label, f))
                         for f in image_files])

    print("Full size of the dataset:", len(data_list))
    print("data_list:", data_list[:5])

    # Convert to json
    data_list = [{'label': itm[0], 'path':itm[1]} for itm in data_list]

    return data_list

# Additional routers here
