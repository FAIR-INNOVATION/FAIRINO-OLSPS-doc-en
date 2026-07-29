"""Sphinx directive for one numbered figure containing two side-by-side images."""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class FigureRowDirective(SphinxDirective):
    required_arguments = 2
    optional_arguments = 2
    final_argument_whitespace = False
    has_content = True
    option_spec = {
        "alt-1": directives.unchanged,
        "alt-2": directives.unchanged,
        "alt-3": directives.unchanged,
        "alt-4": directives.unchanged,
        "class": directives.class_option,
        "name": directives.unchanged,
    }

    def run(self):
        self.assert_has_content()

        classes = ["figure-row", "align-center"]
        classes.extend(self.options.get("class", []))
        figure = nodes.figure("", classes=classes)
        self.set_source_info(figure)
        self.add_name(figure)

        image_row = nodes.container(
            "",
            classes=[
                "figure-row-images",
                f"figure-row-images-{len(self.arguments)}",
            ],
        )
        for index, uri in enumerate(self.arguments, start=1):
            alt_text = self.options.get(f"alt-{index}", "")
            image = nodes.image("", uri=directives.uri(uri), alt=alt_text)
            image["classes"].append("figure-row-image")
            self.set_source_info(image)
            image_row += image
        figure += image_row

        parsed = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, parsed)
        if not parsed or not isinstance(parsed[0], nodes.paragraph):
            error = self.state_machine.reporter.error(
                "figure-row requires a caption paragraph.",
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
            )
            return [error]

        first = parsed[0]
        figure += nodes.caption(first.rawsource, "", *first.children)
        if len(parsed) > 1:
            figure += nodes.legend("", *parsed[1:])
        return [figure]


def setup(app):
    app.add_directive("figure-row", FigureRowDirective)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
