from itertools import cycle

import gradio as gr


def alternating_caps(input):
    # Source: https://stackoverflow.com/a/42939226.
    funcs = cycle([str.lower, str.upper])
    iNpUt = "".join(next(funcs)(c) for c in input.strip())

    html = """
    <div class="examples">
    <button style="background-color: white; border: solid 1px lightgray;" class="btn" data-clipboard-action="copy" data-clipboard-target="div.output_text">
    Copy
    </button>

    <script src="https://cdn.jsdelivr.net/npm/clipboard@2.0.6/dist/clipboard.min.js"></script>
    
    <script>
    var clipboard = new ClipboardJS('.btn');

    clipboard.on('success', function (e) {
        console.log(e);
    });
    </script> 
    </div>
    """

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
)

# iface.test_launch()

if __name__ == "__main__":
    iface.launch(inbrowser=True)
