from datetime import datetime

class bcolors:
	PURPLE = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def log_print(message = "", colorStyle = "default", bcolor = None):

	if not bcolor:

		if colorStyle == "primary":
			bcolor = bcolors.OKBLUE

		elif colorStyle == "warning":
			bcolor = bcolors.WARNING

		elif colorStyle == "danger":
			bcolor = bcolors.FAIL

		elif colorStyle == "success":
			bcolor = bcolors.OKGREEN

		elif colorStyle == "default":
			bcolor = bcolors.PURPLE

	print(f"{bcolor}{datetime.now()} | {message}{bcolors.ENDC}")