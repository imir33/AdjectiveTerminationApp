from tkinter import *
import os


def displayFailureCase():
	global screen2
	screen2 = Toplevel(screen)
	screen2.title("Failure")
	screen2.geometry("300x150")
	Label(screen2, text = "").pack()
	Label(screen2, font=("Courier", 15), text = "Unrecognized case").pack()
	Label(screen2, text = "").pack()
	Button(screen2, text = "OK", command = delete2, font = small_font).pack()

def delete2():
    screen2.destroy()


def displayFailureArticle():
	global screen3
	screen3 = Toplevel(screen)
	screen3.title("Failure")
	screen3.geometry("300x150")
	Label(screen3, text = "").pack()
	Label(screen3, font=("Courier", 15), text = "Unrecognized article").pack()
	Label(screen3, text = "").pack()
	Button(screen3, text = "OK", command = delete3, font = small_font).pack()

def delete3():
    screen3.destroy()


def displayFailureSubstantive():
	global screen4
	screen4 = Toplevel(screen)
	screen4.title("Failure")
	screen4.geometry("300x150")
	Label(screen4, text = "").pack()
	Label(screen4, font=("Courier", 15), text = "Unrecognized gender").pack()
	Label(screen4, text = "").pack()
	Button(screen4, text = "OK", command = delete4, font = small_font).pack()

def delete4():
    screen4.destroy()


def display(t):
	global screen5
	screen5 = Toplevel(screen)
	screen5.title("Termination")
	screen5.geometry("300x150")
	Label(screen5, text = "").pack()
	Label(screen5, font=("Courier", 15), text = t).pack()
	Label(screen5, text = "").pack()
	Button(screen5, text = "OK", command = delete5, font = small_font).pack()

def delete5():
    screen5.destroy()


def determineTermination():
	article = articleVerify.get()
	substantive = substantiveVerify.get()
	case = caseVerify.get()

	articleEntry.delete(0, END)
	substantiveEntry.delete(0, END)
	caseEntry.delete(0, END)

	if article == "definite":
		if substantive == "masculine":
			if case == "nominative":
				display("Der +e")
			elif case == "accusative":
				display("Den +en")
			elif case == "dative":
				display("Dem +en")
			elif case == "genitive":
				display("Des +en")
			else:
				displayFailureCase()
		elif substantive == "feminine":
			if case == "nominative":
				display("Die +e")
			elif case == "accusative":
				display("Die +e")
			elif case == "dative":
				display("Der +en")
			elif case == "genitive":
				display("Der +en")
			else:
				displayFailureCase()
		elif substantive == "neuter":
			if case == "nominative":
				display("Das +e")
			elif case == "accusative":
				display("Das +e")
			elif case == "dative":
				display("Dem +en")
			elif case == "genitive":
				display("Des +en")
			else:
				displayFailureCase()
		elif substantive == "plural":
			if case == "nominative":
				display("Die +en")
			elif case == "accusative":
				display("Die +en")
			elif case == "dative":
				display("Den +en")
			elif case == "genitive":
				display("Der +en")
			else:
				displayFailureCase()
		else:
			displayFailureSubstantive()
	elif article == "indefinite":
		if substantive == "masculine":
			if case == "nominative":
				display("Ein +er")
			elif case == "accusative":
				display("Einen +en")
			elif case == "dative":
				display("Einem +en")
			elif case == "genitive":
				display("Eines +en")
			else:
				displayFailureCase()
		elif substantive == "feminine":
			if case == "nominative":
				display("Eine +e")
			elif case == "accusative":
				display("Eine +e")
			elif case == "dative":
				display("Einer +en")
			elif case == "genitive":
				display("Einee +en")
			else:
				displayFailureCase()
		elif substantive == "neuter":
			if case == "nominative":
				display("Ein +es")
			elif case == "accusative":
				display("Ein +es")
			elif case == "dative":
				display("Einem +en")
			elif case == "genitive":
				display("Eines +en")
			else:
				displayFailureCase()
		elif substantive == "plural":
			if case == "nominative":
				display("Keine +en")
			elif case == "accusative":
				display("Keine +en")
			elif case == "dative":
				display("Keinen +en")
			elif case == "genitive":
				display("Keiner +en")
			else:
				displayFailureCase()
		else:
			displayFailureSubstantive()
	elif article == "no article":
		if substantive == "masculine":
			if case == "nominative":
				display("+er")
			elif case == "accusative":
				display("+en")
			elif case == "dative":
				display("+em")
			elif case == "genitive":
				display("+en")
			else:
				displayFailureCase()
		elif substantive == "feminine":
			if case == "nominative":
				display("+e")
			elif case == "accusative":
				display("+e")
			elif case == "dative":
				display("+er")
			elif case == "genitive":
				display("+er")
			else:
				displayFailureCase()
		elif substantive == "neuter":
			if case == "nominative":
				display("+es")
			elif case == "accusative":
				display("+es")
			elif case == "dative":
				display("+em")
			elif case == "genitive":
				display("+en")
			else:
				displayFailureCase()
		elif substantive == "plural":
			if case == "nominative":
				display("+e")
			elif case == "accusative":
				display("+e")
			elif case == "dative":
				display("+en")
			elif case == "genitive":
				display("+er")
			else:
				displayFailureCase()
		else:
			displayFailureSubstantive()
	else:
		displayFailureArticle()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("800x400")
    screen.title("Adjective Termination")

    global small_font
    small_font = ('Verdana',10)
    large_font = ("Verdana", 100)

    global articleEntry
    global substantiveEntry
    global caseEntry

    global articleVerify
    articleVerify = StringVar()
    Label(text = "").pack()
    Label(text = "").pack()
    Label(font=("Courier", 15), text = "Article type (Definite, Indefinite, No Article)").pack()
    articleEntry = Entry(textvariable = articleVerify, width = "55", font = "large_font")
    articleEntry.pack()

    global substantiveVerify
    substantiveVerify = StringVar()
    Label(text = "").pack()
    Label(text = "").pack()
    Label(font=("Courier", 15), text = "Substantive type (Masculine, Feminine, Neuter, Plural)").pack()
    substantiveEntry = Entry(textvariable = substantiveVerify, width = "55", font = "large_font")
    substantiveEntry.pack()

    global caseVerify
    caseVerify = StringVar()
    Label(text = "").pack()
    Label(text = "").pack()
    Label(font=("Courier", 15), text = "Case type (Nominative, Accusative, Dative, Genitive)").pack()
    caseEntry = Entry(textvariable = caseVerify, width = "55", font = "large_font")
    caseEntry.pack()

    Label(text = "").pack()
    Label(text = "").pack()
    Button(text = "Determine Termination", width = "30", height = "1", font = small_font, command = determineTermination).pack()

    screen.mainloop()


main_screen()