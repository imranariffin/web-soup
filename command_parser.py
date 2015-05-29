# from soupFunctions import *
from classes import *

commands = {
	"print" : []
}

global web_page
web_page = "null"
global returnVal

def command_parser (command_line):
	instructions = command_line.split();

	#check if empty input
	if len(instructions) == 0:
		print "no command"
		return -1

	#do command
	command = instructions[0]
	do_command(command, instructions)

	return instructions

def main_parser():

	while True:
		command_line = raw_input("> ")
		command_parser(command_line)

		#break condition
		if command_line == "exit":
			break

	#exiting main_parser
	print "exiting main_parser ..."
	return 0

def do_command(command, instructions):

	if command == "getpagelinks":
		#validate command line
		if len(instructions) != 2:
			print "Error: not enough argument \n "
			print "get_page_links() requires one argument: url"
			return -1

		url = instructions[1]
		print "do get_page_links"
		url = make_valid_url(url)
		returnVal = get_page_links(url)

		print returnVal
		
		return returnVal

	elif command == "getpagelinksall":
		if len(instructions) != 2:
			print "Error: not enough argument \n "
			print "get_page_links_all() requires one argument: url"
			return -1

		url = instructions[1];
		print "do get_page_links_all"
		links = []
		returnVal = get_page_links_all(url, links)

		print returnVal

		return returnVal

	elif command == "createweb":
		print "creating a web (root page)"
		if len(instructions) != 2:
			print "Error: not enough argument \n "
			print "create_web() requires one argument: url"
			return -1

		url = instructions[1]
		url = make_valid_url(url)
		print "typeof second instruction: " + str(type(url))
		print "do create_web"
		# global web_page
		web_page = create_web(url)
		returnVal = web_page

		return returnVal

	elif command == "showweb":

		if len(instructions) == 1:
			print "web_page: "

			global web_page

			if web_page != "null":
				print_web(web_page)
				return True

			print web_page
			return False

		elif len(instructions) == 2:
			option = instructions[1]
			if option == "links":
				print "web_page links:"
				print_list(web_page.links)
				return True

		elif len(instructions) == 3:
			option1 = instructions[1]
			if option1 == "links":
				option2 = instructions[2]
				if option2 == "relative":
					print "showing web_page links relative"
					rel_links = web_page.get_rel_links()
					print_list(rel_links)
				return "wrong option2"
			return "wrong option1"

		print "wrong option: too many options"
		return False

	elif command == "web":
		if len(instructions) == 1:
			print "insufficient argument"
			return -2

		elif len(instructions) == 2:
			print "command option"
			option = instructions[1]
			if option == "showpage":
				print "showing child pages"
				web_page.show_all_pages()
				return True

			if option == "addpage":
				print "wrong option: addpage needs third arg: url"
				return False

			print "wrong option"
			return False

		elif len(instructions) == 3:
			option = instructions[1]

			if option == "addpage":
				# add one child page
				# option2 = child_url
				option2 = instructions[2]
				if is_relative_url(option2):
					child_url = option2
					# print "adding one child page: SoupPage(" + child_url + ")"
					web_page.add_child_page(web_page.link, child_url)
					return True

				return False

			if option == "showpage":
				option2 = instructions[2]
				if is_relative_url(option2) and option2 in web_page.links:
					child_url = option2
					child_page = web_page.pages[option2]
					print "child page: "
					print_web(child_page)
					return True

				print "wrong option: url is not relative and not in web links"
				return False

			if option == "open":
				option2 = instructions[2]

				if option2 in web_page.links:
					html = web_page.pages[option2]
					openpage(html)
					return True

				return False

			else:
				print "wrong option"
				print False

		if len(instructions) == 2:
			print "wrong option: " + option + " needs third arg: url"
		else:
			print "wrong option: too many options"
		return False

	elif command == "exit":
		return 0

	else:
		print "invalid command"
		return -1