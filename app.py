from itertools import cycle
from pathlib import Path

import gradio as gr


def alternating_caps(input):
    # Source: https://stackoverflow.com/a/42939226.
    funcs = cycle([str.lower, str.upper])
    iNpUt = "".join(next(funcs)(c) for c in input.strip())

    html = Path("copy.html").read_text()

    return iNpUt, html


iface = gr.Interface(
    fn=alternating_caps,
    inputs=gr.inputs.Textbox(lines=1, placeholder="...", label="Input"),
    outputs=[gr.outputs.Textbox(label="Output"), gr.outputs.HTML(label="Clipboard")],
    verbose=True,
    title="Alternating caps",
    show_tips=False,
    allow_flagging=False,
    allow_screenshot=True,
    examples=[["Alternating caps"]],
    css="hide_column.css",
)

# iface.test_launch()

if __name__ == "__main__":
    iface.launch(inbrowser=True)
