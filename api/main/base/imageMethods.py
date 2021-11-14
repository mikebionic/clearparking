import os, sys, shutil
import secrets
from PIL import Image
from datetime import datetime

from flask import current_app
from main.config import Config

def allowed_image(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_IMAGE_EXTENSIONS

def allowed_icon(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_ICON_EXTENSIONS

def dirHandler(path):
	if not os.path.exists(path):
		try:
			os.makedirs(path)
		except Exception as ex:
			print("error creating directory")

def changeImageSize(
	imageFile,
	modulePath,
	FileName,
	image_file_opened = None,
	apply_watermark = False):

	output_sizes = {
		"R": None,
		"M": (800,600),
		"S": (320,240),
	}
	paths={}

	watermark_image_path = os.path.join(
		Config.STATIC_FOLDER_LOCATION,
		Config.WEB_CONFIG_DIRECTORY,
		'watermark.png')

	for size in output_sizes:
		# image = image_file_opened if image_file_opened else Image.open(imageFile)

		image = Image.open(imageFile)

		# create path according to a size abobe like "/images/M/blahblah.jpg"
		sizeSpecificFullPath = os.path.join(Config.STATIC_FOLDER_LOCATION, modulePath, size)
		# check that it exists or create one
		dirHandler(sizeSpecificFullPath)

		# makes the "module/id/R/blahblah.jpg" (required for db path info)
		FilePath = os.path.join(modulePath,size,FileName)

		# join the fullPath with filename to save to
		saving_path = os.path.join(sizeSpecificFullPath,FileName)

		if not output_sizes[size]:
			if (Config.ADD_RESOURCE_WATERMARK == True and apply_watermark == True):
				watermark = Image.open(watermark_image_path).resize(image.size)
				image.paste(watermark,(0,0),mask=watermark)
			
			image.save(saving_path,optimize=True,quality=65)
			paths[f"FilePath{size}"]=FilePath

		else:
			image.thumbnail(output_sizes[size])

			if (Config.ADD_RESOURCE_WATERMARK == True and apply_watermark == True):
				if size != 'S':
					print("adding watermark")
					watermark = Image.open(watermark_image_path).resize(image.size)
					image.paste(watermark,(0,0),mask=watermark)

			image.save(saving_path)
			paths[f"FilePath{size}"]=FilePath

	paths["FilePath"]=os.path.join(modulePath,"<FSize>",FileName)

	return paths


def save_image(
	imageForm = None,
	savedImage = None,
	module = "undefined",
	id = "undefined",
	apply_watermark = False,
	image_name = None):
	image = None
	saving_path = None
	if (image_name and Config.USE_PROVIDED_IMAGE_FILENAME == True):
		image_file_name = image_name
	else:
		image_file_name = secrets.token_hex(Config.IMAGE_RANDOM_HEX_LENGTH)

	modulePath = os.path.join(str(module),str(id),'images')
	sizeSpecificFullPath = None

	if not imageForm:
		image = Image.open(savedImage)
		image = image.convert('RGBA')
		image.save(savedImage)
		saving_path = savedImage
		image = Image.open(savedImage)
		_, f_ext = os.path.splitext(image.filename)
		FileName = image_file_name + f_ext

	if imageForm:
		# need to save the file to proceed compression and resizing if imageForm
		_, f_ext = os.path.splitext(imageForm.filename)
		FileName = image_file_name + f_ext
		size = "dump"

		sizeSpecificFullPath = os.path.join(Config.STATIC_FOLDER_LOCATION, modulePath, size)
		dirHandler(sizeSpecificFullPath)
		FilePath = os.path.join(modulePath,size,FileName)
		saving_path = os.path.join(sizeSpecificFullPath,FileName)
		imageForm.save(saving_path)
		# print('it was a form now saved into:')
		# print(saving_path)

	response = {
		"FileName":FileName
	}
	resizing = changeImageSize(
		imageFile = saving_path,
		modulePath = modulePath,
		FileName = FileName,
		# image_file_opened = image,
		apply_watermark = apply_watermark)
	
	if sizeSpecificFullPath:
		try:
			shutil.rmtree(sizeSpecificFullPath)
		except Exception as ex:
			print(f"{datetime.now()} | Image utils tree removing Exception: {ex}")
	for image in resizing:
		response[image]=resizing[image]
	return response

# save_image(savedImage='IMG_5660.JPG',module="commerce/users",id=12)

def save_icon(
	imageForm = None,
	savedImage = None,
	module = "undefined",
	id = None,
	randomName = True):
	random_hex = secrets.token_hex(Config.IMAGE_RANDOM_HEX_LENGTH)

	if id:
		modulePath = os.path.join(str(module),str(id),'images')
	else:
		modulePath = os.path.join(str(module))

	if not imageForm:
		print('module not working for saved image')
		# image = Image.open(savedImage)
		# _, f_ext = os.path.splitext(image.filename)
		# FileName = random_hex + f_ext

	if imageForm:
		_, f_ext = os.path.splitext(imageForm.filename)
		FileName = random_hex + f_ext
		if randomName == False:
			FileName = imageForm.filename

		sizeSpecificFullPath = os.path.join(Config.STATIC_FOLDER_LOCATION, modulePath)
		dirHandler(sizeSpecificFullPath)
		FilePath = os.path.join(modulePath,FileName)
		saving_path = os.path.join(sizeSpecificFullPath,FileName)
		imageForm.save(saving_path)
		print('it was a form now saved into:')
		print(saving_path)
		
	response = {
		"FileName":FileName,
		"FilePath":FilePath,
	}
	return response