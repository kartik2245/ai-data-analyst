import matplotlib.pyplot as plt


def draw_chart(df, agent):

    chart = agent["chart"].lower()

    fig, ax = plt.subplots(figsize=(8, 5))

    if chart == "histogram":

        column = agent["column"]

        if column not in df.columns:
            return None, f"Column '{column}' not found."

        ax.hist(df[column], bins=30)

        ax.set_title(f"Histogram of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")

    elif chart == "bar":

        column = agent["column"]

        if column not in df.columns:
            return None, f"Column '{column}' not found."

        df[column].value_counts().plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(f"Bar Chart of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Count")

    elif chart == "pie":

        column = agent["column"]

        if column not in df.columns:
            return None, f"Column '{column}' not found."

        df[column].value_counts().plot(
            kind="pie",
            autopct="%1.1f%%",
            ax=ax
        )

        ax.set_title(f"Pie Chart of {column}")
        ax.set_ylabel("")

    elif chart == "scatter":

        x = agent["x"]
        y = agent["y"]

        if x not in df.columns:
            return None, f"Column '{x}' not found."

        if y not in df.columns:
            return None, f"Column '{y}' not found."

        ax.scatter(
            df[x],
            df[y]
        )

        ax.set_title(f"{y} vs {x}")
        ax.set_xlabel(x)
        ax.set_ylabel(y)

    elif chart == "line":

        x = agent["x"]
        y = agent["y"]

        if x not in df.columns:
            return None, f"Column '{x}' not found."

        if y not in df.columns:
            return None, f"Column '{y}' not found."

        ax.plot(
            df[x],
            df[y]
        )

        ax.set_title(f"{y} vs {x}")
        ax.set_xlabel(x)
        ax.set_ylabel(y)

    else:

        plt.close(fig)
        return None, "Unsupported chart type."

    plt.tight_layout()

    return fig, None

def save_chart(figure):

    import io

    buffer = io.BytesIO()

    figure.savefig(
        buffer,
        format="png",
        dpi=300,
        bbox_inches="tight"
    )

    buffer.seek(0)

    return buffer