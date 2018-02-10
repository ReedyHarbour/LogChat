from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import time
from export import *
import sort
import user

stylesheet=getSampleStyleSheet()

# Formatting PDF files using reportlab

def drawTime(textList, style):
	newList = []
	for text in textList:
		newLine = "<strong>"+text.getActualTime()+"</strong>-"+"<i>"+text.user+"</i>: "+text.content
		newList.append(Paragraph(newLine, style=style))
	return newList

def exportToPDF(alltext):

	styles = getSampleStyleSheet()
	styleN = styles['Normal']
	styleH = styles['Heading1']
	# Cited from https://www.reportlab.com/docs/reportlab-userguide.pdf
	body = ParagraphStyle(fontName='Times', fontSize=12, name="TOCHeading1",
 			firstLineIndent=40, leading=16,spaceAfter = 6, spaceBefore = 6)
	heading = ParagraphStyle(fontName='Times-Bold', fontSize=16, name="TOCHeading1",
			leading=16,spaceAfter = 12, spaceBefore = 6, alignment=1)
	heading1 = ParagraphStyle(fontName='Times-Bold', fontSize=14, name="TOCHeading1",
			firstLineIndent=10, leading=16,spaceAfter = 12, spaceBefore = 6)
	heading2 = ParagraphStyle(fontName='Times-Bold', fontSize=12, name="TOCHeading1",
			firstLineIndent=15, leading=16,spaceAfter = 12, spaceBefore = 6)
	story = []

	# add some flowables
	title = Paragraph("Work Log",heading)
	story.append(title)

	modeList = sort.filterByMode(alltext,usefulMode = [0,1,2])
	for i in range(len(modeList)):
		# drawString mode
		modeName = user.mode[i]
		p = Paragraph(modeName,heading1)
		story.append(p)
		d = filterByTime(modeList[i])
		# drawString day
		for key in d:
			k = str(key)[1:-1]
			story.append(Paragraph(k,heading2))
			story.extend(drawTime(d[key], body))

	c = canvas.Canvas("Work.pdf", pagesize=letter)
	c.setLineWidth(.3)
	c.setFont('Helvetica', 12)

	f = Frame(inch, inch, 7*inch, 9*inch)
	f.addFromList(story,c)
	c.save()
