from itertools import cycle

import gradio as gr


def alternating_caps(input):
    # Source: https://stackoverflow.com/a/42939226.
    funcs = cycle([str.lower, str.upper])

    return "".join(next(funcs)(c) for c in input.strip())


iface = gr.Interface(
    fn=alternating_caps,
    inputs=gr.inputs.Textbox(lines=1, placeholder="...", label="Input"),
    outputs="text",
    verbose=True,
    title="Alternating caps",
    show_tips=False,
    allow_flagging=False,
    allow_screenshot=True,
    examples=[["Alternating caps"]],
)

# iface.test_launch()

if __name__ == "__main__":
    iface.launch(inbrowser=True)
