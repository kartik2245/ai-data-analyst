from io import BytesIO
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer


def generate_report(
    df,
    insights,
    question="",
    answer=""
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>AI DATA ANALYST REPORT</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>Dataset Summary</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Rows : {df.shape[0]}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Columns : {df.shape[1]}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Missing Values : {df.isnull().sum().sum()}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Duplicate Rows : {df.duplicated().sum()}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>AI Insights</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            insights.replace("\n","<br/>"),
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>Latest Question</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            question,
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,10))

    story.append(
        Paragraph(
            "<b>Latest Answer</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            answer.replace("\n","<br/>"),
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"Generated on : {datetime.now()}",
            styles["Italic"]
        )
    )

    doc.build(story)

    buffer.seek(0)

    return buffer