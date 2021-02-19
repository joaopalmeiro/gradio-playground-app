from itertools import cycle
from pathlib import Path
from typing import Tuple

import gradio as gr
from gradio.networking import INITIAL_PORT_VALUE, LOCALHOST_NAME


def alternating_caps(input: str) -> Tuple[str, str]:
    # Source: https://stackoverflow.com/a/42939226.
    funcs = cycle([str.lower, str.upper])
    iNpUt = "".join(next(funcs)(c) for c in input.strip())

    html = Path("copy.html").read_text()

    return iNpUt, html


# More info: https://github.com/gradio-app/gradio/blob/master/gradio/interface.py#L46.
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
    css="custom.css",
    server_port=INITIAL_PORT_VALUE,
    server_name=LOCALHOST_NAME,
)

# iface.test_launch()

if __name__ == "__main__":
    print(LOCALHOST_NAME)
    print(INITIAL_PORT_VALUE)

    # iface.launch(inbrowser=True)
    iface.launch()
