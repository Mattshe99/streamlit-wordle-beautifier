import streamlit as st

# Define multiple beautifier options
beautifier_options = {
    "Hearts 🖤💛💚": {
        "⬛": "🖤",  # Black square
        "🟨": "💛",  # Yellow square
        "🟩": "💚"   # Green square
    },
    "Symbols ❌⚠️✔️": {
        "⬛": "❌",  # Black square
        "🟨": "⚠️",  # Yellow square
        "🟩": "✔️"   # Green square
    },
    "Cars 🚓🚕🚙": {
        "⬛": "🚓",  # Black square
        "🟨": "🚕",  # Yellow square
        "🟩": "🚙"   # Green square
    },
    "Nature 🌚☀️🍀": {
        "⬛": "🌚",  # Black square
        "🟨": "☀️",  # Yellow square
        "🟩": "🍀"   # Green square
    },
    "Animals 🕷️🐤🐸": {
        "⬛": "🕷️",
        "🟨": "🐤",  # Yellow square
        "🟩": "🐸"   # Green square
    },
    "Fruit 🥥🍋🍏": {
        "⬛": "🥥",  # Black square
        "🟨": "🍋",  # Yellow square
        "🟩": "🍏"   # Green square
    },
    "Vegetables 🥔🌽🥒": {
        "⬛": "🥔",  # Black square
        "🟨": "🌽",  # Yellow square
        "🟩": "🥒"   # Green square
    },
    "Faces 👨🏿👨🤢": {
        "⬛": "👨🏿",  # Black square
        "🟨": "👨",  # Yellow square
        "🟩": "🤢"   # Green square
    }
}

# App title
st.title("Wordle Beautifier")

st.text("For when blocks are boring.")

# Input for Wordle result with increased height
wordle_input = st.text_area(
    "Paste your Wordle result here:",
    placeholder="e.g.,\nWordle 1,285 3/6\n\n⬛🟨⬛🟩⬛\n⬛⬛🟩🟩🟩\n🟩🟩🟩🟩🟩",
    height=215
)

# Dropdown for selecting a beautifier theme
theme = st.selectbox("Choose a beautifier theme:", options=list(beautifier_options.keys()))

# "Apply" button
if st.button("Apply"):
    if wordle_input.strip():
        # Get the selected emoji map
        emoji_map = beautifier_options[theme]

        # Replace emojis based on the selected theme
        beautified_result = wordle_input
        for original, replacement in emoji_map.items():
            beautified_result = beautified_result.replace(original, replacement)

        # Append the footer
        beautified_result += "\n\nMade with wordlebeautify.streamlit.app"

        # Display the beautified result
        st.subheader("Beautified Wordle Result:")
        st.code(beautified_result, language="markdown")

        # Copy to clipboard button
        st.button("Copy to Clipboard")  # Add clipboard functionality with Pyperclip if desired
    else:
        st.error("Please paste your Wordle result to apply the beautifier!")

# Footer
st.caption("Made with 🍞 in 🇳🇿")
