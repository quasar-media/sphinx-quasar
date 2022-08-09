import pygments.styles.bw
from pygments.token import Generic, String


class BlackWhiteStyle(pygments.styles.bw.BlackWhiteStyle):
    styles = {
        **pygments.styles.bw.BlackWhiteStyle.styles,
        String: "",
        Generic.Emph: "",
    }
