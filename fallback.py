# fallback.py – wird nur benutzt, wenn daily_report.py keine report.pdf erzeugt
from reportlab.pdfgen import canvas
from datetime import datetime, timezone

c = canvas.Canvas("report.pdf")
c.drawString(72, 800, "Report (Fallback) - kein Live-Output vom Script")
c.drawString(72, 780, "Generated: " + datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
c.save()
