"""Connects the page to dedupe.py. Runs in the browser through PyScript."""
import asyncio

from pyscript import document, window, when

from dedupe import remove_duplicates

input_box = document.querySelector("#input")
output_box = document.querySelector("#output")
status = document.querySelector("#status")
copy_btn = document.querySelector("#copy")


def run(event=None):
    text = input_box.value
    if not text.strip():
        output_box.value = ""
        status.textContent = "Paste a list to get started."
        copy_btn.disabled = True
        return

    result, removed, kept = remove_duplicates(
        text,
        ignore_case=document.querySelector("#ignore-case").checked,
        trim_spaces=document.querySelector("#trim").checked,
        sort_az=document.querySelector("#sort").checked,
    )
    output_box.value = result
    noun = "duplicate" if removed == 1 else "duplicates"
    status.textContent = f"{removed} {noun} removed. {kept} unique lines left."
    copy_btn.disabled = False


for selector, evt in [("#input", "input"), ("#ignore-case", "change"),
                      ("#trim", "change"), ("#sort", "change")]:
    document.querySelector(selector).addEventListener(evt, run)


@when("click", "#copy")
async def copy_result(event):
    try:
        await window.navigator.clipboard.writeText(output_box.value)
    except Exception:
        # Fallback for browsers that block the clipboard API
        output_box.select()
        output_box.setSelectionRange(0, 999999)
        document.execCommand("copy")
    copy_btn.textContent = "Copied"
    await asyncio.sleep(1.5)
    copy_btn.textContent = "Copy result"


run()
